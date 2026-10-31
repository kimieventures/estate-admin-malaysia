---
title: "Jurnal Penyelidikan & Analisis — Pentadbiran Pusaka di Malaysia: Ilmu, Research Problems dan Resolusi Melalui Sistem Automasi Pakar Berasaskan Agent"
project: EA-MY (Estate Administration Malaysia)
version: 2.0 (sintesis penuh Fasa 2 — menunggu semakan pemilik projek)
updated: 2026-10-31
status: review-pending (untuk semakan Kimie sebelum go/no-go Fasa 3)
bahasa: Bahasa Malaysia (formal); rujukan civil/common law dalam English dibenarkan
authors: Zizi (Hermes agent, profile estateadministration-project) bersama Kimie (pemilik projek)
asas: Fasa 1 — 22 fail ilmu, 839 sitasi inline, 7/7 stream research selesai
---

# Jurnal Penyelidikan & Analisis — Pentadbiran Pusaka di Malaysia (v2.0)

## Ringkasan Eksekutif (untuk semakan pemilik projek)

1. **Ilmu asas lengkap & bercitation.** 22 fail merentas 9 domain (undang-undang civil/syariah, bidang kuasa, institusi, 7 peta proses, produk, statistik, kes rujukan + Templat A–F, kekangan, penambahbaikan) — 839 sitasi, setiap fakta boleh dikesan. Contoh nilai verifikasi: rujukan popular "Amanah Raya Berhad Act 2001 (Act 682)" terbukti **salah** — statut sebenar ARB ialah **Public Trust Corporation Act 1995 [Act 532]**; Act 682 = Akta Universiti Malaya 1961 [rujuk: `02-institutions/amanahraya-berhad.md`].
2. **Masalah utama Malaysia teruk dan terdokumen:** hanya **~5%** rakyat ada perancangan pewarisan (ARB, Feb 2025); **RM13.3 bilion** wang tak dituntut di BPN (Apr 2025); backlog pusaka kecil **46,707 kes** (31 Dis 2025) walaupun 84,384 kes/RM19.01 bilion selesai pada 2025; kes selesai 2025 hanya ≈ **42%** daripada ~199,000 kematian setahun.
3. **Dwi-jurisdiction ialah punca kerumitan No. 1:** mesinari probat kekal civil/federal (Senarai Persekutuan 4(e)(i)) manakala kandungan hukum pusaka Islam di bidang negeri — model "twin-track" disahkan dalam kes *Latifah* [2007]. Sijil faraid (s.50 Akta 505) wajib untuk Muslim tetapi **perintah syariah tidak boleh didaftarkan** di pejabat tanah — geran sivil tetap diperlukan (Surat Edaran KPTG / Bar Circular 077/2026).
4. **Laluan pentadbiran kini jelas:** pusaka ringkas harta alih ≤RM600,000 (ARB, s.17(1) Act 532) → pusaka kecil ≤RM5 juta (PPKP/JKPTG, Act A1643 berkuat kuasa 15 Julai 2024) → Mahkamah Tinggi (>RM5 juta, Act 97). Tempoh: 4–6 bulan (pusaka kecil), 3–6 bulan (probat tanpa pertikaian).
5. **8 research problems (RP-01→RP-08) disahkan bukti** dengan skor keyakyinan (matriks penuh: `00-project/rp-bukti-matriks.md`): RP-01 (harta tertunggak) dan RP-03 (dwi-jurisdiction) KUAT; RP-02 (kelewatan) KUAT untuk angka backlog; beberapa angka "harta beku RM60–90 bilion" **dipertikaikan kerajaan** — digunakan dengan caveat.
6. **Penyelesaian dicadangkan:** platform webapp + 8 agent pakar (A1 legal, A2 syariah, A3 fiduciary, A4 analisis kes, A5 enjin kiraan faraid/hibah/wasiat deterministik, A6 orkestrator pelaksana arahan, A7 dokumen, A8 pematuhan deontik) dengan Perpustakaan Norma (WAJIB/DIBENAR/DILARANG) dan human-in-the-loop di semua titik keputusan. Prototype visual "Opis EA-MY" sedia (`09-webapp-blueprint/agent-ops-dashboard.html`).
7. **Benchmark membuktikan penyelesaian mungkin:** Singapura Probate eService (2023, ≤S$2 juta, tanpa peguam) dan UK MyHMCTS (probat digital wajib, geran 48 jam) — Malaysia masih TIADA e-Probate awam; sistem sedia ada (MyLAND, e-Syariah V3) belum berintegrasi hujung-ke-hujung.
8. **Keputusan yang perlu anda tetapkan selepas review:** go/no-go Fasa 3, keutamaan modul MVP, pemosisian (awam vs profesional), skop geografi (Semenanjung dulu), dan pendekatan semakan pakar (rujuk Seksyen 9).

