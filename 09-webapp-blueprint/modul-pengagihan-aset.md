---
title: "Modul Pengagihan Aset — Enjin Agih Berasaskan Nilaian (Faraid / Wasiat / Intestate / Arahan Mahkamah)"
project: EA-MY (Fasa 3 blueprint)
version: 1.0
updated: 2026-11-01
status: draft — cross-check IFP/CFF dalam proses (research-ifp-cfp.md)
kategori: 09-webapp-blueprint
rujukan: konsep-model-agent-human.md · modul-pematuhan-enjin-fi.md · 01-legal-framework/ · 06-case-studies/lessons-and-templates.md
---

# Modul Pengagihan Aset (Distribution & Allocation Engine)

## 0. Prinsip Asas — "Tiada Tindakan Tanpa Rujukan Sahih"

1. **Deterministik + berpuncakan rujukan**: setiap langkah pengagihan mesti dipetakan kepada **satu daripada tiga lapis rujukan**: (i) **statutori** (akta/seksyen/warta), (ii) **autoriti hukum** (penghakiman; fatwa/enakmen bagi Muslim), (iii) **framework profesional terakreditasi** (IFP/CFP) — lapisan ketiga sebagai *pengesahan prosedur*, BUKAN asas kuasa. **Tiada prosedur "dicipta sendiri" (purposely created)** — apa yang tiada rujukan → tidak dilaksana sehingga disahkan panel + dicatat sebagai cadangan (proposal), bukan tindakan.
2. **Hierarki kuasa agihan** (bawah): sistem REKOD & LAKSANA arahan — tidak menafsir semula keputusan mahkamah.
3. **Berasaskan nilaian**: pengagihan fizikal (in-kind) diselesaikan berasaskan nilai aset — pecahan abstrak faraid/Act 300 → alokasi aset sebenar.
4. **Rekonsiliasi total**: jumlah diagih mesti = baki lejar pusaka (modul fi §B6) — pintu S9 menyekat rumusan tanpa seimbang.
5. **Konsensus berpasangan**: setiap alokasi lulus pintu (Q&A konsensus) — human partner mengesahkan; pengecualian → Exception Register.

## 1. Hierarki Sumber Kuasa Pengagihan

