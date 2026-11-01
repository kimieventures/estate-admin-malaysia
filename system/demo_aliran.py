"""Demo aliran kes EA-MY — modul asas (workflow stage-gate + audit + norma).

Jalankan:  python -m system.demo_aliran
"""
from system.core.audit import AuditTrail
from system.core.case import Asset, Case, Party, Stage
from system.core.norms import check_trigger, enforce, get_norm
from system.core.roles import Role
from system.core.workflow import CaseWorkflow, Decision


def main() -> None:
    print("=" * 72)
    print("DEMO ALIRAN KES EA-MY — MODEL PASANGAN AGENT-HUMAN (11 PINTU)")
    print("=" * 72)

    # ── S0: Intake ──
    case = Case(
        case_id="EA-2026-0042",
        deceased_name="Ahmad bin Ismail",
        religion="Islam",
        has_will=False,
        total_value=1_200_000,
    )
    case.add_asset(Asset("A1", "Rumah teres, Shah Alam", 450_000, "NILAI_RASMI"))
    case.add_asset(Asset("A2", "Simpanan KWSP", 230_000, "ANGGARAN"))
    case.add_party(Party("W1", "Salmah bte Omar", "balu"))
    case.add_party(Party("W2", "Muhammad Aiman", "anak lelaki"))
    case.add_party(Party("W3", "Nurul Aisyah", "anak perempuan"))

    audit = AuditTrail()
    wf = CaseWorkflow(case, audit)
    print(f"\n[Kes dibuka] {case.case_id} — {case.deceased_name}")
    print(f"  Agama: {case.religion} | Wasiat: {'ada' if case.has_will else 'tiada'} | Nilai: RM{case.total_value:,}")
    print(f"  Peringkat: {case.current_stage.name} — {case.stage_name()}")

    # ── S1: Klasifikasi — semakan norma pra-syarat (N-PK-01) ──
    print(f"\n[Agent A8 — semakan norma pra-syarat bagi {Stage.S1.name}]")
    for n in check_trigger("permohonan_pembahagian_pusaka_kecil_muslim"):
        penanda = "AKTIF " if n["enforceable"] else "DISEKAT"
        print(f"  {penanda} {n['norm_id']} ({n['modality']}) {n['action']} — {n['legal_basis']}")
    enforce(get_norm("N-PK-01"))
    print("  → N-PK-01 dipaksa: WAJIB sijil faraid SEBELUM pembahagian (s.50 Akta 505)")

    # ── Laluan pintu S0 → S10 ──
    langkah = [
        ("petugas", Role.PETUGAS, "identiti & dokumen asal disahkan"),
        ("petugas", Role.PETUGAS, "laluan PPKP disepakati (≤RM5j) + anggaran fi dipaparkan"),
        ("petugas", Role.PETUGAS, "dokumen 100% sahih (sijil kematian, MYKAD waris, geran rumah)"),
        ("ustaz-dr", Role.PAKAR_SYARIAH, "nasihat faraid disemak; sijil faraid diperoleh (RM30)"),
        ("ustaz-dr", Role.PAKAR_SYARIAH, "kiraan semak: balu 1/8, baki anak asabah — tiada bantahan"),
        ("penyelia", Role.PENYELIA, "sifar pelanggaran norma kritikal (6 norma lulus)"),
        ("peguam", Role.PEGUAM, "kertas kes + pelan agihan dilulus"),
        ("ppkp-putrajaya", Role.AGENSI, "KUASA LUARAN: perintah pembahagian diterbit selepas mesyuarat waris"),
        ("petugas", Role.PETUGAS, "pelaksanaan: Borang 14A diserahkan, KWSP oleh penama-wasi (audit agihan)"),
        ("mahkamah-syariah", Role.MAHKAMAH, "PENGESAHAN: lejar seimbang & rumusan disahkan"),
        ("petugas", Role.PETUGAS, "pakej penyampaian diterima pemohon — kes ditutup"),
    ]
    print("\n[Aliran pintu — pasangan berperanan]")
    for actor, role, sebab in langkah:
        wf.decide(actor, role, Decision.LULUS, reason=sebab)
        penanda = "SELESAI ✔" if case.closed else f"→ {case.current_stage.name}"
        print(f"  [{role.value:<15}] {sebab[:58]:<58} {penanda}")

    # ── Audit ──
    ok, rosak = audit.verify()
    print(f"\n[Audit hash-chain] Rantaian sah: {'YA' if ok else 'TIDAK'} | Rekod: {len(audit.records)}")
    for baris in audit.export_lines():
        print("  " + baris)
    print(f"\n  Rantaian: {' → '.join(audit.chain())}")
    print(f"\n[Keputusan] Kes {case.case_id}: {'DITUTUP' if case.closed else 'BERJALAN'} pada {case.stage_name()}")
    print("=" * 72)


if __name__ == "__main__":
    main()
