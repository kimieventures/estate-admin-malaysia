"""Workflow Stage-Gate 11 Pintu — model pasangan agent-human (P3: tiada lulus, tiada maju).

Setiap kemajuan peringkat: output agent → disemak human partner (RBAC ikut
peringkat) → keputusan (LULUS/TOLAK/ESKALASI) → rekod audit hash-chain
dengan asas statutori per peringkat.
"""
from enum import Enum

from .audit import AuditTrail
from .case import Case, Stage
from .roles import Role


class Decision(str, Enum):
    LULUS = "LULUS"
    TOLAK = "TOLAK"
    ESKALASI = "ESKALASI"


class WorkflowError(Exception):
    """Pelanggaran pintu / kuasa pasangan."""


# Nama pintu & asas statutori per peringkat — konsep-model-agent-human.md §3
STAGE_GATE_NAME = {
    Stage.S0: "PINTU 0 — identiti & dokumen asal disahkan",
    Stage.S1: "PINTU 1 — laluan disepakati + anggaran fi dipaparkan",
    Stage.S2: "PINTU 2 — dokumen 100% sahih & lengkap",
    Stage.S3: "PINTU 3 — nasihat disemak pakar",
    Stage.S4: "PINTU 4 — kiraan disemak & tanpa bantahan",
    Stage.S5: "PINTU 5 — sifar pelanggaran norma kritikal",
    Stage.S6: "PINTU 6 — kertas kes dilulus",
    Stage.S7: "PINTU 7 — KUASA LUARAN: perintah/geran diterbit",
    Stage.S8: "PINTU 8 — setiap tugas pelaksanaan disahkan",
    Stage.S9: "PINTU 9 — MAHKAMAH: lejar seimbang & rumusan disahkan",
    Stage.S10: "PINTU 10 — pemohon terima keputusan; kes ditutup",
}

STAGE_LEGAL_BASIS = {
    Stage.S0: "KYC; dokumen rasmi JPN",
    Stage.S1: "Act 532 s.17(1); Akta 98+A1643; Act 97; Akta 505 s.50",
    Stage.S2: "Borang A; senarai semak JBG",
    Stage.S3: "kes Latifah [2007] twin-track; fatwa MKI",
    Stage.S4: "faraid (Al-Nisa' 11/12/176); Akta 300 s.6(1); Akta 303 s.122",
    Stage.S5: "Perpustakaan Norma bercitation",
    Stage.S6: "Act 97 s.30 (senarai aset); format agensi",
    Stage.S7: "Akta 98 (perintah); Act 97 (geran); Akta 505 s.50 (sijil faraid)",
    Stage.S8: "NLC s.346 + Borang 14A; Akta 370 s.13; Akta KWSP s.54(1A)",
    Stage.S9: "kuasa kehakiman (muktamad); duty to account pentadbir",
    Stage.S10: "penyampaian & penutupan",
}

# Siapa BERKUASA meluluskan pintu setiap peringkat (pasangan berperanan)
APPROVERS = {
    Stage.S0: {Role.PETUGAS},
    Stage.S1: {Role.PETUGAS},
    Stage.S2: {Role.PETUGAS},
    Stage.S3: {Role.PEGUAM, Role.PAKAR_SYARIAH},
    Stage.S4: {Role.PAKAR_SYARIAH, Role.PETUGAS, Role.PEGUAM},
    Stage.S5: {Role.PETUGAS, Role.PENYELIA},
    Stage.S6: {Role.PEGUAM, Role.PAKAR_SYARIAH, Role.PETUGAS},
    Stage.S7: {Role.AGENSI},          # kuasa luaran
    Stage.S8: {Role.PETUGAS},
    Stage.S9: {Role.MAHKAMAH},        # pengesahan muktamad
    Stage.S10: {Role.PETUGAS},
}


class CaseWorkflow:
    """Enjin pintu untuk satu kes + audit trail."""

    def __init__(self, case: Case, audit: AuditTrail):
        self.case = case
        self.audit = audit
        self.audit.append(
            actor="system", role="system", action="case.dibuka",
            stage=case.current_stage.name, legal_basis=None,
            payload={
                "case_id": case.case_id,
                "si_mati": case.deceased_name,
                "agama": case.religion,
                "wasiat": case.has_will,
                "nilai_rm": case.total_value,
            },
        )

    @property
    def gate_name(self) -> str:
        return STAGE_GATE_NAME[self.case.current_stage]

    def decide(self, approver: str, role: Role, decision: Decision,
               reason: str = "", payload: dict | None = None) -> Stage:
        """Keputusan pintu oleh human partner; kemajuan hanya jika LULUS."""
        stage = self.case.current_stage
        if role not in APPROVERS[stage]:
            raise WorkflowError(
                f"CHECK & BALANCE: peranan '{role.value}' TIADA kuasa meluluskan "
                f"{stage.name} ({self.gate_name})"
            )
        self.audit.append(
            actor=approver, role=role.value, action=f"gate.{decision.value}",
            stage=stage.name, legal_basis=STAGE_LEGAL_BASIS[stage],
            payload={"sebab": reason, **(payload or {})},
        )
        if decision is Decision.LULUS:
            if stage is Stage.S10:
                self.case.closed = True   # kes selesai — PINTU 10 terakhir
            else:
                self.case.current_stage = Stage(stage.value + 1)
        # TOLAK / ESKALASI: kekal pada peringkat sama (rekod telah dibuat)
        return self.case.current_stage
