---
title: "Konsep Model — Pasangan Agent–Human dengan Semakan Berperingkat (Paired Stage-Gate Check & Balance)"
project: EA-MY (Fasa 3 blueprint)
version: 1.0
updated: 2026-10-31
status: draft — untuk semakan pemilik projek
kategori: 09-webapp-blueprint
rujukan: journal-research-report.md §6 · cross-examination/00-ringkasan-perbandingan.md · process-maps.md
---

# Konsep Model Webapp: Pasangan Agent–Human (Check & Balance)

## 1. Prinsip Asas (8)

| # | Prinsip | Maksud operasi |
|---|---|---|
| P1 | **Agent = KATALIS** | Agent mempercepatkan: pengumpulan dokumen/data, analisis rekod, penyediaan keputusan/hujah berasaskan justifikasi perundangan (syariah/civil), penyediaan kertas kerja kes & material siasatan. Agent TIDAK memutuskan |
| P2 | **PASANGAN (Pairing)** | Setiap peringkat = satu pasangan: agent melaksanakan + human partner menilai. Tiada peringkat berjalan sebulat agent |
| P3 | **PINTU SEMAKAN (Stage-Gate)** | Semua output agent WAJIB direview & disahkan human partner SEBELUM peringkat seterusnya bermula. Tiada lulus = tiada maju |
| P4 | **KESAHIHAN INPUT** | Human mengesahkan kesahihan maklumat/data input (dokumen asal, identiti, kenyataan waris); agent tak berasaskan andaian |
| P5 | **Q&A KONSENSUS** | Agent ↔ human berinteraksi soal-jawab berstruktur untuk mencapai keputusan sebulat suara sebelum tindakan diluluskan |
| P6 | **RANTAI GABUNGAN** | Peringkat dilulus oleh gabungan agent+human; peringkat seterusnya dijaga pasangan lain (sistem tiada titik tunggal kawalan) |
| P7 | **PENGESAHAN MAHKAMAH** | Di penghujung: laporan lengkap + kesimpulan/rumusan kes dicompile untuk pengesahan mahkamah/agensi SEBELUM dimaklumkan kepada pemohon |
| P8 | **GUARDRAILS STATUTORI** | Setiap cadangan/tindakan dipetakan kepada asas statutori terverifikasi (akta/seksyen/peraturan/penghakiman); item PERLU SAHKAN DISEKAT daripada menjadi asas tindakan; diskresi kehakiman terpelihara (cross-examination §5) |

**Asas pembuktian (dari cross-examination 14 kes):** agent cemerlang ex-ante & deterministik (verdict YA); penilaian kredibiliti, bukti lisan & khilaf kekal manusia (SEBAHAGIAN); isu perlembagaan keluar dari skop (TIDAK). Model pasangan ini direka tepat di atas sempadan tersebut.

---

## 2. Struktur Peranan

### 2.1 Agent (katalis — dari jurnal §6.2)
A1 Legal (civil) · A2 Syariah · A3 EA/Fiduciary · A4 Analis Kes (preseden) · A5 Enjin Kiraan (deterministik) · A6 Orkestrator Proses · A7 Dokumen · A8 Pematuhan Deontik (menyemak SEMUA cadangan agent lain terhadap norma sebelum sampai ke human).

### 2.2 Human Partner (penilai & pengesah)
| Peranan | Tanggungjawab utama | Padanan peringkat |
|---|---|---|
| **Petugas Kes** (case officer) | Verifikasi dokumen/identiti, koordinasi, tanda lulus gate operasi | S1, S2, S8 |
| **Peguam / Penasihat Legal** | Semak nasihat & hujah civil | S3, S6 |
| **Pakar Syariah** | Semak faraid/hibah/wasiat/sepencarian, khilaf | S3, S4 |
| **Penyelia Kanan** | Pemutus kebuntuan (deadlock), kawalan mutu | semua (eskalasi) |
| **Pegawai Agensi** (PPKP/JKSM/JPN/bank) | Kuasa rasmi luaran (perintah, sijil, geran) | S7, S9 |
| **Mahkamah** | Pengesahan muktamad rumusan & perintah | S9 |
| **Pemohon / Penfail** | Sumber input, jawab Q&A, terima hasil | S0, S10 |