| Tahap | Sumber | Peranan sistem |
|---|---|---|
| 1 (tertinggi) | **Perintah mahkamah / agensi** (perintah pembahagian pusaka kecil — Akta 98; geran probat/SKM — Act 97; keputusan faraid/sepencarian Mahkamah Syariah — Akta 505) | Rekod penuh → laksana mengikut arahan; tiada tafsiran semula; percanggahan dengan kiraan sistem → **flag & rujuk** (mahkamah menang) |
| 2 | **Wasiat** dalam had undang-undang (bukan Islam: Wills Act 1959 — formaliti s.5 terverifikasi; Islam: ≤1/3 harta bersih & bukan waris tanpa persetujuan — s.26 Enakmen Wasiat Selangor 1999 sebagai contoh negeri) | Enjin baca wasiat → agihan legasi dalam had; N-W-01/N-WC-01 pra-semak |
| 3 | **Skema statutori intestate**: Islam = **faraid** (12 ashab al-furud + asabah + 'aul/radd + Baitulmal); bukan Islam = **Distribution Act 1958** s.4/s.6(1) (tidak terpakai kepada Muslim, s.1(2)) | Enjin kiraan A5 (deterministik + test vectors) |
| 0 (pra-pusaka) | **Hibah / penama (wasi)** — harta yang TERKELUAR daripada pusaka | Dikenal pasti & disahkan PADA S1–S3 supaya tidak diagih salah (pelajaran kes Divyyaa Machap [2024] — penama KWSP bukan pusaka wasiat; kes Noridah — penama Muslim = wasi agih faraid) |

**Corak pelaksanaan:** Lapis 0 disahkan dahulu (pengecualian harta), kemudian hutang/kos jenazah/perbelanjaan pentadbiran (N-EX-01), barulah lapis 1→2→3 digunakan kepada BAKI.

## 2. Saluran Pengagihan per Kategori Harta (semua rujukan dari repo)

| Kategori harta | Kaedah agihan | Rujukan statutori terverifikasi (repo) |
|---|---|---|
| Wang (bank/WTD/KWSP/takaful-insurans) | Agih tunai ikut skema; KWSP/insurans Muslim: **penama = wasi** → agih faraid; bukan Islam: trust policy (Jadual 10 FSA 2013) luar pusaka | Akta 370 s.13 (eGUMIS); Akta KWSP 1991 s.54(1A) + Peraturan EPF; FSA 2013 Jadual 10; IFSA 2013 |
| Tanah/rumah | (a) **Pemilikan bersama (in-kind)** mengikut pecahan — pendaftaran bersebelahan; (b) **jualan** → agih tunai; (c) **penebusan antara waris (buyout)** berasaskan nilai; (d) **pemisahan (partition)** tanah boleh bahagi | NLC: pendaftaran pemegang perwakilan/pemindahan selepas geran (s.346 + Borang 14A — process-maps); pemilikan bersama: amalan pendaftaran PTG; partition: **PERLU SAHKAN** (percanggahan label MyGOV "Partition Act 1958 [Act 300]" vs Act 300 = Distribution — gaps stream 4) |
| Syer syikat (listed) | **Transmission** kepada waris → keputusan waris: pegang bersama / jual | Companies Act 2016 s.109 (geran sebagai bukti cukup s.109(4); pendaftaran 60 hari) |
| Aset perniagaan | Penerusan pemilikan / jualan / penswastaan hasil — ikut perintah & persetujuan waris | flag: mekanisme perlu kelulusan berpasangan (tiada skema automatik) |
| Kenderaan | Pindah milik JPJ selepas geran/perintah | process-maps (JPJ) |

## 3. Enjin Alokasi Bersepara (fractional → physical) — aliran deterministik

```
STEP 1 — INVENTORI + NILAI: setiap aset → nilai (NILAI_RASMI / ANGGARAN / TERJUAL — modul fi §B5)
STEP 2 — MATRIKS HAK: aset × waris × pecahan (dari A5 / perintah / wasiat)
STEP 3 — KAEDAH ALOKASI per aset (dipilih berasaskan syarat, BUKAN ciptaan):
   (a) in-kind → pecahan pemilikan bersama direkod (sesuai: tanah, rumah kekal)
   (b) jualan → hasil tunai diagih ikut pecahan (sesuai: aset susah diagih/kos penjagaan tinggi)
   (c) buyout antara waris → berdasarkan NILAI_RASMI + persetujuan SEMUA waris (rekod: nilai, pembayar, terima)
   (d) partition (tanah) → ikut proses rasmi PTG/mahkamah (PERLU SAHKAN laluan)
STEP 4 — PENYELESAIAN PECAHAN (deterministik, telus):
   - pecahan tak boleh bahagi fizikal (cth. 1/8 rumah) → pemilikan bersama berperingkat % (title share), BUKAN pembundaran senyap
   - baki tunai kecil (< RM minimum ditetapkan pintu, dicatat dasar) → dibundarkan dengan dasar terbuka (contoh: ke baki 0 ke waris asabah terbesar) — DASAR mesti diluluskan panel & dipaparkan dalam penyata — bukan sorok
STEP 5 — PENYATA AGIHAN: matriks penuh (aset | waris | pecahan | nilai | kaedah | rujukan) — disemak kaitan ke lejar (DIBAYAR/DIAGIH)
```

**Kes khas (semua bermula daripada repo/kes):**
- **Waris hilang/tidak dikenali** → bahagian TIDAK diagih sehingga mekanisme Templat B selesai (anggapan kematian s.108 Akta Bukti — 7 tahun; deklarasi Mahkamah Tinggi); pilihan pemegangan (escrow via pentadbir/ARB) → **PERLU SAHKAN mekanisme statutori** — cadangan, bukan tindakan, sehingga disahkan
- **Waris bawah umur** → bahagian disimpan/taruh dengan pentadbir/trustee sehingga majoriti — mekanisme (syariah trust/hibah amanah/Peraturan?) → **PERLU SAHKAN standard** — sistem tahan bahagian & flag
- **Radd ('lebihan balik') & 'aul** — dikira deterministik oleh A5 (kaedah dalam syariah-law.md); justifikasi langkah dipapar
- **Baitulmal** sebagai pewaris akhir (tiada waris — amalan Malaysia, rujuk syariah-law.md)
- **Pertikaian alokasi** → pintu Q&A → eskalasi → mahkamah; sistem freeze bahagian dipertikaikan sahaja, bukan seluruh kes

## 4. Cross-Check Framework Profesional (IFP / CFP) — lapisan pengesahan

**Tujuan (dinyatakan jujur):** IFP (Islamic Financial Planning — silibus terakreditasi, cth. IBFIM) & CFP (FPAM Malaysia — modul estate planning) menyediakan **standard amalan profesional** untuk proses perancangan & pentadbiran harta. Kita guna mereka untuk **mengesahkan prosedur kita selari dengan amalan profesional** — memberi keyakinan tambahan kepada mahkamah/agensi/auditor bahawa langkah kita bukan reka-sendiri. **Kedudukan undang-undang:** framework profesional ≠ asas kuasa; asas kuasa kekal statutori (Bahagian 1). Jika konflik — statutori menang.

**Struktur pengesahan (dua arah):**
| Arah | Soalan | Hasil dicatat dalam |
|---|---|---|
| Proses kita → IFP/CFP | Adakah setiap langkah agihan kita konsisten dengan langkah dalam framework profesional? | Jadual silang (research-ifp-cfp.md → integrate sini) |
| IFP/CFP → kita | Adakah komponen profesional yang kita tertinggal? (cth. semakan pasca-agihan/post-distribution review, pelan kontingensi) | Senarai cadangan (proposal — menunggu panel) |

**✅ KEPUTUSAN CROSS-CHECK (selesai 2026-11-01 — `research-ifp-cfp.md`, 20 sumber bercitation):**

**Komponen prosedur kita yang DISAHKAN silang oleh framework profesional (lapisan pengesahan tercapai):**
1. Inventori aset & liabiliti dahulu (IFP EGADIM-G · CFP Step 2 · ARB · UiTM) — selari STEP 1 enjin alokasi
2. Penjelasan hutang sebelum pengagihan (UTM/UiTM · CFP Topic 16 · PAA) — selari N-EX-01
3. **Turutan fiqh pengagihan**: asing hibah/amanah/waqf → kebumian → hutang → wasiat ≤1/3 → sepencarian → faraid (UTM 6 komponen · UiTM 5 langkah) — mengesahkan turutan kiraan A5
4. Sijil faraid prasyarat saluran Muslim (IIUM · Akta 505 s.50) — selari N-PK-01
5. Instrumen semasa hidup menentukan saluran (3 kaedah Kamarudin · ARB · CFP Topics 13–14) — selari Lapis 0
6. Tugas pentadbir: kutip–jelaskan–agih–pindah (CFP Topic 16 = ARB = PAA)
7. Penama Muslim = wasi (fatwa MKI · modul takaful IFP sejajar) — selari laluan (e)
8. Kelengkapan dokumen = faktor kelancaran utama — selari pintu S2
9. Proses 6-langkah EGADIM (IFP, adaptasi FPSB) boleh jadi pembalut (wrapper) modul perancangan pra-kematian webapp

**Komponen yang kekal berasaskan statutori sahaja** (IFP/CFP tidak liputi; asas kuasa tidak berubah): dokumen & fi setiap saluran (Borang A/MyLAND, RM160/RM16, bon s.35 PAA, eGUMIS, NLC s.346, s.109 CA 2016, fi ARB PTCA); ambang kuasa (RM5j A1643; RM600k s.17(1)); dwi-jurisdiction *Latifah* twin-track; tempoh statutori. *Nota penting: kertas akademik IIUM (2020) masih guna ambang RM600,000 usang (kini RM5 juta) — membuktikan statut mesti kekal rujukan utama; framework hanya lapisan pengesahan.*

**Komponen BERBEZA (dinyatakan jujur):** orientasi masa — IFP/CFP = perancangan **pra-kematian** advisory; sistem kita = pentadbiran **pasca-kematian**. Faraid: IFP pegang mandat fiqh; PPKP benar muafakat — sistem ikut perintah agensi.

**Komponen jurang IFP/CFP ada yang kita belum ada — status CADANGAN (menunggu panel, bukan tindakan):**
(a) **langkah tuntutan sepencarian eksplisit** dalam aliran pintu (ada dalam repo ilmu — syariah-law & kes S4 cross-examination — cadangan: jadikan sub-langkah S3 wajib bagi kes Muslim berpasangan); (b) **zakat/hutang akhirat** sebagai kategori lejar pusaka sebelum faraid (cadangan kemas kini `modul-pematuhan-enjin-fi.md`); (c) **loop monitoring pasca-agihan** (EGADIM-M — selari pintu S9/S10; cadangan peringkat semakan tertutup); (d) POA/perancangan kekurangan upaya — nyatakan batasan produk; (e) business succession — nota keupayaan; (f) kedalaman instrumen trust (waris bawah umur); (g) **pra-skrin likuiditi estet** (adakah tunai cukup untuk hutang & belanja? — cadangan modul nasihat); (h) kod etika FPAM/IBFIM sebagai benchmark tatakelola model pasangan.

## 5. Kaitan dengan Model Pasangan & Modul Sedia Ada

| Pintu | Peranan modul agihan |
|---|---|
| S1–S3 | Kenal pasti hibah/penama (lapis 0) + nilai awal → matriks hak draf |
| S4 | A5 kira pecahan (faraid/Act 300/wasiat) — **pintu: kiraan semak human** |
| S6 | **Pelan Agihan Aset** (kaedah per aset + Penyata Agihan draf) masuk kertas kes — **pintu: lulus pasangan + peguam/pakar** |
| S7 | Perintah/geran agensi → sistem rekod (hierarki tahap 1 menang jika berbeza) |
| S8 | Pelaksanaan agihan (in-kind/buyout/jual/transmission) — **setiap pindahan: sign-off human + resit/daftar rujukan** |
| S9 | Penyata Agihan muktamad + rekonsiliasi lejar (=0) → penyata akaun pusaka |

**Enjin fi ↔ agihan:** nilai aset yang sama digunakan kedua-dua kiraan fi (peratusan fi ikut nilai) & alokasi — SATU sumber nilai (tiada nilai berbeza-beza antara modul — konsistensi diaudit).

## 6. Audit & Rintangan Kontes (contest-resistance)

Setiap baris Penyata Agihan membawa: `aset_id | waris | pecahan (sumber: perintah/wasiat/A5) | nilai (sumber nilai + tarikh) | kaedah alokasi + rujukan | kelulusan (pintu, pasangan)`. Auditor boleh **rekomputasi** (input sama → pecahan & nilai sama). Mana-mana baris tanpa rujukan 3-lapis (statutori/autoriti/framework) = **kecacatan audit** — dihalang pada S6. Penebukan teori: pengagihan yang boleh ditafsir "cipta sendiri" (cth. dasar pembundaran, buyout) DIPAPARKAN sebagai dasar terbuka berasaskan persetujuan waris + kelulusan panel — bukan keputusan tersembunyi sistem.

## 7. Jurang & Status Kebenaran (Gaps)

1. **Partition tanah** — laluan rasmi & asas akta PERLU SAHKAN (percanggahan label MyGOV dikenal pasti Fasa 1); sehingga disahkan → kaedah (d) hanya cadangan.
2. **Mekanisme pegangan bahagian waris hilang** (escrow) & **waris bawah umur** (trustee standard) — PERLU SAHKAN dengan sumber statutori/pakar; sementara: tahan + flag (tiada agihan tanpa asas).
3. **Tarikh nilai** (valuation date) untuk agihan — tarikh kematian vs tarikh agihan: amalan perlu dirujuk (perbezaan fi/kaedah penilaian) — flag untuk panel; jurnal tidak menetapkan sendiri.
4. Dasar pembundaran baki — dicadangkan, menunggu kelulusan panel (Pintu S6 memaparkan dasar aktif).
5. Skim agihan aset perniagaan (penerusan/penswastaan) tiada skema automatik — wajib pintu kelulusan + rujukan undang-undang perniagaan (luar skop repo semasa).
6. ~~Jadual silang IFP/CFP~~ ✅ SELESAI — `research-ifp-cfp.md` (20 sumber): 9 komponen disahkan silang; komponen statutori-sahaja dikenal pasti; 8 komponen jurang dicatat sebagai CADANGAN (a)–(h) di §4 — menunggu kelulusan panel sebelum dilaksana.

*Disediakan Zizi, 2026-11-01 — melengkapi keluarga modul: konsep-model (pintu) · enjin fi & kewangan (nilai+lejar) · pematuhan & audit (rujukan 3-lapis). Semua angka/seksyen diwarisi daripada fail repo bercitation.*
