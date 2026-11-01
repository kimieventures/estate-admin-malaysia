---
title: "Modul Penentuan Faraid — Enjin Faraid Berlapis & Pengiraan Pecahan Deterministik"
project: EA-MY (Fasa 3 blueprint)
version: 1.0
updated: 2026-11-01
status: peraturan teknikal DIINTEGRASIKAN (01-legal-framework/research-faraid-berlapis.md — munasakhat, musyahamah MKI-83, mahjub, 'aul/radd, wasiat wajibah 5 negeri, waris khas)
kategori: 09-webapp-blueprint
rujukan: modul-pengagihan-aset.md (enjin agih) · modul-pematuhan-enjin-fi.md (nilai/lejar) · 01-legal-framework/syariah-law.md §2 (faraid asas) · research-ifp-cfp.md (turutan fiqh disahkan)
---

# Modul Penentuan Faraid (Faraid Determination Engine)

> Jawapan kepada isu: **kelewatan keputusan & pengeluaran sijil faraid disebabkan proses penentuan & pengiraan faraid, terutama kes FARAID BERLAPIS**. Punca ini telah pun terverifikasi dalam repo: "kematian berlapis (layered deaths)" disenaraikan antara punca kelewatan rasmi [Sumber: Bernama 29-01-2026 — dalam `05-statistics/estate-statistics.md`]. Modul ini menyediakan penyelesaian berstruktur untuk penentuan penerima faraid/hibah/wasiat dan pengiraan pembahagian pecahan hingga **pengagihan akhir**.

## 0. Prinsip (mewarisi semua blueprint)

Deterministik (bukan LLM untuk kiraan) · rujukan 3-lapis (statutori/autoriti hukum/framework profesional — turutan fiqh pengagihan DISAHKAN cross-check IFP/CFP: *asing hibah → kebumian → hutang → wasiat ≤1/3 → sepencarian → faraid*) · **enijn MENYEDIAKAN kiraan & dokumen untuk permohonan sijil faraid — Mahkamah Syariah kekal pihak yang MENGELUARKAN sijil** (guardrail: sistem tidak pernah mengeluarkan sijil, hanya memastikan permohonan lengkap & kiraan boleh diaudit supaya sijil keluar lebih cepat) · khilaf syariah → panel pakar (bukan automatik).

## 1. Isu Faraid yang Dikenal Pasti (asas: repo + research berjalan)

| # | Isu | Status bukti | Kesan |
|---|---|---|---|
| F1 | **Kematian berlapis = MUNASAKHAT** (✅ terverifikasi: MAIS E-FARAID §8) — bahagian waris yang mati selepas si mati sebelum pembahagian VESTED lalu diwarisi warisnya; **tiada had lapisan** — kes rujukan AL-KAFI #1021 (Pejabat Mufti WP): **8 lapisan, jami'ah 422,400, 19 penerima akhir** | ✅ | Kiraan bertingkat manual — jami'ah ratus ribu mustahil dikira tangan tanpa ralat |
| F2 | **Verifikasi silsilah waris manual** — pengenalan waris bergantung dokumen (sijil kelahiran/perkahwinan) & kenyataan; tidak berstruktur | amalan PPKP/JKSM (repo: process-maps) | Semakan berulang; ralat penama waris |
| F3 | **Kiraan pecahan** — ✅ mekanik terverifikasi: 'aul (6→10, 12→17, 24→27), radd, **7 asal masalah** (2,3,4,6,8,12,24; +18/36 datuk), jami'ah melalui **3 hubungan** (inqisam/tamathul, tawafuq, tabayun) — contoh penuh MAIS, boleh dikod terus. ⚠️ amalan MAIS: baki ke **Baitulmal** (bukan radd mutaakhirin) → konfigurasi negeri = keputusan panel | ✅ mekanik / ⚠️ konfigurasi | Ralat manual; kitab & kalkulator berbeza amalan |
| F4 | **Waris khas** — ✅ terverifikasi: anak luar nikah mewarisi **melalui ibu sahaja** (AL-KAFI #2002); mualaf/berbeza agama tidak saling mewarisi & tidak menghijab (Re Emily 1996, Re Zarina 2002, Re Zaiton 1989 → Baitulmal); al-haml 2 syarat + ihtiyat (AL-KAFI #729); **mafqud**: dikira hidup pada hartanya, mati pada harta orang lain — **bahagian DITAHAN** (Irsyad 341) | ✅ | Pertikaian & kelewatan penetapan |
| F5 | **Pengecualian waris (mahjub/hijab)** — ✅ senarai penuh bercitation (kitab Syafi'i): 2 jenis (bi al-wasf / bi al-syakhs), hirman vs nuqsan, **6 waris tidak pernah terdinding hirman** (bapa, ibu, anak lelaki, anak perempuan, suami, isteri); cucu terdinding oleh anak lelaki (ijmak); saudara seibu pengecualian dsb. | ✅ | Waris tersenarai salah → sijil ditolak/ulang |
| F6 | **Wasiat wajibah** — ✅ DIENAKMENKAN di 5 negeri disahkan: Selangor (1999, p.2016), Pahang (2017), Perak (2023), Melaka (2005), N. Sembilan (2004); asas MKI Ke-83 (2008) + siyasah syar'iyyah (kes Akmar lwn ARB, MTS Selangor 2012); liputan cucu BERBEZA antara negeri | ✅ 5 negeri / ⚠️ negeri lain | Ketaksaan antara negeri — konfigurasi negeri wajib |
| F7 | **e-Faraid JKSM tersahan secara teknikal** — server HIDUP tetapi sijil TLS `*.jwp.gov.my` tidak sepadan hos → pelayar sekat capaian (disemak langsung 2026-11-01); **MyLAND JKPTG single-layer TANPA medan munasakhat** (disemak terus); K-Faraid MAIS pendidikan sahaja; sokongan berlapis hanya kalkulator swasta BERBAYAR | ✅ disemak sendiri | Jurang kejuruteraan TERBUKTI — enjin kita yang isi |
| F8 | Interaksi lapisan harta: sepencarian/hibah/penama/wasiat mesti diselesaikan DALAM TURUTAN BETUL sebelum faraid | ✅ turutan DISAHKAN IFP/CFP (research-ifp-cfp.md) | Agihan awal salah (kes Divyyaa — penama KWSP bukan pusaka wasiat) |

## 2. Enjin Penentuan Faraid — 5 Lapisan Penyelesaian

```
LAPIS 1 — INPUT SILSILAH BERSTRUKTUR (family tree)
  Waris dimasukkan sebagai GRAF keluarga (bukan teks bebas): pasangan/zuriat/ibu-bapa/adik-beradik
  Setiap nod: status hidup/mati + tarikh kematian (KRITIKAL utk berlapis/musyahamah) + dokumen sokongan
  Validasi automatik: dokumen wajib per waris; percanggahan tarikh diperlihat; waris bawah umur/hilang di-flag

LAPIS 2 — PENENTUAN WARIS DETERMINISTIK (rule engine)
  Peraturan masuk/keluar waris (ashab al-furud / asabah / mahjub — senarai peraturan bercitation
  dari research-faraid-berlapis.md; peraturan PERLU SAHKAN DISEKAT daripada produksi)
  Output: senarai waris sah peringkat 1 + kedudukan khas (waris khas F4) — dilabelkan

LAPIS 3 — ENJIN PECAHAN (fraction arithmetic — KPK/asal masalah, 'aul, radd)
  Aritmetik nombor munasabah TEPAT (tiada floating point); asal masalah dikira; penyesuaian 'aul/radd
  Output: jadual pecahan peringkat 1 + justifikasi langkah demi langkah (boleh diaudit)

LAPIS 4 — ALGORITMA MUNASAKHAT (faraid berlapis — TERAS modul; ✅ peraturan terverifikasi)
  Trigger: waris (peringkat-n) mati SELEPAS si mati & SEBELUM pembahagian selesai (tarikh dari Lapis 1)
  Kaedah (MAIS E-FARAID §8): bahagian vested waris itu menjadi "pusaka kedua" → Lapis 2–3 DIULANG utk warisNYA
  JAMI'AH (angka penyatu merentas lapisan) dikira melalui 3 hubungan saham-vs-masalah terverifikasi:
  (i) inqisam/tamathul, (ii) tawafuq, (iii) tabayun — contoh penuh MAIS; kes rujukan AL-KAFI #1021:
  8 lapisan, jami'ah 422,400, 19 penerima akhir — TIADA had lapisan fiqh; rekursi dikawal kejuruteraan
  MUSYAHAMAH (✅ Muzakarah Fatwa Kebangsaan Ke-83, Okt 2008): kematian serentak tanpa tertib pasti =
  TIDAK saling mewarisi — pemisah munasakhat-vs-musyahamah = tarikh/masa kematian per waris + perakuan perubatan
  MAFQUD (waris hilang — Irsyad 341): dikira hidup pada hartanya, mati pada harta orang lain; bahagian DITAHAN
  Output: MATRIKS PENERIMA AKHIR merentas SEMUA lapisan (penerima × pecahan berkesan × lapisan asal × jami'ah)

LAPIS 5 — PENYATU HARTA → AGIHAN AKHIR
  Turutan fiqh disahkan IFP/CFP: (0) hibah/penama/amanah [keluar pusaka] → sepencarian → kebumian → hutang
  → wasiat ≤1/3 → FARAID (Lapis 2–4) → radd/Baitulmal
  Gabung dengan Enjin Alokasi (`modul-pengagihan-aset.md` §3): pecahan → aset fizikal berasaskan nilai
  → PENYATA AGIHAN AKHIR kepada PENERIMA: faraid / hibah / wasiat (satu matriks tunggal)
```

**Hasil kepada pengguna:** satu matriks penerima akhir (siapa | asas penerimaan: faraid-lapis-1/2/hibah/wasiat | pecahan | nilai | aset) + pakej permohonan sijil faraid lengkap (silsilah + kiraan berjustifikasi) untuk diserah ke Mahkamah Syariah.

## 3. Cara Ini Menyelesaikan Kelewatan (jujur)

| Punca kelewatan | Apa enjin buat | Apa enjin TAK ubah |
|---|---|---|
| Kiraan berlapis manual & terselit | Lapis 4: kiraan berlapis deterministik + matriks akhir dalam SATU penyata | Kuasa Mahkamah Syariah mengesahkan waris & mengeluarkan sijil |
| Silsilah tak lengkap/bercanggah | Lapis 1: validasi dokumen berperingkat — permohonan TIDAK dibenarkan maju ke Lapis 2 tanpa lengkap (fail-fast awal, bukan jumpa masalah di mahkamah) | Kesediaan waris menyerahkan dokumen |
| Ralat pecahan ('aul/radd/KPK) | Lapis 3: aritmetik tepat + kiraan semak pakar (pintu S4) | Khilaf/penilaian hukum — panel pakar |
| Turutan harta salah (sepencarian/hibah/wasiat) | Lapis 5: turutan fiqh terkunci (disahkan IFP/CFP) | Tuntutan sepencarian perlu perintah MTS (s.122 Akta 303) |
| Ulang semakan oleh agensi | Pakej permohonan lengkap & konsisten kali pertama | SLA agensi & tempoh proses rasmi |

## 4. Integrasi dengan Model Pasangan (pintu)

| Pintu | Peranan |
|---|---|
| S1–S2 | Silsilah + dokumen (Lapis 1) — **human partner sahkan KESAHIHAN setiap nod keluarga & tarikh kematian** (P4: kunci kepada berlapis/musyahamah) |
| S3 | Waris khas & risiko (waris berbeza agama, anak luar nikah) — A2 + pakar syariah |
| S4 | **Kiraan Lapis 2–4** — A5 jana; pakar syariah buat KIRAAN SEMAK sampel + sahkan lapisan berlapis; khilaf → panel |
| S6 | Penyata Faraid Berlapis + matriks penerima akhir masuk kertas kes |
| S7 | Serahan permohonan sijil faraid (pakej lengkap) — **Mahkamah Syariah keluarkan sijil** (hierarki kuasa tahap 1) |
| S8–S9 | Agihan ikut matriks + rekonsiliasi lejar (fi modul §B6) |

## 5. Pengujian & Audit

- **Test vectors**: kes single-layer klasik (balu+anak; suami+anak perempuan; 'aul 6→10/12→17/24→27; radd) + kes BERLAPIS 2-3 tingkat + **kes rujukan AL-KAFI #1021 (8 lapisan, jami'ah 422,400, 19 penerima)** + musyahamah (MKI-83) + waris khas (anak luar nikah via ibu; mualaf; al-haml; mafqud) — setiap satu berjustifikasi & disemak pakar syariah sebelum aktivasi (Fasa 3.6)
- Rekomputasi bebas: input sama → pecahan sama (hash direkod)
- Setiap peraturan pengecualian/penyesuaian bawa citation; PERLU SAHKAN disekat
- Matriks akhir: kaitan ke lejar pusaka & Penyata Agihan (tiada pecahan "terapung")

## 6. Jurang & Status Kebenaran (Gaps)

1. ~~Peraturan teknikal~~ ✅ TERINTEGRASI (`research-faraid-berlapis.md`): munasakhat (MAIS E-FARAID §8; kes 8 lapisan), musyahamah (MKI-83/2008), mahjub penuh, mekanik 'aul/radd + 7 asal masalah + 3 hubungan jami'ah, wasiat wajibah 5 negeri, waris khas. Baki PERLU SAHKAN: **amalan bilangan sijil kes berlapis** (1 perintah jami'ah vs sijil bertingkat — tiada arahan amalan rasmi dalam talian; sahkan dengan JKSM/JKSN negeri).
2. ~~Status e-Faraid & kalkulator~~ ✅ DISEMAK SENDIRI (2026-11-01): e-Faraid JKSM server hidup tetapi sijil TLS salah hos (penyekat capaian); MyLAND single-layer tanpa munasakhat; K-Faraid MAIS pendidikan sahaja; kFaraid JKSM PERLU SAHKAN secara berfungsi.
3. **Konfigurasi negeri → keputusan PANEL PAKAR diperlukan**: radd vs Baitulmal (amalan MAIS = Baitulmal, berbeza fatwa mutaakhirin); wasiat wajibah (5 negeri disahkan; teks Kelantan/Sabah belum semak; senarai negeri tanpa enakmen perlu pengesahan rasmi); fi sijil faraid per negeri.
4. Maksimum lapisan rekursi & kaedah pegangan bahagian lapisan yang belum dituntut (waris lapisan-2 hilang) — dasar dicadangkan, menunggu panel.
5. Enjin menyokong Semenanjung; negeri berbeasas enakmen sendiri — kawalan konfigurasi negeri wajib.

*Disediakan Zizi, 2026-11-01 — melengkapi keluarga enjin: A5 (pecahan) + alokasi bersepara (modul-pengagihan-aset) + fi & lejar (modul-pematuhan-enjin-fi). Peraturan teknikal akan diintegrasikan sebaik research-faraid-berlapis.md selesai.*
