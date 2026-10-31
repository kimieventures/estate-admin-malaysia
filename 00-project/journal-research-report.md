---
title: "Jurnal Penyelidikan & Analisis — Pentadbiran Pusaka di Malaysia: Ilmu, Research Problems dan Resolusi Melalui Sistem Automasi Pakar Berasaskan Agent"
project: EA-MY (Estate Administration Malaysia)
version: 0.1 (kerangka draf — menunggu verifikasi 7 stream kajian Fasa 1)
updated: 2026-10-31
status: draft — Fasa 1 berjalan
bahasa: Bahasa Malaysia (formal); rujukan civil/common law dibenarkan dalam English
authors: Zizi (Hermes agent, profile estateadministration-project) bersama Kimie (pemilik projek)
---

# Jurnal Penyelidikan & Analisis — Pentadbiran Pusaka di Malaysia

## 1. Abstrak

Dokumen ini ialah **jurnal penyelidikan induk** projek EA-MY. Tujuannya tiga lapis: (i) memetakan ilmu pentadbiran pusaka (Estate Administration, EA) di Malaysia secara menyeluruh — undang-undang dwi-jurisdiction civil–syariah, institusi, proses, produk, statistik, kes rujukan dan kekangan; (ii) membentuk **pernyataan masalah penyelidikan (research problems/statements)** berdasarkan analisis punca–kesan kepincangan semasa pentadbiran pusaka; dan (iii) mengemukakan **konsep resolusi** menerusi platform webapp dan **kumpulan agent pakar (agentic AI)** yang bertindak sebagai expert advisory — penasihat legal/syariah seperti peguam — dan pegawai pentadbir yang mengurus serta melaksanakan arahan mahkamah syariah/civil, termasuk automasi proses menerusi **logik deontik (deontic logic)** dan enjin pengiraan bahagian faraid/hibah/wasiat/intestate.

Versi 0.1 ini menetapkan kerangka, struktur ilmu dan pernyataan masalah. Data, angka dan rujukan citation penuh akan diintegrasikan apabila tujuh (7) stream kajian Fasa 1 selesai dan lulus kawalan kualiti citation. Setiap dakwaan fakta yang belum disahkan ditanda `[status: dalam verifikasi]` atau `PERLU SAHKAN`.

---

## 2. Latar Belakang & Konteks

### 2.1 Pentadbiran pusaka sebagai perkhidmatan fiduciary

Estate administration ialah perkhidmatan **fiduciary**: pentadbir pusaka (administrator) atau pelaksana wasiat (executor) bertindak dalam kedudukan amanah (position of trust) untuk mengesan, mengumpul dan mengurus harta si mati; melangsaikan hutang serta perbelanjaan pentadbiran; kemudian membahagikan baki harta kepada waris/benefisiari yang berhak selaras dengan undang-undang, wasiat (jika ada) dan arahan mahkamah atau agensi berautoriti. Kegagalan melaksanakan tugas fiduciary boleh menjadi punca pertikaian dan tindakan mahkamah — sila rujuk folder `06-case-studies/` untuk kes-kes berkaitan breach of trust.

### 2.2 Struktur dwi-jurisdiction Malaysia

Malaysia mengamalkan sistem **dwi-jurisdiction**:

| Saluran | Bidang | Peranan dalam EA |
|---|---|---|
| Civil | Mahkamah Tinggi (High Court) | Geran probat / letters of administration bagi pusaka melebihi had pusaka kecil |
| Civil/rasmi | Pejabat Pusaka Kecil (PPKP) di bawah JKPTG (Land Administrator) | Pembahagian pusaka kecil (had nilai — dalam verifikasi, rujuk `01-legal-framework/civil-law.md`) |
| Syariah | Mahkamah Syariah (JKSM) | Penetapan waris & kadar bahagian faraid bagi si mati Muslim (sijil faraid), kesahihan wasiat/hibah, harta sepencarian |
| Korporat kerajaan | Amanahraya Berhad (ARB) | Trustee/pentadbir pusaka profesional yang dilantik `[status: dalam verifikasi — 02-institutions/amanahraya-berhad.md]` |