### 2.3 Matriks pemeriksaan (siapa semak siapa)
- **A8 → semua agent**: setiap cadangan agent lain mesti lulus semakan norma deontik dahulu (guardrail dalaman).
- **Human partner → agent**: lulus/tolak/kemaskini output pada setiap pintu.
- **Penyelia Kanan → pasangan**: semakan rawak (spot-check) + pemutus kebuntuan.
- **Audit trail → semua**: setiap tindakan (agent & human) dicatat tanpa boleh diubah.

---

## 3. Kitaran Hidup Kes — 11 Peringkat × Pintu Semakan

> Aliran penuh dari kes difail pemohon sehingga keputusan disampaikan. Setiap peringkat: **Agent (kumpul/semak/analisis/sediakan)** → **Human Partner (nilai/sahkan)** → **PINTU** (lulus → peringkat seterusnya; tolak → kembali dengan alasan; kebuntuan → eskalasi).

| Peringkat | Agent buat (katalis) | Human Partner buat | PINTU — syarat lulus | Asas statutori (contoh terverifikasi) |
|---|---|---|---|---|
| **S0 — Pendaftaran & Intake** | A3: wizard klasifikasi awal (Muslim/bukan; wasiat/tiada; jenis harta; anggaran nilai) | Pemohon: isi & muat naik; Petugas: verifikasi identiti & dokumen asal | Identiti disahkan; dokumen asal sah | KYC; Akta Pendaftaran (dokumen rasmi) |
| **S1 — Verifikasi & Klasifikasi** | A3+A1/A2: cadangan laluan (pusaka ringkas ARB ≤RM600k / pusaka kecil ≤RM5j / Mahkamah Tinggi >RM5j) + sijil faraid diperlukan? (N-PK-01) + **A5-Fi: anggaran kos & fi laluan (jadual berversi bercitation, label ANGGARAN)** | Petugas: sahkan klasifikasi; tanya Q&A jika data bercanggah | Laluan & bidang kuasa disepakati; anggaran fi dipaparkan | Act 532 s.17(1); Akta 98+A1643; Act 97; Akta 505 s.50; jadual fi (P.U.(A) 194/2024 dsb.) |
| **S2 — Pengumpulan & Pengesahan Dokumen** | A6: jana senarai semak dokumen ikut laluan; A7: semak kelengkapan & flag percanggahan | Petugas: **sahkan kesahihan setiap dokumen** (asal vs salinan; waris dikenal pasti) | Senarai dokumen 100% SAH & lengkap | Borang A; senarai semak JBG; NLC (geran) |
| **S3 — Analisis Kes & Nasihat** | A1/A2: nasihat berjustifikasi + citation; A4: preseden & risiko (Templat A–F) | Peguam/Pakar Syariah: semak hujah; Q&A konsensus; tolak jika justifikasi lemah | Nasihat disemak pakar & meyakinkan | Latifah twin-track; fatwa MKI; enakmen negeri |
| **S4 — Pengiraan Bahagian** | A5: faraid/hibah/wasiat/Act 300 — deterministik + justifikasi langkah-demi-langkah + test vectors | Pakar Syariah/Petugas: **kiraan semak manual** (sampel langkah); khilaf → panel | Kiraan disemak & tiada bantahan matematik | Faraid (Al-Nisa' 11/12/176); Akta 300 s.6(1); Akta 303 s.122 |
| **S5 — Semakan Norma & Pematuhan** | A8: nilai semua langkah terhadap Perpustakaan Norma (WAJIB/DIBENAR/DILARANG); flag pelanggaran & CTD | Petugas/Penyelia: sahkan keputusan pematuhan; kenal pasti keperluan eskalasi | Sifar pelanggaran kritikal; semua norma lulus atau CTD diaktifkan | Perpustakaan Norma (bercitation) |
| **S6 — Kertas Kes & Draf Keputusan/Hujah** | A4+A7: compile kertas kerja kes siasatan: kronologi, inventori harta, pengiraan, nasihat, justifikasi perundangan, draf perintah/permohonan | Peguam/Pakar/Petugas: semak & lulus kertas; tanda tangan draf | Kertas kes lengkap, berjustifikasi, bercitation | Senarai aset Act 97 s.30; format agensi |
| **S7 — Serahan & Pengesahan Agensi/Mahkamah** | A6: serahan (MyLAND/kaunter/e-filing peguam); jejak status | Petugas/Peguam: serah rasmi; **Pegawai Agensi: kuasa luaran memproses** (perintah pembahagian / geran) | Perintah/geran/sijil diterbitkan agensi | Akta 98 (perintah); Act 97 (geran); Akta 505 s.50 (sijil faraid) |
| **S8 — Pelaksanaan & Pemantauan** | A6: pecahkan arahan → tugas (pindahan tanah NLC, WTD eGUMIS, KWSP, syer); A7: sediakan setiap dokumen; A8: pra-semak setiap tugas | Petugas + pihak penerima (bank/PTG/KWSP): laksanakan; human sign-off setiap tindakan | Setiap tugas selesai & disahkan; akaun/tajuk/pindahan sah | NLC s.346 + Borang 14A; Akta 370 s.13; Akta KWSP s.54(1A) |
| **S9 — Laporan Akhir & Rumusan Kes** | A4+A6: **compile laporan lengkap** — kronologi, tindakan, keputusan, pengiraan akhir, pengagihan, audit trail ringkas + rumusan + **A5-Fi: Penyata Akaun Pusaka (DITERIMA−DIBAYAR−DIAGIH = 0)** | Petugas/Penyelia/Pegawai Kewangan: semak; **Mahkamah/agensi: PENGESAHAN rumusan** (P2/P7) | Lejar pusaka seimbang (rekonsiliasi lulus) & rumusan DISAHKAN mahkamah/agensi | Kuasa kehakiman (muktamad); tugas akaun pentadbir (duty to account) |
| **S10 — Penyampaian & Penutupan** | A6: jana pakej penyampaian (salinan disahkan, jadual pengagihan, penutupan kes); notifikasi | Petugas: sahkan terima oleh pemohon; arkib | Pemohon menerima keputusan lengkap; kes ditutup | — |

**Ciri penting:** peringkat S7 & S9 — kuasa muktamad DI LUAR sistem (agensi/mahkamah); sistem tidak pernah "meluluskan" bagi pihak mereka — sistem menyediakan, menjejak & merekod.

---

## 4. Protokol Q&A Konsensus (P5)

```
UMAN → AGENT: cadangan + JUSTIFIKASI + citation statutori
     ↓
HUMAN: soal / bantah (berstruktur: "tanya bukti" | "tanya alternatif" | "bantah dengan fakta")
     ↓
AGENT: jawab dengan bukti dari repo / recomputes / revised cadangan
     ↓
┌─ SEBULAT SUARA? ─ YA → PINTU LULUS (dicatat: persetujuan kedua-dua pihak + alasan)
│                └ TIDAK → pusingan 2 (maks 2 pusingan)
│                         └ masih kebuntuan → ESKALASI berperingkat:
│                           Penyelia Kanan → Pakar luar (peguam/mufti/pegawai agensi)
│                           → rujuk agensi berautoriti. Keputusan eskalasi DIRAKAM dalam audit trail.
└─ Setiap pusingan Q&A direkod penuh (soalan, jawaban, citation, hasil) — asas audit & pembelajaran sistem
```

**Peraturan konsensus:** (a) agent WAJIB kemukakan citation bagi setiap dakwaan; tanpa citation → cadangan ditolak automatik; (b) human WAJIB beri alasan bertulis bagi setiap penolakan (input pembelajaran); (c) keputusan sebulat suara direkod dengan nama + peranan + masa + hash artifak yang diluluskan.

---

## 5. Audit Trail di Aras Proses

Setiap PINTU merakam satu **rekod pintu (gate record)**: `peringkat | pasangan (agent+human) | input hash | output hash | asas statutori yang dipetakan | transkrip Q&A (rujukan) | keputusan (lulus/tolak/eskalasi) | masa | tandatangan digital`. Rantai hash menghubungkan rekod pintu berturutan → sebarang pengubahan silam boleh dikesan (tamper-evident). Susunan atur teknikal penuh: `rangka-pembangunan-sistem.md` §6.

---

## 6. Contoh Aliran Nyata (Muslim, pusaka kecil RM1.2j, tanpa wasiat) — naratif padat

S0 pemohon daftar, muat naik sijil kematian & MYKAD → S1 A3 cadang laluan PPKP (≤RM5j) + N-PK-01 → sijil faraid dulu; Petugas sahkan → S2 A6 jana senarai (Borang A, senarai aset, sijil faraid, MYKAD semua waris); Petugas sahkan dokumen asal → S3 A2 nasihat faraid & risiko (A4: Templat A — tiada hibah dicabar); Pakar Syariah semak → S4 A5 kira: balu 1/8, baki anak (asabah) + justifikasi; Pakar buat kiraan semak → S5 A8: N-PK-01 ✓ N-EX-01 ✓ (hutang dulu); Penyelia sahkan → S6 kertas kes lengkap di-compile; Peguam/Petugas lulus & tandatangan → S7 serahan MyLAND/kaunter; **PPKP proses & keluarkan perintah pembahagian** (mesyuarat waris) → S8 pelaksanaan: pindahan tanah (Borang 14A, NLC s.346), pengeluaran KWSP oleh penama-wasi (agih ikut faraid, A8 audit); setiap tugas human sign-off → S9 laporan penuh + rumusan → **disahkan** → S10 pakej penyampaian kepada pemohon; kes ditutup, semua rekod diarkib.

---

## 7. Pemetaan kepada Hasil Cross-Examination

| Penemuan cross-examination | Reka bentuk dalam model ini |
|---|---|
| Klasifikasi awal mencegah salah-laluan (C1/C5/C6) | S1 gate klasifikasi + human sahkan |
| Saman penama sia-sia boleh dicegah (C3/C4/S3) | S8: A8 audit agihan penama sebelum pembayaran |
| Kepastian hukum awal termasuk berita buruk (C6) | S3 nasihat + Q&A dengan pemohon turut dibenarkan |
| Kiraan deterministik > manual (S7) | S4 A5 + kiraan semak human |
| Status kes tunggal (RP-06) | S2–S10 satu kes-fail, semua pihak nampak status pintu |
| Khilaf & kredibiliti kekal manusia (S2–S6) | Pakar syariah & penyelia dalam pasukan; eskalasi |
| Perlembagaan di luar skop (C5 Moorthy) | Sistem mengesan & eskalasi isu forum — tidak menyelesaikan |

---

## 8. Had & Gaps

1. Model ini masih KONSEP — belum diuji prototype; perlu walkthrough atas 3 kes simulasi (Fasa 3.6 pilot).
2. Peranan "Pegawai Agensi" & "Mahkamah" di luar kawalan sistem — S7/S9 bergantung kerjasama/konfigurasi luaran (MVP: sistem sediakan pakej + jejak, serahan manual human).
3. Tempoh agensi tidak dipendekkan oleh sistem (cross-examination S7) — KPI jujur: kelengkapan & ketepatan, bukan tempoh agensi.
4. Kuasa digital signature & PDPA perlu pengesahan statutori (flag kekal sehingga disemak).
5. Panel pakar syariah & peguam perlu dilantik sebenar sebelum pilot (keputusan D-5 pemilik projek).

*Disediakan Zizi, 2026-10-31 — untuk semakan pemilik projek bersama jurnal v2.1 (D-1/D-2) dan ringkasan cross-examination.*
