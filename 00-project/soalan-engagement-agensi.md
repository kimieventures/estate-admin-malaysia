---
title: "Kertas Soalan Engagement Agensi — Kemushkilan & Persoalan untuk Melonggarkan Stopblocker Sistem EA-MY"
project: EA-MY
version: 1.0
updated: 2026-11-01
status: final — untuk pertemuan/misi jurang
kategori: 00-project
asas: Semua soalan diwarisi daripada seksyen Gaps & item PERLU SAHKAN dalam fail repo (Fasa 1–2 + blueprint). Setiap soalan menyatakan fail asas — tiada soalan direka tanpa asas.
---

# Kertas Soalan Engagement Agensi (JKSM · JKPTG · ARB · Jabatan Kehakiman · BPN · KWSP · JPN · PTG)

## 0. Cara Guna Dokumen Ini

Disediakan untuk pertemuan/rujukan rasmi dengan agensi pentadbiran pusaka. Setiap soalan ada: **Konteks** (dari mana kemushkilan datang — fail repo), **Hint jawapan** (arah jawapan yang kami jangka & apa yang ia longgarkan), dan **Impact** (modul/keputusan yang terbuka). Keutamaan ditanda: 🔴 **STOPBLOCKER** (mesti dijawab sebelum modul berkaitan boleh LIVE) · 🟠 PENTING (sebelum pilot) · 🟡 BAIK ADA (meningkatkan mutu).

**Ringkasan:** 33 soalan merentas 9 stakeholder — 🔴 8 stopblocker, 🟠 13 penting, 🟡 12 baik ada.

| Stakeholder | Soalan | Stopblocker |
|---|---|---|
| JKSM / Mahkamah Syariah | 9 | 3 |
| JKPTG / PPKP | 6 | 1 |
| Amanahraya Berhad (ARB) | 4 | 2 |
| Jabatan Kehakiman Malaysia | 4 | 1 |
| BPN / JANM | 3 | 0 |
| KWSP | 3 | 1 |
| JPN | 2 | 0 |
| Pejabat Tanah & Galian | 2 | 0 |
| Majlis Peguam / Tadbir urus | 2 | 🔴 (kedua-duanya) |

---

## A. JKSM / MAHKAMAH SYARIAH (9 soalan)