Bagi si mati **Muslim**, mesinari pentadbiran (geran, pusaka kecil, pemindahan harta) kekal dalam saluran civil/rasmi manakala penetapan bahagian syarie memerlukan **sijil faraid** daripada mahkamah syariah — justeru kebanyakan kes Muslim melibatkan kedua-dua saluran serentak. Asas perlembagaan pembahagian ini ialah Perkara 121(1A) dan Senarai Kesembilan (Ninth Schedule) Perlembagaan Persekutuan `[status: dalam verifikasi — 01-legal-framework/jurisdiction-civil-vs-syariah.md]`.

### 2.3 Kenapa projek ini dijalankan

Pentadbiran pusaka di Malaysia kerap dilaporkan menghadami kelewatan, harta tertunggak bernilai berbilion ringgit yang tidak dituntut, proses pelbagai agensi yang membebankan waris, dan kekurangan akses kepada kepakaran legal/syariah/fiduciary. Angka-angka khusus sedang dikumpul dalam `05-statistics/`. Masalah-masalah ini membentuk research problems di Seksyen 4 dan menjadi asas pembangunan penyelesaian di Seksyen 6.

---

## 3. Peta Ilmu Projek (Knowledge Map)

| Domain | Lokasi repo | Kandungan teras | Status |
|---|---|---|---|
| Dokumen projek | `00-project/` | Jurnal ini; pelan tindakan berfasa | Diterbitkan v0.1 |
| Undang-undang civil | `01-legal-framework/civil-law.md` | Probate & Administration Act 1959, Distribution Act 1958, Wills Act 1959, Small Estates Distribution Act 1955, Amanah Raya Berhad Act 2001, Trustees Act 1949, Unclaimed Moneys Act 1965, NLC 1965, FSA 2013, EPF Act 1991, Companies Act 2016 | Stream 1 berjalan |
| Undang-undang syariah | `01-legal-framework/syariah-law.md` | Faraid (ashab al-furud, asabah), wasiat (had 1/3), hibah, harta sepencarian, waqf, kedudukan penama (nominee), sijil faraid | Stream 2 berjalan |
| Bidang kuasa | `01-legal-framework/jurisdiction-civil-vs-syariah.md` | Art 121(1A), Ninth Schedule, koordinasi PPKP–JKSM–Mahkamah Tinggi, konflik bidang kuasa | Stream 2 berjalan |
| Institusi | `02-institutions/` | ARB, Mahkamah Tinggi, PPKP/JKPTG, JKSM, MdI, BPN, trustee berlesen | Stream 3 berjalan |
| Peta proses | `03-processes/process-maps.md` | Langkah, dokumen, yuran, tempoh bagi 7 laluan utama | Stream 3 berjalan |
| Produk EA | `04-products/` | Islamic estate planning & conventional + matriks perbandingan | Stream 4 — fail awal sudah ditulis (dalam semakan) |
| Statistik & demografi | `05-statistics/` | Harta tak dituntut, backlog, kematian, agama, penuaan | Stream 5 — fail awal sudah ditulis (dalam semakan) |
| Kes rujukan | `06-case-studies/` | Kes civil & syariah + pelajaran + template prosedur | Stream 6 berjalan |
| Kekangan | `07-limitations/` | Bottleneck + kaedah penyelesaian direkodkan | Stream 7 — fail awal sudah ditulis (dalam semakan) |
| Penambahbaikan | `08-improvements/roadmap-ideas.md` | Cadangan penambahbaikan proses | Stream 7 — fail awal ditulis (dalam semakan) |
| Blueprint webapp | `09-webapp-blueprint/` | Spesifikasi agent & platform | Dibina selepas Fasa 1 |

