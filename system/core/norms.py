"""Perpustakaan Norma (deontik) — WAJIB / DIBENAR / DILARANG.

Prinsip (modul-pematuhan-enjin-fi.md §A, journal §6.3):
- Norma hanya aktif dalam produksi jika status TERVERIFIKASI.
- Item PERLU SAHKAN DISEKAT (enforce() membangkitkan ralat).
- Setiap norma membawa asas statutori + citation repo.
"""
from dataclasses import dataclass
from enum import Enum


class Modality(str, Enum):
    WAJIB = "WAJIB"
    DIBENAR = "DIBENAR"
    DILARANG = "DILARANG"


class NormStatus(str, Enum):
    TERVERIFIKASI = "TERVERIFIKASI"
    PERLU_SAHKAN = "PERLU_SAHKAN"


class NormNotVerifiedError(Exception):
    """Norma belum disahkan — DISEKAT daripada produksi."""


@dataclass(frozen=True)
class Norm:
    norm_id: str
    domain: str
    modality: Modality
    trigger: str            # keadaan/pencetus norma
    action: str             # tindakan yang dinormakan
    order: str              # SEBELUM / SEMASA / SELEPAS
    legal_basis: str        # akta/seksyen/peraturan
    citation: str           # fail repo / URL
    status: NormStatus


# ── 6 norma terverifikasi (journal-research-report.md v2.1 §6.3) ──
# ── + 1 norma contoh PERLU SAHKAN (untuk ujian mekanisme sekatan) ──
NORM_LIBRARY: list[Norm] = [
    Norm("N-PK-01", "pusaka_kecil", Modality.WAJIB,
         "permohonan_pembahagian_pusaka_kecil_muslim", "dapatkan_sijil_faraid", "SEBELUM",
         "s.50 Akta 505 + amalan PPKP",
         "[rujuk: 03-processes/process-maps.md; 01-legal-framework/syariah-law.md]",
         NormStatus.TERVERIFIKASI),
    Norm("N-W-01", "wasiat_islam", Modality.DILARANG,
         "wasiat_muslim_beri_manfaat", "melebihi_satu_tiga_harta_bersih_tanpa_persetujuan_waris", "SEMASA",
         "had 1/3 + Enakmen Wasiat Orang Islam (Selangor) 1999 s.26",
         "[rujuk: 01-legal-framework/syariah-law.md; research-faraid-berlapis.md]",
         NormStatus.TERVERIFIKASI),
    Norm("N-PA-01", "probat", Modality.WAJIB,
         "pengambilan_harta_melebihi_had_agensi", "dapatkan_geran_probat_skm", "SEBELUM",
         "Probate and Administration Act 1959 [Act 97]",
         "[rujuk: 01-legal-framework/civil-law.md]",
         NormStatus.TERVERIFIKASI),
    Norm("N-EX-01", "pentadbiran", Modality.DILARANG,
         "pembahagian_harta", "sebelum_hutang_dan_perbelanjaan_dilangsaikan", "SEBELUM",
         "urutan piawai pentadbiran",
         "[rujuk: 01-legal-framework/civil-law.md]",
         NormStatus.TERVERIFIKASI),
    Norm("N-WC-01", "wasiat_civil", Modality.WAJIB,
         "wasiat_civil_dilaksanakan", "verifikasi_formaliti_s5_dua_saksi_serentak", "SEBELUM",
         "Wills Act 1959 s.5 (Semenanjung; tidak terpakai kepada Muslim s.2(2))",
         "[rujuk: 01-legal-framework/gap-mission-undang-undang.md Misi 2]",
         NormStatus.TERVERIFIKASI),
    Norm("N-PP-01", "pusaka_kecil", Modality.WAJIB,
         "perintah_pembahagian_pusaka_kecil", "mesyuarat_waris_dihadiri", "SEBELUM",
         "proses Akta 98 (Borang A)",
         "[rujuk: 03-processes/process-maps.md]",
         NormStatus.TERVERIFIKASI),
    # Contoh norma belum disahkan — kekal DISEKAT; jangan buang (dokumentasi jurang)
    Norm("N-XX-TEST", "test", Modality.WAJIB,
         "trigger_contoh", "tindakan_contoh", "SEBELUM",
         "asas belum disahkan",
         "[contoh untuk ujian sekatan produksi]",
         NormStatus.PERLU_SAHKAN),
]


def get_norm(norm_id: str) -> Norm:
    for n in NORM_LIBRARY:
        if n.norm_id == norm_id:
            return n
    raise KeyError(f"Norma {norm_id} tidak wujud dalam Perpustakaan")


def applicable(trigger: str) -> list[Norm]:
    """Norma yang terpakai bagi sesuatu pencetus (kebolehterpakaian sebagai fungsi data)."""
    return [n for n in NORM_LIBRARY if n.trigger == trigger]


def enforce(norm: Norm) -> None:
    """Penguatkuasaan produksi: hanya norma TERVERIFIKASI boleh dipaksa.

    Norma PERLU SAHKAN membangkitkan NormNotVerifiedError — by design
    (tiada tindakan tanpa rujukan sahih).
    """
    if norm.status is not NormStatus.TERVERIFIKASI:
        raise NormNotVerifiedError(
            f"{norm.norm_id} berstatus {norm.status.value} — DISEKAT daripada produksi "
            f"(asas: {norm.legal_basis})"
        )


def check_trigger(trigger: str) -> list[dict]:
    """Senarai norma terpakai + status penguatkuasaan (untuk pintu S5 / A8)."""
    return [
        {
            "norm_id": n.norm_id,
            "modality": n.modality.value,
            "action": n.action,
            "order": n.order,
            "legal_basis": n.legal_basis,
            "status": n.status.value,
            "enforceable": n.status is NormStatus.TERVERIFIKASI,
        }
        for n in applicable(trigger)
    ]