**JQ-01 🔴 — Amalan sijil kes munasakhat (faraid berlapis): SATU perintah jami'ah atau SIJIL BERTINGKAT per si mati?**
- Konteks: Peraturan munasakhat terverifikasi (MAIS E-FARAID §8; kes AL-KAFI #1021 — 8 lapisan), tetapi **tiada arahan amalan rasmi dalam talian** tentang bilangan dokumen mahkamah keluarkan bagi kes berlapis [rujuk: `01-legal-framework/research-faraid-berlapis.md` Gaps #1; `09-webapp-blueprint/modul-penentuan-faraid.md` Lapis 4].
- Hint jawapan: Kami jangka jawapan kemungkinan **sijil/perintah BERASINGAN bagi setiap si mati** (bidang kuasa mahkamah tertakluk kepada si mati masing-masing) — jika betul, Enjin Munasakhat perlu menjana **satu SET permohonan bersiri** (sijil lapisan-1 → digunakan untuk permohonan sijil lapisan-2), bukan satu dokumen jami'ah. Mohon pengesahan + borang/urutan sebenar.
- Impact: Menentukan **format output utama** Enjin Penentuan Faraid (Lapis 4) — tanpa ini enjin tak boleh live.

**JQ-02 🔴 — Konfigurasi RADD vs BAITULMAL: amalan mana yang dipegang mahkamah negeri bagi baki pusaka tanpa asabah?**
- Konteks: Mekanik radd terverifikasi, TETAPI **amalan MAIS = baki ke Baitulmal** (bukan radd mutaakhirin); kedudukan MAIWP/negeri lain belum disahkan [rujuk: `research-faraid-berlapis.md` kesimpulan; `modul-penentuan-faraid.md` F3].
- Hint jawapan: Kami perlukan **pengesahan amalan PER NEGERI** + asasnya (kitab/arah amalan/fatwa) untuk jadual konfigurasi enjin. Jika amalan berbeza antara negeri, sistem akan config per negeri — jangan generalize.
- Impact: Lapis 3 (pecahan) — kiraan akhir berbeza ikut konfigurasi; panel pakar akan sahkan selepas ini.

**JQ-03 🔴 — Kedudukan WASIAT WAJIBAH di negeri TANPA enakmen (FT/Johor/Kedah/Pulau Pinang/Perlis/Terengganu): adakah diamalkan (siyasah/fatwa) atau tidak terpakai?**
- Konteks: Enakmen disahkan di 5 negeri (Selangor 1999/2016, Pahang 2017, Perak 2023, Melaka 2005, NS 2004) dengan liputan cucu berbeza; negeri lain belum disahkan [rujuk: `research-faraid-berlapis.md` seksyen 5].
- Hint jawapan: Kami jangka negeri tanpa enakmen **tidak terpakai secara automatik** — minta pengesahan + sama ada terdapat perbezaan perlakuan walaupun tiada enakmen (amalan pentadbiran). Enjin akan flag "wasiat wajibah tidak berkuat kuasa di negeri X" dengan citation.
- Impact: Rule engine Lapis 2 — konfigurasi negeri.

**JQ-04 🟠 — Jadual fi sijil faraid per negeri (warta rasmi semasa)**
- Konteks: JKSM FAQ menyatakan RM30/RM20/RM10 "tanpa menyatakan negeri rujukan"; jadual negeri berpecah (Selangor P.U. 22/2004 dsb. — sumber ketiga) [rujuk: `syariah-law.md` Gaps #3; `gap-mission-fi-statistik.md`].
- Hint jawapan: Mohon salinan warta/jadual semasa SETIAP negeri + tarikh kuat kuasa. Enjin fi akan muat sebagai jadual berversi (tarikh peristiwa menentukan versi).
- Impact: Enjin Fi (`modul-pematuhan-enjin-fi.md` §B2).

**JQ-05 🟠 — Arahan Amalan No. 5/2003 (tuntutan harta sepencarian selepas kematian): masih berkuat kuasa di semua negeri? Borang & tempoh?**
- Konteks: Arahan ini asas aliran sepencarian pasca-kematian [rujuk: `syariah-law.md` §9; cross-examination S4]; perlu pengesahan tarikh kuat kuasa semasa + dokumen rasmi yang diterima (perintah MTS sebagai prasyarat KWSP MKI-128).
- Hint jawapan: Mohon teks arahan semasa + status negeri (Sarawak tiada e-Syariah V3 — bagaimana di sana?).
- Impact: Aliran pintu S3/S4 bagi pasangan Muslim; integrasi KWSP.

**JQ-06 🟠 — Perlaksanaan MKI-128 (Sept 2025) tentang tuntutan sepencarian ke atas KWSP: arahan/borang yang dikeluarkan kepada KWSP?**
- Konteks: Muzakarah mengharuskan tuntutan tertakluk perintah MTS; **perlaksanaan oleh KWSP belum direkodkan** [rujuk: `modul-pengagihan-aset.md`; `research-faraid-berlapis.md` berkaitan].
- Hint jawapan: Adakah wujud arahan bersama JKSM-KWSP/borang khas? Enjin perlu tahu dokumen perintah yang diterima KWSP untuk melonggarkan tuntutan.
- Impact: Modul A2 (nasihat KWSP/sepencarian).

**JQ-07 🟡 — Sistem e-Faraid JKSM (efaraid.esyariah.gov.my): status penyelenggaraan & adakah kfaraid.gov.my menyokong munasakhat?**
- Konteks: Semakan kami 2026-11-01: **server hidup tetapi sijil TLS (*.jwp.gov.my) tidak sepadan hos** — pelayar sekat; kfaraid JKSM belum diuji berfungsi; MyLAND single-layer [rujuk: `research-faraid-berlapis.md` #7-8].
- Hint jawapan: Lapor isu teknikal TLS (mungkin mereka tak sedar!); tanya roadmap: adakah kalkulator rasmi akan sokong munasakhat? adakah API tersedia untuk integrasi sistem pihak ketiga berlesen?
- Impact: Peluang kerjasaka teknikal; penempatan enjin kita dalam ekosistem.

**JQ-08 🟡 — Protokol rujuk-balik civil–syariah: adakah wujud pekeliling KOORDINASI antara KPTG/mahkamah sivil tentang penggunaan sijil faraid?**
- Konteks: Yang didokumenkan hanyalah s.50 Akta 505 + prinsip *Latifah* + Surat Edaran KPTG (sijil faraid bukan instrumen daftar); **tiada protokol bertulis ditemui** [rujuk: `jurisdiction-civil-vs-syariah.md` Gaps #1].
- Hint jawapan: Mohon salinan sebarang pekeliling/garis panduan dalaman; jika tiada — ini pengesahan bahawa kekosongan wujud (dalamnya ada peluang platform kita jadi "jambatan" standard).
- Impact: Modul klasifikasi dwi-jurisdiction (S1) — kepastian dokumen yang diakui antara agensi.

**JQ-09 🟡 — Capaian teks penuh keputusan Mahkamah Syariah (preseden): repositori awam?**
- Konteks: Kes syariah dalam repo kami dipetik melalui jurnal akademik sahaja; teks penuh diperlukan sebelum modul A4 memetik sebagai "autoriti" [rujuk: `klasik-vs-agent-syariah.md` Gaps].
- Hint jawapan: Mohon laluan capaian repositori (baca sahaja) atau prosedur permohonan; jika terbuka — A4 boleh citation-grade.
- Impact: Modul analitis kes A4.

---

## B. JKPTG / PEJABAT PUSAKA KECIL (6 soalan)

**JP-01 🔴 — MyLAND & kalkulator faraid: adakah roadmap untuk MEDAN MUNASAKHAT (kes berlapis)? Bolehkah senarai semak rasmi permohonan dikongsi untuk wizard intake kami?**
- Konteks: Disemak terus: MyLAND **single-layer tanpa medan munasakhat**; kalkulator faraid terpisah daripada proses [rujuk: `research-faraid-berlapis.md` #8; `modul-penentuan-faraid.md` F7].
- Hint jawapan: Kami bukan minta akses sistem dalaman — minta (a) pengesahan jurang berlapis diiktiraf, (b) senarai semak dokumen RASMI per laluan (untuk validasi Lapis 1 kami supaya permohonan siap lengkap kali pertama), (c) sama ada JKPTG sedia jadikan syarikat rujukan penyedia khidmat persediaan dokumen (benchmark SG membenarkan permohonan tanpa peguam).
- Impact: Validasi intake; kedudukan "partner persediaan dokumen" — teras model bisnes sistem.

**JP-02 🟠 — Data statistik: siri backlog & kes selesai 2022–2024 + penyelesaian konflik angka rasmi**
- Konteks: Titik 2022–2024 tidak diterbitkan; konflik didokumenkan: kes 2021 (25,988 Ketua Pengarah vs 43,519 Menteri), 31 Dis 2025 (Hansard 46,707/84,384 vs RTM 46,077/84,028); 72,348 = Ogos 2022 [rujuk: `gap-mission-fi-statistik.md` Misi 4; `05-statistics/data-pack.md`].
- Hint jawapan: Mohon siri tahunan rasmi + rekonsiliasi konflik. Data ini jadi **baseline metrik** kami (KPI: dokumen lengkap kali pertama) — kami boleh kongsi hasil analisis balik kepada JKPTG.
- Impact: Data pack & KPI; laporan penyelidikan kami lebih boleh dipercayai.

**JP-03 🟠 — Punca penolakan/kelewatan permohonan pusaka kecil: adakah statistik punca dirakam?**
- Konteks: Punca kelewatan kualitatif sahaja (waris tak lengkap, berlapis, pertikaian — Bernama 29-01-2026); tiada pecahan volum [rujuk: `05-statistics/estate-statistics.md`].
- Hint jawapan: Kalau punca direkod dalam MyeTaPP/MyLAND — minta pecahan % punca; jika tidak direkod — cadang JKPTG manfaatkan laporan analisis kami untuk kategori punca standard.
- Impact: Matric RP-02; module priority.

**JP-04 🟠 — Pengesahan amalan tempoh rayuan s.29 selepas Act A1643 (30 hari) + tarikh warta P.U.(B) 267/2024 + taras Small Estates (Distribution) Rules (s.30)**
- Konteks: Kami selesaikan 14 vs 30 hari melalui teks LOM (30 hari bagi perintah ≥15.7.2024; klausa simpanan s.25(3) bagi perintah lama) — minta pengesahan rasmi + salinan warta + kajian Rules (s.30) yang mungkin mengatur tatacara rayuan [rujuk: `gap-mission-undang-undang.md` Misi 1].
- Hint jawapan: Pengesahan + dokumen rujukan; kami akan paparkan 30-hari (dengan klausa tarikh) dan flag risalah usang 14-hari.
- Impact: Norma kalkulator tarikh (N-RT-01 baru); koreksi maklumat awam.

**JP-05 🟡 — SLA/masa median sebenar per peringkat: permohonan → mesyuarat waris → perintah → (penyerahan ke PTG)**
- Konteks: Yang terbit: piagam 4 bulan, FAQ 4–6 bulan, min 5½ bulan Borang A; **tiada median per peringkat** [rujuk: `data-pack.md`; `bottlenecks.md`].
- Hint jawapan: Median per peringkat membolehkan kami paparkan "jangkaan masa jujur" kepada pemohon — Kurangkan keputusasaan waris (cross-examination: kelewatan tak dijangka = punca cicir).
- Impact: Fitur jangkaan masa (S1); KPI.

**JP-06 🟡 — Perbezaan amalan & fi antara negeri bagi permohonan pusaka kecil (warta negeri, borang DDA dsb.)**
- Konteks: Fi utama persekutuan (P.U.(A) 194/2024) disahkan, tetapi amalan negeri (negeri berbeza prosedur kertas/mesyuarat) [rujuk: `process-maps.md`].
- Hint jawapan: Mohon matriks perbezaan negeri; enjin proses akan config per negeri.
- Impact: Konfigurasi workflow engine per negeri.

---

## C. AMANAHRAYA BERHAD — ARB (4 soalan)

**AR-01 🔴 — Jadual fi pentadbiran pusaka AM (SEMENANJUNG, semua jenis aset) + deposit: skala 5%→1% yang diterbitkan di FAQ didapati bagi pentadbiran kenderaan/pusaka Sabah — sahkah ia untuk pusaka am?**
- Konteks: FAQ rasmi menyenaraikan skala untuk skop tertentu; **jadual khusus pusaka am Semenanjung tidak diterbitkan eksplisit** [rujuk: `gap-mission-fi-statistik.md` Misi 1; `modul-pematuhan-enjin-fi.md` §B2].
- Hint jawapan: Mohon jadual fi lengkap (jenis aset × skala × deposit × tempoh). Jika fi berbeza ikut kategori, kami muat sebagai jadual berversi. Ini penting kerana enjin fi TIDAK boleh bil berasaskan jadual PERLU SAHKAN.
- Impact: Enjin Fi — penerbitan bil ARB dalam aliran.

**AR-02 🔴 — Yuran trust administration / pending fund management: adakah didedahkan (untuk waris bawah umur & penaja amanah)?**
- Konteks: Tidak didedahkan di laman rasmi; penting bagi kes waris bawah umur (modul pengagihan menahan bahagian) [rujuk: `gap-mission-fi-statistik.md` Gaps; `modul-pengagihan-aset.md` kes khas].
- Hint jawapan: Mohon kadar/struktur; jika berunding per-kes — enjin akan jadikan "fi berunding" dengan proses pengecualian berjustifikasi.
- Impact: Modul pengagihan (waris bawah umur) + enjin fi.

**AR-03 🟠 — Statistik tahunan permohonan pusaka ringkas s.17(1) PTCA (≤RM600k harta alih): volum, kadar lulus, tempoh purata**
- Konteks: Laman rasmi menyatakan jumlah kumulatif (230,000+ kes) tetapi **tiada siri tahunan** [rujuk: `amanahraya-berhad.md` Gaps].
- Hint jawapan: Siri tahunan menolok volum laluan ringkas — kami boleh mengesyorkan laluan ini kepada pemohon yang layak (ia laluan TERPENDEK tanpa mahkamah).
- Impact: Modul klasifikasi (S1) — cadangan laluan tepat.

**AR-04 🟡 — Kerjasaka digital: adakah ARB terbuka menerima permohonan/perwakilan melalui platform sokongan proses pihak ketiga (partner persediaan dokumen)?**
- Konteks: Model bisnes kami: sistem menyediakan pakej; ARB tetap pentadbir/trustee berautoriti. Contoh semula jayanya: Pegawai Probet Kuching = ARB sejak 1995 [rujuk: `amanahraya-berhad.md`].
- Hint jawapan: Jangkaan: terbuka secara berperingkat (standard SLA); jika ada program partner/reseller sedia ada — kami sertai. Jika tiada — mohon garis panduan apa yang diperlukan.
- Impact: Go-to-market; modul serahan S7 (laluan ARB).

---

## D. JABATAN KEHAKIMAN MALAYSIA — Mahkamah Tinggi/e-Kehakiman (4 soalan)

**KH-01 🔴 — Statistik kes probat/SKM (Kod 31 & 32): siri 2022–2025 + backlog**
- Konteks: **Yearbook Badan Kehakiman 2022/2023 diimbas penuh — TIADA siri kod 31/32**; angka terbaik 2013 (7,982 permohonan — kertas Tun Abdul Hamid) [rujuk: `gap-mission-fi-statistik.md` Misi 3; `data-pack.md`].
- Hint jawapan: Mohon siri rasmi (permohonan, pelupusan, baki). Tanpa ini, negara TAK BOLEH ukur masalah probat mahkamah — kami sedia kongsi analisis silang kami.
- Impact: Data pack (trend saluran mahkamah) — jurang pengukuran terbesar RP-01/RP-02.

**KH-02 🟠 — Adakah rancangan e-Probate awam (permohonan tanpa peguam bagi kes lurus)? + status SOP pendengaran probat online**
- Konteks: e-Filing oleh peguam sahaja; TIADA e-Probate awam; SG (≤S$2j tanpa peguam, 2023) & UK (MyHMCTS wajib) jadi benchmark; SOP probat online dilaporkan dari interaksi Bar Council tanpa tarikh [rujuk: `solutions-and-reforms.md`].
- Hint jawapan: Jika jawapan "tiada pelan semasa" — kami dokumentasikan jurang (sokong cadangan reformasi); jika "ada" — kami selaraskan format pakej permohonan kami.
- Impact: Positioning sistem; modul S7.

**KH-03 🟠 — Salinan jadual fi semasa (Lampiran B1 KKM 2012 via P.U.(A) 67/2013) + kedudukan selepas P.U.(A) 229/2023 + fi e-Filing**
- Konteks: RM160 (petisyen), RM16 (senarai aset), RM400 (resealing) disahkan; status konsolidasi & fi e-Filing CMS belum disemak menyeluruh [rujuk: `gap-mission-fi-statistik.md` Misi 2].
- Hint jawapan: Mohon jadual semasa + pengesahan tiada perubahan selepas 2013 selain dinyatakan.
- Impact: Enjin Fi (laluan Mahkamah Tinggi).

**KH-04 🟡 — SLA pendengaran tanpa pertikaian dalam 30 hari (AA 3/2009): adakah dipatuhi & diukur?**
- Konteks: Piagam wujud; pematuhan tidak diterbitkan [rujuk: `courts-and-offices.md`].
- Hint jawapan: Data pematuhan → jangkaan masa jujur kepada pemohon.
- Impact: Fitur jangkaan masa.

---

## E. BPN / JABATAN AKAUNTAN NEGARA (3 soalan)

**BN-01 🟠 — Tempoh pemprosesan tuntutan WTD (eGUMIS) & SLA: berapa lama selepas UMA-7 lengkap?**
- Konteks: Tiada had masa statutori (s.13(1) Akta 370) & tempoh tidak diterbitkan [rujuk: `process-maps.md`; `gap-mission-fi-statistik.md` Gaps].
- Hint jawapan: SLA dalaman (jangkaan: 14–30 hari) → kami paparkan kepada pemohon.
- Impact: Jangkaan masa laluan WTD.

**BN-02 🟡 — Pecahan demografi & punca WTD (umur/negeri/jenis akaun): boleh dikongsi untuk kajian?**
- Konteks: Hanya komposisi ~70% akaun bank tidak aktif diterbitkan [rujuk: `estate-statistics.md`; `demographics.md`].
- Hint jawapan: Data agregat (bukan peribadi) menyokong RP-01 (punca tak tuntut) — boleh jadi kertas kajian bersama.
- Impact: Penyelidikan RP-01; laporan.

**BN-03 🟡 — Borang UMA-7/UMA-8S versi semasa + senarai semak dokumen rasmi**
- Konteks: Dokumen kunci laluan WTD; senarai semak untuk wizard [rujuk: `process-maps.md`].
- Hint jawapan: Salinan borang semasa → validasi intake.
- Impact: Modul dokumen S2 (laluan WTD).

---

## F. KWSP (3 soalan)

**KW-01 🔴 — Perlaksanaan MKI-128 (tuntutan sepencarian ke atas simpanan KWSP): borang, dokumen perintah MTS yang DITERIMA, had & tempoh**
- Konteks: Muzakarah Sept 2025 mengharuskan; **perlaksanaan Lembaga KWSP belum direkodkan** — modul A2 isu KWSP tertahan [rujuk: `modul-pengagihan-aset.md`; `research-faraid-berlapis.md` berkaitan; `klasik-vs-agent-syariah.md` S4].
- Hint jawapan: Mohon arahan pelaksanaan/siaran rasmi kepada pasukan perkhidmatan KWSP + spesifikasi dokumen. Ini menentukan sama ada tuntutan sepencarian-KWSP boleh dialirkan melalui sistem kami.
- Impact: Modul sepencarian + integrasi KWSP — stopblocker operasi untuk kes pasangan Muslim.

**KW-02 🟠 — SLA pengeluaran kematian semasa + dasar bank bagi akaun kecil tanpa geran (jika masih diamalkan)**
- Konteks: Dasar lama "wang sebelah kubur" tidak bersumber semasa [rujuk: `bottlenecks.md`].
- Hint jawapan: SLA + pengesahan dasar semasa (pekeliling bank mana-mana?).
- Impact: Nasihat awal pemohon (S3).

**KW-03 🟠 — Statistik simpanan ahli MATI yang belum dituntut waris (nilai & volum)**
- Konteks: Hanya statistik pembayaran (RM1.52b/2020) direkod; stok tertunggak tidak [rujuk: `estate-statistics.md` Gaps].
- Hint jawapan: Angka stok menyokong RP-01 secara tepat (dan boleh jadi ukuran kejayaan program kesedaran bersama).
- Impact: Data pack; laporan.

---

## G. JPN — JABATAN PENDAFTARAN NEGARA (2 soalan)

**JN-01 🟠 — Prosedur rasmi bila TIADA MAYAT (s.18 Akta Pendaftaran Kelahiran & Kematian 1957): apakah dokumen yang JPN/mahkamah perlukan untuk sijil kematian atau pengesahan?**
- Konteks: Waris perlu deklarasi Mahkamah Tinggi (mahal/lama); panduan bertindung-tindung antara JPN & mahkamah [rujuk: `lessons-and-templates.md` Templat B; `bottlenecks.md`].
- Hint jawapan: Mohon senarai semak rasmi JPN + contoh kes lalu — kami jadikan Templat B konkrit untuk pemohon.
- Impact: Templat B (waris hilang) — dari "mekanisme umum" kepada checklist executable.

**JN-02 🟡 — Status pengesanan waris (diaspora/luar negeri): adakah JPN/carian waris rasmi wujud?**
- Konteks: Waris tak dikenali = punca kelewatan; tiada servis carian rasmi ditemui dalam repo [rujuk: `bottlenecks.md`].
- Hint jawapan: Jika tiada servis rasmi — kami dokumentasikan jurang; sistem kami boleh bantu dokumentasi pengesanan waris (bukti pertalian).
- Impact: Modul waris hilang (S2).

---

## H. PEJABAT TANAH & GALIAN — PTG (2 soalan)

**PT-01 🟠 — Fi pendaftaran pemindahan pusaka (Borang 14A) + duti setem LHDN: jadual kadar tunggal + SLA pendaftaran selepas perintah**
- Konteks: Tiada kadar bersumber tunggal dalam repo; tempoh pendaftaran tidak diterbitkan [rujuk: `gap-mission-fi-statistik.md` Gaps; `process-maps.md` laluan (f)].
- Hint jawapan: Mohon jadual fi + duti (LHDN turut dilibatkan) + SLA → enjin fi melengkapkan laluan tanah.
- Impact: Enjin Fi (laluan tanah) + jangkaan masa.

**PT-02 🟠 — PARTITION tanah pusaka: laluan rasmi & asas akta (percanggahan label MyGOV "Partition Act 1958 [Act 300]" vs Act 300 = Distribution Act — mohon pengesahan nama/akta partition sebenar)**
- Konteks: Kaedah alokasi (d) dalam modul pengagihan TERTAHAN sehingga disahkan [rujuk: `modul-pengagihan-aset.md` §2 & Gaps #1].
- Hint jawapan: Nama akta/ordinan partition yang betul + proses (mahkamah tanah? LLA?) → kami aktifkan kaedah (d) dengan citation.
- Impact: Enjin Alokasi — kaedah partition unlock.

---

## I. MAJLIS PEGUAM / TADBIR URUS UMUM (2 soalan — kedua-duanya STOPBLOCKER)

**MP-01 🔴 — Kedudukan undang-undang: platform "maklumat & sokongan proses" berhadapan peruntukan Legal Profession Act 1976 (akta guaman berlesen)?**
- Konteks: Kami memosisikan sistem sebagai maklumat pendidikan + sokongan proses/dokumen + eskalasi peguam — BUKAN nasihat guaman; kedudukan ini perlu disahkan oleh peguam/Majlis Peguam sebelum modul advisorial dilancarkan [rujuk: `journal-research-report.md` §8; D-3].
- Hint jawapan: Kami jangka (ikuti amalan penulisan wasiat/dokumen): penyediaan dokumen & maklumat awam DIBENARKAN; nasihat kes-kes-KHAS mesti di-eskalasi. Mohon panduan sempadan ("apa yang boleh/apa yang mesti merujuk peguam") — supaya disclaimers kami selaras kehendak Majlis.
- Impact: Positioning keseluruhan (D-3) + modul A1/A3 live.

**MP-02 🔴 — PDPA 2010: keperluan pematuhan bagi data waris (kanak-kanak? nenda?) & tempoh retensi rekod pusaka yang patuh?**
- Konteks: Flag sejak jurnal v0.1 — kewajiban belum disahkan [rujuk: `rangka-pembangunan-sistem.md` §7; D-6].
- Hint jawapan: Mohon panduan peguam data: (a) consent model untuk waris, (b) retention (selari had kuasa tuntut?), (c) langkah jika waris menolak data diproses. Ini menentukan rekabentuk pangkalan data (retention field design).
- Impact: Skema data (F3.a) — mesti sebelum pembinaan DB muktamad.

---

## Penutup — Cara Membuka Perbincangan (cadangan pendekatan)

1. **Bawa bukti, bukan dakwaan**: setiap soalan disertai data bercitation dari repo kami (1,277 sitasi) — tunjuk yang kami dah buwa kerja rumah (cth. isu TLS e-Faraid, konflik angka rasmi — agensi biasa HARGAI laporan teknikal sebegini).
2. **Tawar nilai balik**: analisis silang data, laporan punca penolakan, sokongan kesedaran awam, pakej permohonan lengkap kali pertama — frame engagement sebagai "mengurangkan beban agensi, bukan menambah".
3. **Kedudukan jujur**: sistem tidak menggantikan mahkamah/agensi (human-in-the-loop; hierarki kuasa) — sebut dalam pembukaan setiap pertemuan.
4. **Urutan cadangan pertemuan**: (i) JKSM (3 stopblocker konfigurasi syariah), (ii) Majlis Peguam (positioning), (iii) JKPTG (data + senarai semak), (iv) ARB (fi), kemudian KWSP/PTG/JPN.

*Disediakan Zizi, 2026-11-01 — semua soalan diwarisi daripada Gaps & PERLU SAHKAN repo (silang rujuk fail yang dinyatakan). Kemas kini bila jawapan diterima: tandakan status JAWAB di setiap soalan + naikkan status norma/jadual berkaitan daripada PERLU SAHKAN.*