**Konvensyen ilmu:** Bahasa Malaysia formal; istilah legal English inline; setiap fakta bawa sitasi `[Sumber: ... — URL, dicapai tarikh]`; rujukan civil/non-syariah dibenarkan dalam English sepenuhnya; fakta tidak sah ditanda `PERLU SAHKAN`.

---

## 4. Research Problems / Pernyataan Masalah

Setiap masalah dinyatakan bersama punca, kesan, soalan kajian (RQ) dan sumber bukti yang akan mengesahkannya dalam Fasa 1–2.

### RP-01 — Harta pusaka tertunggak tidak dituntut (dead capital)
- **Pernyataan:** Sebahagian besar harta si mati di Malaysia tidak dituntut oleh waris dan terperangkap (akaun bank beku, tanah tanpa geran pentadbiran, wang tak dituntut di BPN, akaun EPF/insurans terbengkalai), menghasilkan kekayaan mati bernilai berbilion ringgit yang tidak produktif.
- **Punca:** waris tidak sedar berhak; tiada perancangan harta semasa hidup; kelewatan permohonan; proses dianggap rumit.
- **Kesan:** kerugian ekonomi keluarga & negara; harta terbiar bertahun; pertikaian muncul apabila waris akhirnya muncul.
- **RQ:** Berapa nilai harta tidak dituntut (trend tahunan)? Apa profil utama punca tidak tuntut?
- **Bukti:** `05-statistics/estate-statistics.md` (stream berjalan).

### RP-02 — Tempoh pentadbiran panjang & proses kompleks pelbagai agensi
- **Pernyataan:** Proses pentadbiran pusaka memakan masa berbulan hingga bertahun dan melibatkan pelbagai agensi dengan keperluan dokumen, borang dan yuran berbeza; waris tercicir di pertengahan proses.
- **Punca:** proses manual; dokumen berulang antara agensi; mesyuarat waris dan sijil faraid mengambil masa; tiada panduan hujung-ke-hujung.
- **Kesan:** harta beku lebih lama; kos meningkat; waris berputus asa.
- **RQ:** Berapa tempoh purata setiap laluan (probat/LA, pusaka kecil, BPN, EPF)? Di mana langkah paling lambat?
- **Bukti:** `03-processes/process-maps.md`, `07-limitations/bottlenecks.md`.

### RP-03 — Kerumitan dwi-jurisdiction (civil–syariah)
- **Pernyataan:** Pembahagian bidang kuasa civil–syariah (Art 121(1A)) mewujudkan proses silang — si mati Muslim memerlukan sijil faraid (mahkamah syariah) sebelum/menyertai geran civil atau pembahagian pusaka kecil — yang memeningkan orang awam dan meningkatkan risiko ralat permohonan serta pertikaian hibah vs pusaka.
- **Punca:** dua sistem undang-undang beroperasi serentak; tiada panduan bersepadu untuk awam; istilah teknikal berbeza.
- **Kesan:** permohonan ditolak/dilambatkan; pertikaian keluarga; keperluan peguam dua kali ganda.
- **RQ:** Bagaimana koordinasi sebenar antara PPKP–JKSM–Mahkamah Tinggi beroperasi? Apakah titik konflik yang kerap berlaku?
- **Bukti:** `01-legal-framework/jurisdiction-civil-vs-syariah.md`, `06-case-studies/`.

### RP-04 — Akses kepakaran legal/syariah/fiduciary terhad & berkos tinggi
- **Pernyataan:** Kepakaran peguam (civil), pegawai/ulama syariah dan pentadbir profesional fiduciary terhad dan mahal; komuniti luar bandar/B40 serta waris biasa sukar mendapat panduan yang betul pada kos munasabah.
- **Punca:** bilangan pakar terhad; yuran profesional; geografi; kesedaran rendah.
- **Kesan:** ralat permohonan; penipuan "khidmat nasihat" tidak berkelayakan; kes terbengkalai.
- **RQ:** Berapa kos sebenar pentadbiran mengikut laluan? Apa jurang akses antara kumpulan demografi?
- **Bukti:** `02-institutions/`, `04-products/` (yuran), `05-statistics/demographics.md`.