---

## 1. Abstrak & Kaedah Kajian

Dokumen ini ialah **jurnal penyelidikan induk** projek EA-MY: (i) memetakan ilmu pentadbiran pusaka (Estate Administration, EA) di Malaysia — undang-undang dwi-jurisdiction civil–syariah, institusi, proses, produk, statistik, kes rujukan dan kekangan; (ii) membentuk **pernyataan masalah penyelidikan (RP-01→RP-08)** berdasarkan bukti; dan (iii) mengemukakan **konsep resolusi** — platform webapp dan kumpulan agent pakar (agentic AI) sebagai expert advisory (penasihat legal/syariah seperti peguam) dan pegawai pentadbir yang mengurus serta melaksanakan arahan mahkamah syariah/civil, diautomasi menerusi **logik deontik** dan enjin pengiraan bahagian faraid/hibah/wasiat/intestate yang deterministik.

**Kaedah:** 7 stream research selari (subagent) dengan kawalan citation wajib; setiap fakta membawa sitasi `[Sumber: — URL, dicapai]`; fakta tidak sah ditanda `PERLU SAHKAN`; jurang direkod dalam seksyen Gaps setiap fail + daftar jurang pusat (`00-project/fasa1-stream-summaries.md`). Verifikasi silang dilakukan semasa sintesis (contoh: pembetulan Akta 532 vs 682 disahkan oleh 2 stream bebas dengan PDF rasmi UM).

**Had kaedah:** sumber awam sahaja (tiada akses pangkalan MLJ/CLJ berlangganan); keputusan mahkamah syariah jarang diterbitkan terbuka; peta proses terhad kepada Semenanjung (Sabah/Sarawak dalam misi jurang Fasa 2); statistik probat Mahkamah Tinggi tidak diterbitkan sebagai siri tahunan.

---

## 2. Latar Belakang & Konteks (terverifikasi Fasa 1)

### 2.1 Pentadbiran pusaka sebagai perkhidmatan fiduciary
Estate administration ialah perkhidmatan **fiduciary**: pentadbir pusaka (administrator) / pelaksana wasiat (executor) bertindak dalam kedudukan amanah untuk mengesan, mengumpul dan mengurus harta si mati; melangsaikan hutang serta perbelanjaan pentadbiran; kemudian membahagikan baki harta kepada waris/benefisiari yang berhak selaras dengan undang-undang, wasiat dan arahan mahkamah/agensi berautoriti. Kegagalan tugas fiduciary boleh membawa pertikaian dan tindakan mahkamah — contoh kes dicatatkan dalam `06-case-studies/civil-cases.md` (kategori pentadbir cuai/breach of trust).

### 2.2 Struktur dwi-jurisdiction (asas perlembagaan terverifikasi)

- **Senarai Persekutuan item 4(e)(i):** Parlimen berkuasa atas "probate and letters of administration"; perenggan (ii) mengecualikan undang-undang peribadi Islam → **mesinari probat kekal civil/federal**.
- **Senarai Negeri item 1 (Jadual Kesembilan):** pewarisan/wasiat/hibah orang Islam di bidang negeri → **kandungan hukum kekal syariah/negeri**.
- **Perkara 121(1A)** (kuat kuasa 10 Jun 1988): mahkamah sivil tiada bidang kuasa atas perkara dalam bidang kuasa mahkamah syariah; namun mahkamah sivil menentukan sempadannya sendiri — *Indira Gandhi* [2018] dan *SIS* [2022] mengekalkan judicial review pada Mahkamah Tinggi Sivil [rujuk: `01-legal-framework/jurisdiction-civil-vs-syariah.md`].
- **Kes *Latifah Mat Zin v Rosmawati* [2007] (Mahkamah Agung/FC):** penentuan hibah ialah isu undang-undang Islam untuk Mahkamah Syariah dan mahkamah sivil "shall give effect" kepadanya dalam geran dan pengagihan — **model dua-laluan (twin-track)** yang menjadi asas koordinasi amalan.

### 2.3 Laluan pentadbiran pusaka (had & asas terverifikasi)

