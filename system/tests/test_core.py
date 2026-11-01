"""Ujian pengesahan modul asas — aliran penuh, audit tamper-evident,
sekatan norma PERLU SAHKAN, RBAC pintu (check & balance).
"""
import unittest

from system.core.audit import AuditTrail
from system.core.case import Asset, Case, Stage
from system.core.norms import (
    NormNotVerifiedError,
    NormStatus,
    check_trigger,
    enforce,
    get_norm,
)
from system.core.roles import Role, can
from system.core.workflow import CaseWorkflow, Decision, WorkflowError


def make_case() -> Case:
    return Case(
        case_id="EA-2026-0001",
        deceased_name="Ahmad bin Ismail",
        religion="Islam",
        has_will=False,
        total_value=1_200_000,
    )


# (actor, role) bagi pintu S0 → S10 — pasangan berperanan ikut APPROVERS
APPROVAL_SEQ = [
    ("petugas", Role.PETUGAS),        # S0
    ("petugas", Role.PETUGAS),        # S1
    ("petugas", Role.PETUGAS),        # S2
    ("ustaz-dr", Role.PAKAR_SYARIAH),  # S3
    ("ustaz-dr", Role.PAKAR_SYARIAH),  # S4
    ("penyelia", Role.PENYELIA),      # S5
    ("peguam", Role.PEGUAM),          # S6
    ("ppkp", Role.AGENSI),            # S7 — kuasa luaran
    ("petugas", Role.PETUGAS),        # S8
    ("mahkamah", Role.MAHKAMAH),      # S9 — pengesahan muktamad
    ("petugas", Role.PETUGAS),        # S10
]


class TestWorkflow(unittest.TestCase):
    def test_aliran_penuh_11_pintu(self):
        """Kes lulus semua pintu oleh pasangan betul → kes DITUTUP."""
        case, audit = make_case(), AuditTrail()
        wf = CaseWorkflow(case, audit)
        for actor, role in APPROVAL_SEQ:
            wf.decide(actor, role, Decision.LULUS, reason="uji-aliran")
        self.assertTrue(case.closed)
        self.assertEqual(case.current_stage, Stage.S10)

    def test_tolak_tidak_maju(self):
        """Pintu TOLAK — kes kekal peringkat sama (P3: tiada lulus tiada maju)."""
        case, audit = make_case(), AuditTrail()
        wf = CaseWorkflow(case, audit)
        wf.decide("petugas", Role.PETUGAS, Decision.LULUS, reason="S0 ok")
        stage_sebelum = case.current_stage
        wf.decide("petugas", Role.PETUGAS, Decision.TOLAK, reason="dokumen bercanggah")
        self.assertEqual(case.current_stage, stage_sebelum)

    def test_peranan_salah_disekat(self):
        """CHECK & BALANCE: pemohon tak boleh lulus pintu; mahkamah tak boleh lulus S1."""
        case, audit = make_case(), AuditTrail()
        wf = CaseWorkflow(case, audit)
        with self.assertRaises(WorkflowError):
            wf.decide("waris", Role.PEMOHON, Decision.LULUS, reason="nak cepat")
        with self.assertRaises(WorkflowError):
            wf.decide("mahkamah", Role.MAHKAMAH, Decision.LULUS)  # S0 bukan pintu mahkamah


class TestAuditChain(unittest.TestCase):
    def test_rantaian_sah(self):
        case, audit = make_case(), AuditTrail()
        wf = CaseWorkflow(case, audit)
        for actor, role in APPROVAL_SEQ[:5]:
            wf.decide(actor, role, Decision.LULUS, reason="uji")
        ok, rosak = audit.verify()
        self.assertTrue(ok)
        self.assertIsNone(rosak)

    def test_pengubahan_silam_dikesan(self):
        """TAMPER-EVIDENT: ubah rekod lama → verify() gagal pada rekod itu."""
        case, audit = make_case(), AuditTrail()
        wf = CaseWorkflow(case, audit)
        for actor, role in APPROVAL_SEQ[:4]:
            wf.decide(actor, role, Decision.LULUS, reason="asal")
        self.assertTrue(audit.verify()[0])
        audit.records[2]["payload"]["sebab"] = "DISABOTAJ"   # pengubahan silam
        ok, rosak = audit.verify()
        self.assertFalse(ok)
        self.assertIsNotNone(rosak)
        self.assertEqual(rosak["action"], "gate.LULUS")

    def test_rekomputasi_bebas(self):
        """Auditor: rekod yang sama menghasilkan hash yang sama (deterministik)."""
        case, audit = make_case(), AuditTrail()
        wf = CaseWorkflow(case, audit)
        wf.decide("petugas", Role.PETUGAS, Decision.LULUS, reason="rekod-1")
        snapshot = [dict(r) for r in audit.records]
        ok, _ = audit.verify()
        self.assertTrue(ok)
        self.assertEqual([r["hash"] for r in audit.records], [r["hash"] for r in snapshot])


class TestNorms(unittest.TestCase):
    def test_norma_terverifikasi_boleh_dipaksa(self):
        enforce(get_norm("N-PK-01"))   # tidak membangkitkan ralat
        enforce(get_norm("N-EX-01"))

    def test_norma_perlu_sahkan_disekat(self):
        """PERLU SAHKAN = DISEKAT daripada produksi (tiada tindakan tanpa rujukan sahih)."""
        with self.assertRaises(NormNotVerifiedError):
            enforce(get_norm("N-XX-TEST"))

    def test_norma_terpakai_pusaka_kecil_muslim(self):
        hasil = check_trigger("permohonan_pembahagian_pusaka_kecil_muslim")
        ids = [n["norm_id"] for n in hasil]
        self.assertIn("N-PK-01", ids)
        pk = next(n for n in hasil if n["norm_id"] == "N-PK-01")
        self.assertTrue(pk["enforceable"])
        self.assertEqual(pk["status"], NormStatus.TERVERIFIKASI.value)
        self.assertIn("s.50", pk["legal_basis"])

    def test_semua_norma_bawa_asas_statutori(self):
        for n in __import__("system.core.norms", fromlist=["NORM_LIBRARY"]).NORM_LIBRARY:
            self.assertTrue(n.legal_basis.strip(), f"{n.norm_id} tiada asas statutori")
            self.assertTrue(n.citation.strip(), f"{n.norm_id} tiada citation")


class TestRBAC(unittest.TestCase):
    def test_kebenaran_asas(self):
        self.assertTrue(can(Role.AUDITOR, "audit.read"))
        self.assertFalse(can(Role.AUDITOR, "gate.decide"))       # auditor baca-sahaja
        self.assertFalse(can(Role.PEMOHON, "gate.decide"))       # pemohon tak lulus pintu
        self.assertTrue(can(Role.PENYELIA, "norm.panel"))
        self.assertTrue(can(Role.ADMIN, "backup.run"))


class TestCaseModel(unittest.TestCase):
    def test_status_nilai_harta(self):
        Asset("A1", "Rumah teres", 450_000, "NILAI_RASMI")
        with self.assertRaises(ValueError):
            Asset("A2", "Kereta", 30_000, "NILAI_APA-APA")  # label tidak sah ditolak


if __name__ == "__main__":
    unittest.main(verbosity=2)