### RP-05 — Pengiraan bahagian (faraid/hibah/wasiat/intestate) ralat & tidak berstandard
- **Pernyataan:** Pengiraan bahagian pusaka secara manual — faraid (pecahan, penyesuaian 'aul/radd, asabah), hibah, wasiat (had 1/3 harta bersih), dan pembahagian intestate civil (Distribution Act 1958) — mudah berlaku ralat; tiada enjin piawai bersepadu yang boleh diaudit dan disambungkan kepada proses permohonan.
- **Punca:** aritmetik pecahan kompleks; variasi keluarga (waris campur, anak luar nikah, waris hilang); dokumen pengiraan tidak konsisten antara pihak.
- **Kesan:** bahagian salah dibayar/didaftarkan; pertikaian & tuntutan semula; kelewatan.
- **RQ:** Apa skema pengiraan muktamad bagi setiap kategori waris? Bagaimana penyesuaian ('aul, radd, harta sepencarian) dikira dan didokumenkan?
- **Bukti:** `01-legal-framework/syariah-law.md`, `01-legal-framework/civil-law.md` (skema Distribution Act), `06-case-studies/`.

### RP-06 — Data silos antara agensi; tiada status kes tunggal
- **Pernyataan:** Maklumat pusaka tersebar antara agensi (mahkamah, JKPTG/PPKP, JKSM, ARB, BPN, bank, EPF) tanpa integrasi; waris dan pentadbir tidak mempunyai satu sumber status kes, menyebabkan dokumen berulang dan ketiadaan kebolehanjejakan (traceability).
- **Punca:** sistem agensi berasingan; inisiatif digital tidak seragam `[status: dalam verifikasi — 07-limitations/solutions-and-reforms.md]`.
- **Kesan:** proses lembap; waris berulang kali menyerahkan dokumen sama; tiada rekod tunggal untuk audit.
- **RQ:** Apa sistem digital sedia ada di setiap agensi? Apa titik integrasi yang wujud/ketiadaan?
- **Bukti:** `07-limitations/solutions-and-reforms.md`.

### RP-07 — Waris tidak dikenali/tidak sedar; dokumen hilang
- **Pernyataan:** Kes kerap tergendala kerana waris tidak dapat dikesan atau tidak sedar haknya, dan dokumen asas (geran tanah, MYKAD/sijil kelahiran si mati, dokumen wasiat) hilang; mekanisme gantian memakan masa dan tidak diketahui umum.
- **Punca:** saiz keluarga besar, migrasi, hubungan tidak formal; simpanan dokumen lemah.
- **Kesan:** pembahagian tidak lengkap; harta terbiar; pertikaian kemudian.
- **RQ:** Apa mekanisme undang-undang bagi waris hilang (notis, dispensasi) dan dokumen hilang (salinan rasmi)? Berapa lama proses tersebut?
- **Bukti:** `07-limitations/bottlenecks.md`, `06-case-studies/lessons-and-templates.md`.

### RP-08 — Ilmu kes & amalan terbaik tidak berstruktur
- **Pernyataan:** Amalan penyelesaian daripada kes-eks terdahulu (public-access court cases, preseden, kaedah penyelesaian yang direkodkan) tidak diagih secara berstruktur; pentadbir baharu dan waris tidak mempunyai rujukan template yang boleh dicontohi untuk menentukan proses kerja.
- **Punca:** keputusan mahkamah tersebar; tiada pengelasan kes mengikut isu; kepakaran tersirat (tacit knowledge) dalam kalangan pegawai berpengalaman.
- **Kesan:** kepakaran tidak menular; kes berulang dengan ralat sama; masa keputusan panjang.
- **RQ:** Apa klasifikasi isu kes yang paling berguna untuk pentadbiran? Bagaimana template prosedur boleh diekstrak daripada keputusan mahkamah?
- **Bukti:** `06-case-studies/` (3 fail: civil, syariah, lessons & templates).

---

## 5. Analisis Masalah

### 5.1 Analisis punca (kategori)

| Kategori punca | Huraian | RP berkaitan |
|---|---|---|
| Rangka undang-undang & bidang kuasa | Dua sistem beroperasi serentak; akta berlapis; istilah teknikal berbeza | RP-03, RP-05 |
| Proses & prosedur | Pelbagai agensi, borang, mesyuarat; tiada panduan hujung-ke-hujung | RP-02, RP-06, RP-07 |
| Manusia & kesedaran | Perancangan harta rendah; waris tak sedar; sikap menangguh | RP-01, RP-04, RP-07 |
| Teknologi & data | Manual, silos, tiada status kes tunggal | RP-02, RP-06, RP-08 |
| Ekonomi & akses | Yuran profesional; jurang geografi & demografi | RP-01, RP-04 |

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

### 5.3 Rantai punca–kesan utama

```
Tiada perancangan harta semasa hidup
        ↓
Harta beku sebaik si mati (akaun/tanah/syer terkunci)
        ↓
Waris tidak sedar / tidak tahu langkah pertama
        ↓
Tiada permohonan atau permohonan tersalah laluan / dokumen tak lengkap
        ↓
Proses berulang + sijil faraid + mesyuarat waris = kelewatan berbulan-tahun
        ↓
Harta tertunggak (dead capital) + backlog agensi + pertikaian keluarga
```

Penyelesaian yang dicadangkan memutus rantai ini pada **setiap mata**: kesedaran (kandungan ilmu), langkah pertama (wizard klasifikasi kes), dokumen (senarai semak standard), pengiraan (enjin deterministik), dan kelewatan (orkestrasi proses berstatus tunggal).

---

## 6. Konsep Resolusi: Webapp + Kumpulan Agent Pakar + Logik Deontik

### 6.1 Prinsip reka bentuk

- **P1 — Grounded:** setiap nasihat/cadangan agent mesti berpuncakan repo ilmu bercitation; tiada "karangan". Dakwaan tanpa sumber ditolak oleh kawalan kualiti.
- **P2 — Autoriti manusia & agensi:** agent bertindak sebagai **expert advisory** (seperti peguam/penasihat) dan **sokongan pelaksanaan** (seperti pegawai pentadbir yang melaksanakan arahan mahkamah syariah/civil); keputusan muktamad kekal pada mahkamah/agensi berautoriti dan manusia bertauliah. Agent tidak menggantikan mahkamah atau peguam.
- **P3 — BM formal** untuk ilmu & antara muka; rujukan civil dalam English dibenarkan.
- **P4 — Auditability:** setiap cadangan pengiraan/langkah boleh dikesan ke norma dan sumber undang-undang.
- **P5 — Berfasa:** research (Fasa 1) → report/data (Fasa 2) → solution (Fasa 3); kriteria penerimaan setiap fasa seperti `00-project/pelan-tindakan-berfasa.md`.

### 6.2 Senarai agent (kumpulan pakar)

| ID | Agent | Peranan (analogi) | Ilmu rujukan | Had kuasa |
|---|---|---|---|---|
| A1 | Agent Penasihat Legal (Civil) | Peguam civil/peguamcara | `01-legal-framework/civil-law.md`, `jurisdiction-civil-vs-syariah.md` | Nasihat berasaskan citation; tak boleh wakil dalam mahkamah |
| A2 | Agent Penasihat Syariah | Penasihat syariah/ulama | `syariah-law.md`, fatwa bercitation | Nasihat ilmu faraid/wasiat/hibah; pentauliahan keputusan pada mahkamah syariah |
| A3 | Agent Penasihat EA/Fiduciary | Pegawai pentadbir profesional | `02-institutions/`, `04-products/` | Cadangan produk/prosedur fiduciary |
| A4 | Agent Analisis Kes (Case Analyst) | Peguam menyelidik preseden | `06-case-studies/` (RAG) | Mengenal pasti preseden & template; bukan jaminan hasil |
| A5 | Enjin Pengiraan Bahagian | "Kalkulator" pakar | Skema faraid/hibah/wasiat/Distribution Act | Deterministik, buat senarai semak (bukan LLM bebas) |
| A6 | Agent Orkestrator Proses | Pegawai pentadbir pelaksana | `03-processes/process-maps.md`, SOP Fasa 3 | Susun & jejak langkah; manusia tandatangani & serah |
| A7 | Agent Dokumen | Kerani pentadbiran | Template borang/surat | Draf dokumen untuk disemak manusia |
| A8 | Agent Pematuhan Deontik | Auditor pematuhan | Perpustakaan Norma (Seksyen 6.3) | Tandakan pelanggaran WAJIB/DILARANG sebelum tindakan |

**Pembahagian kerja utama** (selaras hasrat projek): A1–A4 ialah **expert advisory** yang menentukan proses/prosedur/kaedah berdasarkan kes; A6–A7 ialah **pegawai pentadbir** yang mengurus dan melaksanakan arahan/tindakan yang diberi oleh mahkamah syariah/civil; A5 memberikan pengiraan pecahan syer faraid/hibah (undang-undang Islam) atau wasiat/intestate (undang-undang civil); A8 memastikan setiap tindakan tidak melanggar norma.

### 6.3 Logik deontik dalam automasi proses

Proses pentadbiran pusaka sifatnya **normatif** — ia penuh dengan kewajiban, kebenaran dan larangan bersyarat. Kami menggubalkan **Perpustakaan Norma (Norm Library)** yang mengkod prosedur sebagai norma formal:

**Operator** (Standard Deontic Logic sebagai asas, dilaksana sebagai peraturan boleh dinilai mesin):
- `WAJIB(p)` — obligation: p mesti dilakukan
- `DIBENAR(p)` — permission: p boleh dilakukan
- `DILARANG(p)` — prohibition: DILARANG(p) ≡ WAJIB(¬p)
- Norma bersyarat: `WAJIB(p | q)` — jika keadaan q, maka p wajib
- **Contrary-to-duty (CTD):** jika norma WAJIB dilanggar (cth. dokumen hilang), norma pengganti diaktifkan (cth. WAJIB dapatkan salinan rasmi) — proses tidak mati, tetapi dipindah ke laluan gantian.

**Contoh skema peraturan (JSON):**

```json
{
  "norma_id": "N-PK-01",
  "domain": "pusaka_kecil",
  "modaliti": "WAJIB",
  "trigger": "permohonan_pembahagian_pusaka_kecil_muslim",
  "tindakan": "dapatkan_sijil_faraid",
  "susunan": "SEBELUM",
  "sumber": "amalan PPKP + Small Estates Distribution Act 1955 [akan disahkan]",
  "status_verifikasi": "PERLU SAHKAN"
}
```

**Contoh norma awal (semua menunggu verifikasi Fasa 1):**

| ID | Norma | Sumber dirujuk |
|---|---|---|
| N-PK-01 | WAJIB sijil faraid sebelum pembahagian pusaka kecil Muslim | `03-processes/`, `01-legal-framework/` |
| N-W-01 | DILARANG wasiat Muslim memberi manfaat melebihi 1/3 harta bersih tanpa persetujuan waris | `syariah-law.md` |
| N-WC-01 | WAJIB wasiat (civil) ditandatangani testator & disaksikan 2 saksi | `civil-law.md` (Wills Act 1959) |
| N-PA-01 | WAJIB geran probat/LA sebelum pengambilan harta melebihi had agensi | `civil-law.md` (Probate & Administration Act 1959) |
| N-EX-01 | DILARANG pentadbir membahagikan harta sebelum hutang & perbelanjaan pentadbiran dilangsaikan | urutan piawai pentadbiran `civil-law.md` |

**Mekanisme penilaian:** evaluator deterministik menyemak setiap langkah yang dicadang/dijalankan A6 terhadap norma berkaitan (precondition checking); pengesan konflik mengesan `WAJIB(p) ∧ WAJIB(¬p)` dan menyelesaikan mengikut keutamaan sumber (undang-undang > peraturan mahkamah > amalan agensi); setiap penilaian direkod dalam **audit trail**. Norma tidak boleh ditambah tanpa citation; norma tidak bercitation kekal `PERLU SAHKAN` dan tidak boleh dipaksa dalam modul pengeluaran (production).

### 6.4 Enjin pengiraan bahagian (faraid/hibah/wasiat/intestate)

- **Prinsip:** pengiraan **deterministik** (aritmetik pecahan nombor munasabah — bukan LLM) supaya boleh diaudit; LLM hanya untuk interpretasi input pengguna → struktur data; keputusan disertakan justifikasi langkah demi langkah.
- **Skop faraid:** senarai waris `ashab al-furud` (pemegang bahagian tetap) & `asabah` (pemilik baki); penyesuaian **'aul** (kekurangan) dan **radd** (lebihan); kedudukan khas (anak luar nikah, waris berlainan agama — akan disahkan dengan sumber syariah) `[status: dalam verifikasi]`.
- **Skop civil:** skema pembahagian intestate di bawah Distribution Act 1958 (pindaan semasa) `[status: dalam verifikasi]`; wasiat di bawah Wills Act 1959.
- **Skop wasiat/hibah Muslim:** had 1/3 harta bersih (selepas hutang & perbelanjaan), persetujuan waris bagi pemberian kepada waris `[status: dalam verifikasi]`.
- **Harta sepencarian:** penyesuaian sebelum pembahagian faraid, berdasarkan kes dan enakmen `[status: dalam verifikasi]`.
- **Pengujian:** test vectors daripada kes bercitation + buku teks/panduan berautoriti; lulus 100% sebelum dikeluarkan; semakan panel pakar syariah (Fasa 3.6).

### 6.5 Aliran kes end-to-end (contoh: si mati Muslim, pusaka kecil, tanpa wasiat)

1. **Intake:** waris masukkan maklumat si mati & harta melalui wizard webapp.
2. **Klasifikasi kes:** A1/A2 tentukan kategori (Muslim/bukan; wasiat/tiada; nilai pusaka; jenis harta) → tentukan laluan (pusaka kecil vs geran; ARB/individual).
3. **Penasihat (A1–A3):** terangkan laluan, hak, tanggungjawab fiduciary, kos & jangkaan masa — setiap satunya bercitation.
4. **Norma (A8):** senarai semak keperluan dibina (dokumen, sijil faraid, MYKAD, geran).
5. **Pengiraan (A5):** struktur waris dimasukkan → jadual faraid (dengan justifikasi) atau skema Distribution Act.
6. **Analitis kes (A4):** kes serupa diimbas; risiko & presiden dilaporkan.
7. **Dokumen (A7):** borang & surat disediakan untuk disemak manusia.
8. **Serahan (manusia):** waris/pentadbir serahkan ke PPKP/mahkamah — platform menyediakan, **agensi yang memutuskan**.
9. **Orkestrasi (A6):** status kes dijejak (sijil faraid → mesyuarat waris → keputusan → pemindahan) dengan peringatan & norma semakan.
10. **Pelaksanaan arahan:** arahan mahkamah/agensi dimasukkan → A6 pecahkan kepada tugas pelaksanaan (draf, dokumen, pindahan, pembayaran) — setiap tugas lulus semakan A8.
11. **Pengauditan:** audit trail penuh (siapa cadang apa, berasaskan norma/sumber mana).
12. **Penutupan:** laporan pengagihan & rekod untuk semua pihak.

### 6.6 Struktur platform webapp (lapisan)

1. **Knowledge Base** — repo ilmu (git) + indeks RAG; citation wajib.
2. **Perpustakaan Norma** — norma deontik JSON + evaluator (Seksyen 6.3).
3. **Enjin Pengiraan** — faraid/hibah/wasiat/intestate deterministik (Seksyen 6.4).
4. **Agent Runtime** — A1–A8 (Seksyen 6.2), audit trail, kawalan akses peranan (waris, pentadbir, pegawai, admin).
5. **Antara muka (UI)** — wizard klasifikasi kes; penjejak checklist & status; kalkulator; case file & dokumen; modul perbualan advisorial; eskalasi kepada pakar manusia.
6. **Integrasi** — eksport borang/piawaian agensi; sambungan sistem agensi bila tersedia `[status: dalam verifikasi — 07-limitations/solutions-and-reforms.md]`; human-in-the-loop di semua titik serahan.

---

## 7. Ringkasan Pelan Berfasa

| Fasa | Takrif (mengikut pelan induk) | Output utama | Status |
|---|---|---|---|
| **Fasa 1** | Kajian kes, research problems/statements & analisis | Repo 01–08 terisi bercitation; jurnal (dokumen ini); daftar RP; klasifikasi kes | **BERJALAN** (7 stream research) |
| **Fasa 2** | Research report/writing, fact findings/data & analisis | Jurnal v2.0 verified; data pack; matriks RP↔bukti; draf SOP & norma | Belum mula (auto selepas Fasa 1) |
| **Fasa 3** | Develop solution: structured process/procedures + automation agentic AI/deontic logic + webapp | SOP digital; Perpustakaan Norma; agent A1–A8; enjin pengiraan; webapp MVP; pilot | Belum mula |

Butiran penuh aktiviti, deliverable dan kriteria penerimaan: `00-project/pelan-tindakan-berfasa.md`.

---

## 8. Risiko, Had & Tatakelola

| Risiko/had | Huraian | Mitigasi |
|---|---|---|
| Nasihat guaman berlesen | Hanya peguam berlesen boleh memberi nasihat guaman formal `[status: kedudukan undang-undang perlu disahkan]` | Platform diposisikan sebagai maklumat pendidikan + sokongan proses & draf; disclaimers jelas; eskalasi ke peguam; modul profesional untuk peguam/pentadbir |
| Autoriti keputusan | Agent tidak boleh dianggap menggantikan mahkamah/agensi | P2: keputusan muktamad agensi; semua serahan human-in-the-loop |
| Halusinasi ilmu | LLM boleh karang | P1: grounding wajib + kawalan citation + semakan pakar sebelum pengeluaran |
| Data peribadi | Data waris sensitif (PDPA) `[status: kewajiban PDPA perlu disahkan]` | Simpanan minimum, kebenaran pengguna, kawalan akses, pilihan data |
| Kualiti sumber | Statistik/kutipan media mungkin berulang tanpa asal | Fasa 2: sahkan rujukan silang; tandakan sumber sekunder |
| Kaedah syariah berbeza mazhab/pendapat | Hukum faraid/hibah boleh ada khilaf | A2 hanya bermula daripada sumber berautoriti yang disahkan; panel semakan syariah (Fasa 3.6) |
| Keselamatan platform | Serangan & kebocoran | Kadar capaian, audit, sandaran, ujian keselamatan sebelum MVP |

---

## 9. Rujukan Struktur

- Repo ilmu: `/opt/data/profiles/estateadministration-project/estate-admin-malaysia/`
- Pelan tindakan: `00-project/pelan-tindakan-berfasa.md`
- Konvensyen sitasi & bahasa: `README.md` (repo)
- Semua citation fakta hidup dalam fail domain masing-masing (01–08).

*Tarikh kemas kini: 2026-10-31 — versi 0.1 akan dinaik taraf ke v2.0 selepas verifikasi Fasa 1 & sintesis Fasa 2.*
