---
title: "Modul Penentuan Faraid — Enjin Faraid Berlapis & Pengiraan Pecahan Deterministik"
project: EA-MY (Fasa 3 blueprint)
version: 1.0
updated: 2026-11-01
status: draft — research peraturan berlapis berjalan (research-faraid-berlapis.md)
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
| F1 | **Kematian berlapis** — waris mati selepas si mati sebelum pembahagian; bahagiannya menimbulkan kiraan faraid kedua (kadang ketiga) | ✅ punca rasmi kelewatan (Bernama 29-01-2026, dalam repo); peraturan teknikal → `research-faraid-berlapis.md` 🔄 | Kiraan bertingkat manual; dokumen sijil tambahan; tempoh berganda |
| F2 | **Verifikasi silsilah waris manual** — pengenalan waris bergantung dokumen (sijil kelahiran/perkahwinan) & kenyataan; tidak berstruktur | amalan PPKP/JKSM (repo: process-maps) | Semakan berulang; ralat penama waris |
| F3 | **Kiraan pecahan kompleks** — 'aul (jumlah > 1), radd (baki tanpa asabah), asal masalah (KPK), nisbah 2:1 | kaedah dalam repo (syariah-law §2.3); mekanik penuh 🔄 research | Ralat manual; tidak konsisten antara pengira |
| F4 | **Waris khas** — anak luar nikah (melalui ibu), waris berbeza agama (tidak mewarisi harta orang Islam — *MAIWP v Lim Ee Seng*, Re Timah), mualaf, al-haml, waris hilang | ✅ sebahagian dalam repo (kes + syariah-law) | Pertikaian & kelewatan penetapan |
| F5 | **Pengecualian waris (mahjub)** — cth. keturunan mengecualikan adik-beradik | 🔄 research (senarai penuh belum dalam repo) | Waris tersenarai salah → sijil ditolak/ulang |
| F6 | **Wasiat wajibah** (cucu yatim) — amalan berbeza negeri | 🔄 research | Ketaksaan antara negeri |
| F7 | **Sistem e-Faraid JKSM** dilaporkan tidak dapat dicapai (Sep 2026, sumber ketiga — PERLU SAHKAN); kalkulator sedia ada (MyLAND dsb.) mungkin single-layer sahaja | 🔄 research | Tiada alat piawai sokong kes berlapis — jurang kejuruteraan kita isi |
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

LAPIS 4 — ALGORITMA FARAID BERLAPIS (nested faraid — TERAS modul ini)
  Trigger: waris (peringkat-n) mati SELEPAS si mati & SEBELUM pembahagian selesai (tarikh dari Lapis 1)
  Kaedah: bahagian vested waris itu menjadi "pusaka kedua" → Lapis 2–3 DIULANG utk warisNYA (peringkat n+1)
  Rekursi terkawal (maks lapisan dikonfigurasi; setiap lapisan = kiraan berasingan berjustifikasi)
  MUSYAHAMAH (kematian serentak): tiada pewarisan antara mereka — peraturan dikuatkuasa ikut tarikh/input
  Output: MATRIKS PENERIMA AKHIR merentas SEMUA lapisan (penerima × pecahan berkesan × lapisan asal)

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

- **Test vectors**: kes single-layer klasik (balu+anak; suami+anak perempuan; 'aul klasik; radd) + kes BERLAPIS 2-3 tingkat + musyahamah + waris khas — setiap satu berjustifikasi & disemak pakar syariah sebelum aktivasi (Fasa 3.6)
- Rekomputasi bebas: input sama → pecahan sama (hash direkod)
- Setiap peraturan pengecualian/penyesuaian bawa citation; PERLU SAHKAN disekat
- Matriks akhir: kaitan ke lejar pusaka & Penyata Agihan (tiada pecahan "terapung")

## 6. Jurang & Status Kebenaran (Gaps)

1. Peraturan teknikal berlapis/musyahamah/mahjub/wasiat wajibah & amalan JKSM (1 sijil vs berlapis?) — 🔄 `01-legal-framework/research-faraid-berlapis.md` sedang dikumpul; **sehingga selesai, Lapis 2 & 4 hanya beroperasi dengan peraturan terverifikasi; yang lain DISEKAT**.
2. Status Sistem e-Faraid JKSM & liputan kalkulator sedia ada (berlapis?) — 🔄 research (jika kalkulator rasmi sokong berlapis, integrasi/muatan dikaji).
3. Wasiat wajibah per negeri — konfigurasi per negeri diperlukan (tiada penetapan sehingga sumber disahkan).
4. Maksimum lapisan rekursi & kaedah pegangan bahagian lapisan yang belum dituntut (waris lapisan-2 hilang) — dasar dicadangkan, menunggu panel.
5. Enjin menyokong Semenanjung; negeri berbeasas enakmen sendiri — kawalan konfigurasi negeri wajib.

*Disediakan Zizi, 2026-11-01 — melengkapi keluarga enjin: A5 (pecahan) + alokasi bersepara (modul-pengagihan-aset) + fi & lejar (modul-pematuhan-enjin-fi). Peraturan teknikal akan diintegrasikan sebaik research-faraid-berlapis.md selesai.*
