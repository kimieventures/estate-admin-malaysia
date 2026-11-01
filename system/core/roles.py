"""RBAC — peranan & kebenaran (rangka-pembangunan-sistem.md §3, §7)."""
from enum import Enum


class Role(str, Enum):
    PEMOHON = "pemohon"
    PETUGAS = "petugas_kes"
    PEGUAM = "peguam"
    PAKAR_SYARIAH = "pakar_syariah"
    PENYELIA = "penyelia_kanan"
    PEGAWAI_KEWANGAN = "pegawai_kewangan"
    AGENSI = "pegawai_agensi"
    MAHKAMAH = "mahkamah"
    AUDITOR = "auditor"
    ADMIN = "admin"


# Kebenaran per peranan — prinsip: auditor baca-sahaja; pemohon tak boleh
# meluluskan pintu; hanya pasangan berkuasa pada peringkat masing-masing.
ROLE_PERMISSIONS = {
    Role.PEMOHON: {"case.view_own", "case.submit_input", "case.qa", "case.upload_doc"},
    Role.PETUGAS: {"case.view", "gate.decide", "doc.verify", "qa.engage", "case.coordinate"},
    Role.PEGUAM: {"case.view", "gate.decide", "advice.review", "qa.engage"},
    Role.PAKAR_SYARIAH: {"case.view", "gate.decide", "calc.review", "advice.review", "qa.engage"},
    Role.PENYELIA: {"case.view", "gate.decide", "gate.eskalasi", "qc.spotcheck", "norm.panel"},
    Role.PEGAWAI_KEWANGAN: {"case.view", "ledger.review", "fee.exception_review"},
    Role.AGENSI: {"case.view_limited", "agency.confirm", "gate.decide"},
    Role.MAHKAMAH: {"case.view_limited", "gate.confirm_final", "gate.decide"},
    Role.AUDITOR: {"audit.read", "audit.recompute"},
    Role.ADMIN: {"users.manage", "norms.govern", "system.config", "backup.run"},
}


def can(role: Role, permission: str) -> bool:
    """Semak kebenaran peranan."""
    return permission in ROLE_PERMISSIONS.get(role, set())