| Situasi | Laluan | Asas undang-undang |
|---|---|---|
| Harta alih ≤RM600,000 | Pusaka ringkas — Amanahraya Berhad | s.17(1) PTCA 1995 [Act 532] |
| Harta (alih/tak alih/gabungan) ≤RM5 juta | Pusaka kecil — PPKP/JKPTG (Borang A, mesyuarat waris) | Akta 98 + Act A1643 (kuat kuasa 15 Julai 2024); fi P.U.(A) 194/2024 |
| >RM5 juta / berwasiat kompleks | Geran probat/SKM — Mahkamah Tinggi | Probate & Administration Act 1959 [Act 97]; Order 71/72 KM 2012 |
| Penetapan waris & kadar faraid Muslim | Sijil faraid — Mahkamah Syariah | s.46(2)(b) & s.50 Akta 505 |
| Tuntutan harta sepencarian (Islam) | Mahkamah Syariah (termasuk selepas kematian) | Akta 303 s.122; Arahan Amalan JKSM No. 5/2003 |

[rujuk: `03-processes/process-maps.md` untuk 7 peta proses penuh dengan langkah/dokumen/yuran/tempoh]

### 2.4 Amanahraya Berhad — pembetulan penting
ARB diperbadankan **1995** di bawah **Public Trust Corporation Act 1995 [Act 532]** (kuat kuasa 1 Ogos 1995) — BUKAN "Act 682 2001" (Akta 682 ialah University of Malaya Act 1961). Pemilikan: 99.99% Menteri Kewangan (Terperbadanan) + 0.01% Pesuruhjaya Tanah Persekutuan. Kuasa fidusiari: s.11–12 (pemegang amanah/wasi), s.13 (geran), s.16 (penguasaan harta intestat), s.17(1) (pusaka ringkas ≤RM600k), s.33 (fi). Statistik: 230,000+ kes pusaka & 155,000+ pentadbiran >RM16.7 bilion. Fi pentadbiran 5%→1% berperingkat (sumber pegawai ARB; PERLU SAHKAN jadual rasmi). [rujuk: `02-institutions/amanahraya-berhad.md`]

### 2.5 Kenapa projek ini
Angka-angka di Ringkasan Eksekutif menunjukkan sistem sedia ada tertunggak dan sukar diakses orang awam; laluan penyelesaian digital (benchmark SG/UK) belum wujud di Malaysia; dan kepakaran fiduciary terhad. Research problems (Seksyen 4) memformalkan masalah ini; Seksyen 6 mencadangkan resolusi.

---

## 3. Peta Ilmu & Keputusan Utama Setiap Domain

