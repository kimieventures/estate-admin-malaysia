"""Model Kes (Case) & Kitaran Hidup 11 Peringkat — konsep-model-agent-human.md."""
from dataclasses import dataclass, field
from enum import Enum


class Stage(int, Enum):
    """11 peringkat kitaran hidup kes (S0-S10) — model pasangan agent-human."""
    S0 = 0   # Pendaftaran & Intake
    S1 = 1   # Verifikasi & Klasifikasi
    S2 = 2   # Pengumpulan & Pengesahan Dokumen
    S3 = 3   # Analisis Kes & Nasihat
    S4 = 4   # Pengiraan Bahagian
    S5 = 5   # Semakan Norma & Pematuhan
    S6 = 6   # Kertas Kes & Draf Keputusan
    S7 = 7   # Serahan & Pengesahan Agensi/Mahkamah
    S8 = 8   # Pelaksanaan & Pemantauan
    S9 = 9   # Laporan Akhir & Rumusan Kes
    S10 = 10  # Penyampaian & Penutupan


STAGE_NAMES = {
    Stage.S0: "Pendaftaran & Intake",
    Stage.S1: "Verifikasi & Klasifikasi",
    Stage.S2: "Pengumpulan & Pengesahan Dokumen",
    Stage.S3: "Analisis Kes & Nasihat",
    Stage.S4: "Pengiraan Bahagian",
    Stage.S5: "Semakan Norma & Pematuhan",
    Stage.S6: "Kertas Kes & Draf Keputusan",
    Stage.S7: "Serahan & Pengesahan Agensi/Mahkamah",
    Stage.S8: "Pelaksanaan & Pemantauan",
    Stage.S9: "Laporan Akhir & Rumusan Kes",
    Stage.S10: "Penyampaian & Penutupan",
}

# Nilai status harta — modul-pematuhan-enjin-fi.md §B5
VALUE_STATUS = ("NILAI_RASMI", "ANGGARAN", "TERJUAL")


@dataclass
class Asset:
    """Aset pusaka dengan nilai berlabel (satu sumber nilai antara modul fi & agihan)."""
    asset_id: str
    description: str
    value: float
    value_status: str = "ANGGARAN"  # VALUE_STATUS

    def __post_init__(self):
        if self.value_status not in VALUE_STATUS:
            raise ValueError(f"value_status mesti salah satu daripada {VALUE_STATUS}")


@dataclass
class Party:
    """Pihak berkaitan kes (waris, penama, pasangan)."""
    party_id: str
    name: str
    relation: str


@dataclass
class Case:
    """Kes pusaka — fail tunggal (jawab RP-06: tiada silos)."""
    case_id: str
    deceased_name: str
    religion: str          # "Islam" | "BukanIslam"
    has_will: bool
    total_value: float
    current_stage: Stage = Stage.S0
    closed: bool = False
    assets: list = field(default_factory=list)
    parties: list = field(default_factory=list)

    def stage_name(self) -> str:
        return STAGE_NAMES[self.current_stage]

    def add_asset(self, asset: Asset) -> None:
        self.assets.append(asset)

    def add_party(self, party: Party) -> None:
        self.parties.append(party)
