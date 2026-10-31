---
title: Repo Ilmu — Pentadbiran Pusaka / Estate Administration Malaysia
version: 0.1 (skeleton)
updated: 2026-10-31
status: under-construction — 7 research agents berjalan
maintainer: Zizi (Hermes agent, profile estateadministration-project)
---

# 📚 Repo Ilmu: Pentadbiran Pusaka / Estate Administration (EA) Malaysia

Repo rujukan utama untuk projek **webapp/automation Pentadbiran Pusaka Malaysia** yang akan diuruskan oleh agent-agent bertindak sebagai legal advisor, syariah advisor, dan EA advisor ( kepakaran fiduciary Islamic & non-Islamic jurisdiction).

**Konteks asas projek:** Pentadbiran pusaka di Malaysia melibatkan dua bidang kuasa — civil (Mahkamah Tinggi, Pejabat Pusaka Kecil/JKPTG) dan syariah (JKSM, faraid) — dengan Amanahraya Berhad sebagai badan korporat kerajaan yang dilantik melaksanakan pentadbiran pusaka (fiduciary service). Semua fakta dalam repo ini mesti ada sumber — lihat konvensyen di bawah.

---

## 🗂️ Klasifikasi & Struktur Repo

| # | Folder | Kategori | Isi kandungan |
|---|--------|----------|---------------|
| 00 | `00-project/` | Dokumen projek | Jurnal penyelidikan & analisis (research problems → resolusi), pelan tindakan berfasa (3 fasa), notulasi semakan |
| 01 | `01-legal-framework/` | Undang-undang | Akta civil (Probat & Pentadbiran, Distribusi, Wills, Pusaka Kecil, ARB Act), undang-undang syariah (faraid, wasiat, hibah, sepencarian), bidang kuasa civil vs syariah (Art 121(1A) FC) |
| 02 | `02-institutions/` | Institusi | Amanahraya Berhad, Mahkamah Tinggi, Pejabat Pusaka Kecil (PPKP/JKPTG), JKSM, MdI, BPN (Wang Tak Dituntut), trustee companies berlesen |
| 03 | `03-processes/` | Proses & prosedur | Peta proses step-by-step: probat/LA, pusaka kecil, ARB, BPN, EPF/insurans/takaful, pemindahan tanah |
| 04 | `04-products/` | Produk EA | Islamic estate planning (wasiat, hibah, amanah/trust, waqf, harta sepencarian) & conventional (wills, testamentary trust, nominations) + matriks perbandingan |
| 05 | `05-statistics/` | Data & demografi | Nilai harta tak dituntut, backlog kes, kadar kematian, komposisi agama/penduduk, statistik pentadbiran |
| 06 | `06-case-studies/` | Kes rujukan | Kes mahkamah public-access (civil & syariah) + lessons learned & template prosedur |
| 07 | `07-limitations/` | Had & kekangan | Bottleneck (delay, frozen assets, dokumen, waris), kaedah penyelesaian yang direkodkan |
| 08 | `08-improvements/` | Penambahbaikan | Inisiatif digital, pindaan akta, cadangan reformasi, benchmark antarabangsa |
| 09 | `09-webapp-blueprint/` | Fasa 2 — webapp | Mapping ilmu → peranan agent (legal advisor, syariah advisor, EA advisor, process agent). Dibina selepas fasa research |

---

## 📐 Konvensyen Fail (WAJIB ikut)

1. **Bahasa:** Bahasa Malaysia formal utama + istilah legal English inline (contoh: "geran probat (grant of probate)"). Bahan rujukan civil/non-syariah dibenarkan dalam English sepenuhnya sebagai bahan rujukan.
2. **Frontmatter YAML:** `title`, `category`, `updated: YYYY-MM-DD`, `status: draft|verified`, `sources_count: N`.
3. **Sitasi:** setiap fakta/angka mesti ada `[Sumber: <tajuk/penerbit> — <URL>, dicapai 2026-10-31]`.
4. **Tiada fabrikasi:** fakta tanpa sumber ditanda `(PERLU SAHKAN)` atau dibuang. Jurang maklumat dicatat bawah `## Jurang maklumat (Gaps)`.
5. **Presisi:** nombor seksyen akta, nama akta, angka, tarikh — quote SEPERTI sumber.

---

## 🚧 Status Fasa 1 (Research) — berjalan 2026-10-31

| Stream | Agent | Fail target | Status |
|--------|-------|-------------|--------|
| 1. Undang-undang civil | research-1 | `01-legal-framework/civil-law.md` | 🔄 berjalan |
| 2. Undang-undang syariah + bidang kuasa | research-2 | `01-legal-framework/syariah-law.md`, `01-legal-framework/jurisdiction-civil-vs-syariah.md` | 🔄 berjalan |
| 3. Institusi + peta proses | research-3 | `02-institutions/*`, `03-processes/process-maps.md` | 🔄 berjalan |
| 4. Produk EA | research-4 | `04-products/*` | 🔄 berjalan |
| 5. Statistik + demografi | research-5 | `05-statistics/*` | 🔄 berjalan |
| 6. Kes rujukan | research-6 | `06-case-studies/*` | 🔄 berjalan |
| 7. Bottleneck + penyelesaian + penambahbaikan | research-7 | `07-limitations/*`, `08-improvements/*` | 🔄 berjalan |

Fasa seterusnya: verifikasi fakta, klasifikasi akhir, `09-webapp-blueprint/agent-roles.md`, skill `estate-administration-malaysia`.

---

## 📌 Kegunaan Repo

- Rujukan klasifikasi ilmu untuk **agent legal advisor** (jurisdiction, seksyen akta), **agent syariah advisor** (faraid, wasiat, hibah, fatwa), dan **agent EA advisor** (proses, produk, fiduciary, Islamic & non-Islamic).
- Asas template prosedur untuk penentuan proses kerja pentadbiran pusaka berasaskan case study.
- Sumber data untuk webapp feature (statistics, bottleneck mapping, improvement roadmap).