| Domain | Fail | Keputusan utama (dengan pointer) |
|---|---|---|
| Undang-undang civil | `01-legal-framework/civil-law.md` | Act 97 (geran, komisen pentadbir maks 5% s.43(1), bon >RM50k), Act 300 (intestate bukan Islam; tidak terpakai kepada Muslim s.1(2)), Act 346 (wasiat), Act 98 + A1643 (pusaka kecil RM5j), Act 532 (ARB), NLC 1965, FSA 2013 (Jadual 10), Akta KWSP 1991 |
| Undang-undang syariah | `syariah-law.md` | Faraid 12 ashab al-furud (1/2–1/6, Al-Nisa' 11/12/176) + asabah + 'aul/radd; wasiat ≤1/3 harta bersih & tidak kepada waris tanpa persetujuan; hibah inter vivos; sepencarian s.122 Akta 303; penama Muslim = wasi (Fatwa MKI 1978/2000) |
| Bidang kuasa | `jurisdiction-civil-vs-syariah.md` | Twin-track Latifah; s.50 Akta 505; konflik didokumenkan (Moorthy, MAIWP v Lim Ee Seng, Re Timah); SIS 2022 |
| Institusi | `02-institutions/` | ARB (Act 532); Mahkamah Tinggi (Order 71/72, e-Filing peguam sahaja); PPKP/JKPTG (MyLAND, had RM5j); JKSM (e-Syariah V3, kecuali Sarawak); MdI (s.5(4) Enakmen Selangor); BPN (WTD RM13.3b, eGUMIS) |
| Peta proses | `03-processes/process-maps.md` | 7 laluan lengkap: probat/SKM (3–6 bulan; peguam RM2k–5k); pusaka kecil (fi RM30/RM50/0.2–0.3%; 4–6 bulan); ARB; WTD (UMA-7, tiada caj, tiada had masa); KWSP (RM2,500 s.58(1)); tanah (NLC s.346, Borang 14A); syer (s.109 Companies Act 2016) |
| Produk | `04-products/` | Wasiat RM298–RM30,000 (Maybank/Rockwills/MAIS/ARB); HiBAHKU (RM1,500+RM500); Pewarisan Bertakaful (RM10/bln); hibah amanah (TH/ASNB); trust policy FSA hanya bukan Islam; tiada "MyEstate" — portfolio sebenar disahkan |
| Statistik | `05-statistics/` | WTD RM9.4b(2021)→RM13.3b(2025); backlog 72,348(2021)→46,707(2025), sasaran sifar 2028; wasiat ~5% (ARB 2025) vs 37% (Sun Life 2026 — definisi beza); kematian 198,992 (2024); Islam 63.5%; 65+ 8.0% |
| Kes rujukan | `06-case-studies/` | Kes civil (Savatery 2023 — suspicious circumstances; Divyyaa Machap [2024] — penama KWSP terkini menang; How Yew Hock 1996) + syariah (Nyonya Tahir — status agama; wasiat >1/3 — Sabri) + **Templat A–F** prosedur |
| Kekangan | `07-limitations/` | Tempoh terdokumen; sijil faraid tak boleh daftar tanah; waris hilang (s.108 Akta Bukti — 7 tahun; s.18 JPN tiada sijil tanpa mayat); kos; kejahilan 70% & bertangguh 43.3% (UiTM) |
| Penambahbaikan | `08-improvements/` | MyeTaPP→MyLAND; e-Syariah V3; TIADA e-Probate awam; benchmark SG/UK; cadangan roadmap berkeutamaan |

---

## 4. Research Problems dengan Bukti (skor keyakyinan)

> Matriks penuh dengan senarai bukti setiap per item: `00-project/rp-bukti-matriks.md` (Fasa 2). Skor di bawah ringkasan sintesis.

### RP-01 — Harta pusaka tertunggak tidak dituntut (dead capital) — **KUAT**
**Bukti:** WTD BPN RM13.3 bilion (Apr 2025, ~70% akaun bank tidak aktif ≥7 tahun; hanya RM4b dituntut sejak 1977) — rasmi; KWSP pengeluaran kematian RM1.52b (2020) — rasmi; harta beku RM65b (ARB, Feb 2025, separuh-rasmi) hingga RM90b (media) — **dipertikaikan** (MAMPU 2015, JKPTG 2022 ~RM13.7b); hanya ~5% ada perancangan (ARB 2025); jurang pemprosesan ≈58% (Seksyen 5.3). **Jurang:** tiada angka rasmi tunggal nilai harta beku.

### RP-02 — Tempoh pentadbiran panjang & proses kompleks — **KUAT (angka backlog) / SEDERHANA (purata tempoh)**
**Bukti:** backlog JKPTG 46,707 kes (Hansard/Bernama 29 Jan 2026); 84,384 kes selesai 2025; tempoh standard 4 bulan (Parlimen Jan 2026) vs 4–6 bulan (FAQ JKPTG) vs min 5½ bulan Borang A (artikel JKPTG); probat 3–6 bulan, SKM 6–9 bulan (firma guaman). **Jurang:** tiada median rasmi per pejabat; backlog probat Mahkamah Tinggi tidak diterbitkan.

### RP-03 — Kerumitan dwi-jurisdiction — **KUAT**
**Bukti:** struktur perlembagaan + twin-track Latifah [2007]; s.50 Akta 505; sijil faraid diperlukan PPKP (checklist JBG); **perintah syariah BUKAN instrumen pendaftaran tanah** (Surat Edaran KPTG, Bar Circular 077/2026) — waris Islam melalui DUA saluran; kes konflik (Moorthy [2006] — tiada forum; MAIWP v Lim Ee Seng [2000]). **Jurang:** tiada statistik kes pertindihan; tiada protokol rujuk-balik bertulis.

### RP-04 — Akses kepakaran terhad & kos tinggi — **SEDERHANA**
**Bukti:** yuran peguam RM2,000–5,000 (pusaka kecil) / RM4,000+ (mahkamah); fi pentadbir 5% (s.43(1) Act 97) & ARB 5%→1% (PERLU SAHKAN rasmi); fi wasiat RM298–RM30,000; bantuan guaman JBG RM10 (akses rendah); kejahilan 70% punca utama (UiTM Sarawak). **Jurang:** tiada kajian rasmi jurang akses demografi.

### RP-05 — Pengiraan bahagian ralat & tak berstandard — **SEDERHANA→KUAT (kaedah) / LEMAH (bukti ralat)**
**Bukti:** kaedah faraid (12 ashab al-furud, asabah, 'aul/radd) & skema Act 300 didokumenkan penuh; kalkulator faraid JKPTG wujud (MyLAND) tapi terpisah daripada proses permohonan; kes Divyyaa Machap [2024] menunjukkan kompleksiti penamaan yang mengelirukan. **Jurang:** tiada statistik ralat pengiraan; tiada enjin piawai bersepadu (ini yang Fasa 3 bina).

### RP-06 — Data silos antara agensi — **KUAT**
**Bukti:** sistem berasingan (MyLAND vs e-Syariah V3 vs e-Filing mahkamah vs eGUMIS vs bank/KWSP); waris kena bawa dokumen sama berulang (proses PPKP); tiada status kes tunggal; sijil faraid fizikal dihantar antara agensi. **Jurang:** statistik penggunaan sistem digital tidak diterbitkan.

### RP-07 — Waris hilang & dokumen hilang — **KUAT (mekanisme) / LEMAH (frekuensi)**
**Bukti:** anggapan kematian 7 tahun (s.108 Akta Bukti 1950); JPN tidak keluarkan sijil tanpa mayat (s.18 Akta Pendaftaran Kelahiran & Kematian 1957) — perlu deklarasi Mahkamah Tinggi; perbezaan tempoh menunggu civil vs syariah dikenal pasti sebagai kelewatan. **Jurang:** tiada statistik kes waris hilang.

### RP-08 — Ilmu kes tidak berstruktur — **KUAT**
**Bukti:** keputusan syariah "jarang diterbitkan terbuka" (semua stream 6 mengesahkan); kepakaran preseden tersebar; kami sendiri terpaksa bina Templat A–F dari kes terpilih. Deliverable Templat A–F (`06-case-studies/lessons-and-templates.md`) ialah bukti bahawa template boleh diekstrak — asas modul case reasoning A4.

---

## 5. Analisis Masalah

### 5.1 Analisis punca (kategori → data)

| Kategori | Punca (dengan bukti) | RP |
|---|---|---|
| Rangka undang-undang & bidang kuasa | Twin-track civil-syariah; sijil faraid + geran sivil; perintah syariah tak boleh daftar tanah | RP-03, RP-05 |
| Proses & prosedur | 7 laluan berasingan; borang & mesyuarat waris; min 5½ bulan Borang A | RP-02, RP-06, RP-07 |
| Manusia & kesedaran | ~95% tanpa perancangan; kejahilan 70%; bertangguh 43.3% | RP-01, RP-04 |
| Teknologi & data | Sistem digital berasingan; tiada e-Probate awam; tiada status kes tunggal | RP-02, RP-06, RP-08 |
| Ekonomi & akses | Fi pentadbir/peguam; probat Mahkamah Tinggi hanya melalui e-Filing peguam | RP-04 |

### 5.2 Analisis pihak berkepentingan (stakeholder matrix)

| Pihak | Kepentingan | Masalah dihadapi | Keperluan daripada penyelesaian |
|---|---|---|---|
| Waris & benefisiari | Terima bahagian segera & adil | Tak faham proses; harta beku; kos | Panduan jelas, jangkaan masa, pengiraan telus |
| Pentadbir pusaka (individu/ARB/MdI) | Laksana tugas fiduciary dengan betul | Beban tugas kompleks, risiko liabiliti | SOP, checklist, audit trail |
| Mahkamah Tinggi & Mahkamah Syariah/JKSM | Kesahan & kecekapan proses | Backlog; dokumen tak lengkap | Permohonan lengkap & tepat kali pertama |
| PPKP/JKPTG | Pembahagian pusaka kecil cekap | Backlog; mesyuarat waris lambat; sijil faraid lewat | Persediaan kes berstruktur |
| BPN / Jabatan Akauntan Negara | Keluarkan wang tak dituntut | Tuntutan tak dibuat; dokumen tak lengkap | Senarai semak tuntutan standard |
| Peguam & penulis wasiat | Beri khidmat profesional | Kerja berulang, margin masa | Sokongan penyediaan dokumen & kajian kes |
| Bank, EPF, insurans/takaful | Patuh proses si mati | Akaun beku tanpa pentadbir; pertikaian penama | Pengesahan waris/pentadbir yang jelas |

### 5.3 Rantai punca–kesan dikuantifikasi

```
~199,000 kematian setahun (DOSM 2024: 198,992)
   ↓ hanya ~42% diproses melalui pusaka kecil (84,384 kes selesai 2025)
~115,000 kematian/tahun TIDAK melalui pentadbiran formal pusaka kecil
   (sebahagian melalui Mahkamah Tinggi/ARB — tiada siri statistik; sebahagian besar kemungkinan terbiar)
   ↓
Harta beku: WTD RM13.3b (berkembang ~RM1b setahun) · harta beku RM65–90b (dipertikaikan)
   ↓
Backlog 46,707 kes · tempoh 4–6 bulan (lurus) hingga 2 tahun (kompleks)
```

**Kesimpulan analisis:** masalah bukan satu titik tetapi satu **rantai** — kesedaran → perancangan → proses → data. Penyelesaian yang hanya menyerang satu titik (cth. kalkulator faraid sahaja) tidak akan memutus rantai. Itu sebabnya konsep resolusi (Seksyen 6) merangkumi kesemua lapisan.

### 5.4 Bukti bahawa penyelesaian mungkin
- **Singapura:** Probate eService (12 April 2023) — permohonan geran probat online penuh tanpa peguam bagi pusaka ≤S$2 juta (MyInfo/ICA pra-isi).
- **UK:** probat digital wajib via MyHMCTS (sejak 2020/2021; fi £526; geran dalam 48 jam bagi kes lurus).
- **Malaysia sendiri:** MyLAND (permohonan online + ePayment + kalkulator faraid), e-Syariah V3 — komponen wujud, tetapi **belum berintegrasi hujung-ke-hujung dan belum sampai kepada probat awam**. [rujuk: `07-limitations/solutions-and-reforms.md`]

---

## 6. Konsep Resolusi (Fasa 3) — kini berasaskan data

### 6.1 Prinsip reka bentuk (kekal)
P1 Grounded (semua nasihat bercitation daripada repo); P2 autoriti manusia & agensi (keputusan muktamad mahkamah/agensi; agent = advisory + sokongan pelaksanaan); P3 BM formal; P4 auditability (setiap cadangan boleh dikesan ke norma/sumber); P5 berfasa.

### 6.2 Kumpulan agent (A1–A8) — asas ilmu kini LENGKAP

| ID | Agent | Peranan (analogi) | Ilmu rujukan (fail sedia) | Had kuasa |
|---|---|---|---|---|
| A1 | Penasihat Legal (civil) | Peguam civil | civil-law.md, jurisdiction-civil-vs-syariah.md, process-maps.md | Nasihat bercitation; tak wakil mahkamah |
| A2 | Penasihat Syariah | Penasihat syariah | syariah-law.md, kes syariah, fatwa dalam fail | Pentauliahan keputusan pada mahkamah syariah |
| A3 | EA/Fiduciary Advisor | Pegawai pentadbir profesional | amanahraya-berhad.md, courts-and-offices.md, 04-products/ | Cadangan produk/prosedur fiduciary |
| A4 | Analis Kes (RAG) | Peguam penyelidik preseden | 06-case-studies/ (3 fail) + Templat A–F | Bukan jaminan hasil |
| A5 | Enjin Kiraan | Kalkulator pakar | kaedah faraid (12 waris, 'aul/radd), Act 300, wasiat 1/3, sepencarian s.122 | Deterministik, bukan LLM bebas |
| A6 | Orkestrator Proses | Pegawai pentadbir pelaksana arahan | process-maps.md (7 laluan) | Manusia tandatangani & serah |
| A7 | Dokumen | Kerani pentadbiran | borang & checklist dalam process-maps | Draf untuk semakan manusia |
| A8 | Pematuhan Deontik | Auditor pematuhan | Perpustakaan Norma (6.3) | Tandakan pelanggaran WAJIB/DILARANG |

### 6.3 Logik deontik & Perpustakaan Norma
Operator: `WAJIB(p)`, `DIBENAR(p)`, `DILARANG(p) ≡ WAJIB(¬p)`, norma bersyarat `WAJIB(p|q)`, contrary-to-duty (pelanggaran mengaktifkan norma gantian, cth. dokumen hilang → WAJIB dapatkan salinan rasmi). Evaluator deterministik + pengesan konflik (`WAJIB(p) ∧ WAJIB(¬p)` diselesaikan mengikut keutamaan sumber: undang-undang > peraturan mahkamah > amalan agensi) + audit trail. Norma hanya sah dengan citation; norma belum disahkan kekal `PERLU SAHKAN` dan disekat daripada modul pengeluaran.

**Norma awal — status verifikasi semasa:**

| ID | Norma | Status |
|---|---|---|
| N-PK-01 | WAJIB sijil faraid sebelum pembahagian pusaka kecil Muslim (s.50 Akta 505 + amalan PPKP) | ✅ terverifikasi |
| N-W-01 | DILARANG wasiat Muslim memberi manfaat >1/3 harta bersih tanpa persetujuan waris | ✅ terverifikasi |
| N-PA-01 | WAJIB geran probat/SKM sebelum pengambilan harta melebihi had agensi (Act 97) | ✅ terverifikasi |
| N-EX-01 | DILARANG pentadbir membahagikan harta sebelum hutang & perbelanjaan pentadbiran dilangsaikan | ✅ terverifikasi (urutan piawai) |
| N-WC-01 | WAJIB wasiat civil ditandatangani testator + disaksikan (formaliti Wills Act 1959 s.5) | 🔄 misi jurang Fasa 2 |
| N-PP-01 | WAJIB mesyuarat waris PPKP (proses Akta 98) sebelum perintah pembahagian | ✅ terverifikasi |

### 6.4 Enjin pengiraan bahagian (A5)
Deterministik (aritmetik pecahan munasabah, bukan LLM); skop terverifikasi: faraid (12 ashab al-furud, asabah, penyesuaian 'aul/radd, Baitulmal), wasiat 1/3 (selepas hutang/kos jenazah), harta sepencarian (s.122 Akta 303 — kecenderungan equality of division, fakta diambil kira), hibah, intestate civil (Act 300). Test vectors daripada kes repo + sumber syariah berautoriti; semakan panel pakar syariah wajib sebelum pengeluaran (Fasa 3.6).

### 6.5 Aliran kes end-to-end (contoh Muslim, pusaka kecil — dengan data sebenar)
1. Intake & klasifikasi (A3): Muslim, tanpa wasiat, nilai RM1.2j → laluan PPKP (≤RM5j).
2. Norma pra-syarat (A8): N-PK-01 → WAJIB sijil faraid terlebih dahulu (fi RM30/RM20/RM10; ~5 hari).
3. Penasihat (A2/A1): senarai waris, hak, tanggungjawab fiduciary, kos (fi PPKP RM30/RM50 + 0.2–0.3%).
4. Pengiraan (A5): jadual faraid dengan justifikasi langkah demi langkah.
5. Analitis kes (A4): kes serupa (Templat A–F) — risiko (hibah dicabar, waris hilang).
6. Dokumen (A7): Borang A + senarai aset + sijil faraid untuk mesyuarat waris.
7. Serahan (manusia): melalui MyLAND/kaunter PPKP — **agensi memutuskan**.
8. Orkestrasi (A6): jejak status mesyuarat waris → perintah → pendaftaran (Borang 14A, NLC s.346) → penutupan. Semua pelanggaran norma direkod; eskalasi manusia pada setiap titik serahan.

### 6.6 Platform webapp (lapisan)
1. Knowledge Base (repo 22 fail + RAG index) · 2. Perpustakaan Norma (deontik) · 3. Enjin Kiraan · 4. Agent Runtime (A1–A8 + audit + peranan pengguna) · 5. UI: wizard klasifikasi, penjejak checklist, kalkulator, case file, chat advisorial, eskalasi pakar · 6. Integrasi (eksport borang; sambungan agensi bila tersedia). **Prototype visual sedia:** `09-webapp-blueprint/agent-ops-dashboard.html` (Opis EA-MY).

---

## 7. Deliverable Fasa 2 & Status

| Deliverable | Status |
|---|---|
| Jurnal v2.0 (dokumen ini) | ✅ siap — menunggu semakan pemilik projek |
| Data pack & trend (`05-statistics/data-pack.md`) | 🔄 berjalan (subagent) |
| Matriks RP↔bukti (`00-project/rp-bukti-matriks.md`) | 🔄 berjalan (subagent) |
| Misi jurang: undang-undang (s.29 Akta 98, Wills Act s.5, enakmen wasiat Selangor, Sabah/Sarawak) | 🔄 berjalan (subagent) |
| Misi jurang: fi & statistik (fi ARB/mahkamah, statistik probat, backlog JKPTG 2022–24) | 🔄 berjalan (subagent) |
| Semakan pakar luar (peguam/pakar syariah) | ⏸ dicadang — menunggu keputusan pemilik projek (D-5) |

---

## 8. Risiko, Had & Tatakelola

| Risiko/had | Status semasa | Mitigasi |
|---|---|---|
| Nasihat guaman berlesen (Legal Profession Act) | ⚠️ kedudukan perlu disahkan (belum diverifikasi dalam sumber awam Fasa 1) | Pemosisian "maklumat & sokongan proses"; disclaimers; eskalasi peguam; modul profesional |
| Angka dipertikaikan (RM60–90b) | ✅ dikenal pasti | Guna dengan caveat + pecahan separuh-rasmi (RM65b) + rasmi (WTD RM13.3b) |
| Kegagalan kredit agent (HTTP 402) | ✅ dialami & diatasi Fasa 1 (salvage protocol) | Tulis berperingkat + snapshot git kerap |
| PDPA & data peribadi waris | ⚠️ kewajiban perlu disahkan | Simpanan minimum, kebenaran, kawalan akses (Fasa 3.5/3.6) |
| Khilaf pendapat syariah | Diakui (cth. hibah bersyarat takaful berbeza operator) | A2 bermula dari sumber berautoriti disahkan + panel semakan; pendedahan dalil |
| Keputusan syariah tidak diterbitkan | ✅ didokumenkan (Gaps stream 6) | A4 hanya petik kes bercitation; teks penuh perlu esyariah.gov.my sebelum "autoriti" |

---

## 9. Keputusan untuk Pemilik Projek (selepas review)

| # | Keputusan | Pilihan |
|---|---|---|
| D-1 | Go/no-go **Fasa 3** | Mulakan dengan sub-fasa 3.2 (Perpustakaan Norma) + 3.4 (enjin kiraan) dahulu? |
| D-2 | **Modul MVP** pertama | (a) Wizard klasifikasi kes · (b) Kalkulator faraid + audit trail · (c) Chat advisorial RAG · (d) Penjejak proses/checklist |
| D-3 | **Pemosisian** | Awam (maklumat pendidikan) vs profesional (decision-support peguam/pentadbir) vs kedua-dua berperingkat |
| D-4 | **Skop geografi** | Semenanjung dahulu (jurang Sabah/Sarawak masih terbuka) vs tunggu misi jurang selesai |
| D-5 | **Semakan pakar luar** | Libatkan peguam/pakar syariah sebelum pembinaan enjin (Fasa 2.6)? |
| D-6 | **Data & PDPA** | Pendekatan simpanan data pengguna bila webapp dibina |

---

## 10. Panduan Bacaan (study path untuk pemilik projek) & Rujukan

**Susunan bacaan disarankan untuk memahami keseluruhan proses & bidang kuasa EA:**
1. `01-legal-framework/jurisdiction-civil-vs-syariah.md` — faham dulu siapa pegang apa kuasa (Art 121(1A), twin-track *Latifah*)
2. `01-legal-framework/civil-law.md` — akta-akta mesinari (Act 97, 98+A1643, 300, 346, 532)
3. `01-legal-framework/syariah-law.md` — faraid, wasiat, hibah, penama, sepencarian
4. `03-processes/process-maps.md` — 7 laluan langkah demi langkah (dokumen/yuran/tempoh)
5. `02-institutions/courts-and-offices.md` + `amanahraya-berhad.md` — siapa buat apa
6. `04-products/comparison-matrix.md` — produk perancangan harta berbanding
7. `06-case-studies/lessons-and-templates.md` — Templat A–F (paling praktikal!)
8. `07-limitations/bottlenecks.md` + `solutions-and-reforms.md` — masalah & inisiatif sedia ada
9. `05-statistics/` — angka besar; untuk ringkasan pantas setiap stream baca `00-project/fasa1-stream-summaries.md`
10. Kembali ke jurnal ini → `00-project/pelan-tindakan-berfasa.md`

---

*Versi 2.0 dikemas kini oleh Zizi pada 2026-10-31. Matriks RP↔bukti, data pack dan dua misi jurang sedang berjalan dan akan dilampirkan sebagai rujukan silang jurnal apabila siap. **Semakan pemilik projek (Kimie) diperlukan sebelum Fasa 3 dimulakan.***
