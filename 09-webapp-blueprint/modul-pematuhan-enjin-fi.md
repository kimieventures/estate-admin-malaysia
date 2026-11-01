---
title: "Modul Pematuhan & Audit + Enjin Fi & Kewangan — Blueprint Tambahan"
project: EA-MY (Fasa 3 blueprint)
version: 1.0
updated: 2026-11-01
status: draft — untuk semakan pemilik projek
kategori: 09-webapp-blueprint
rujukan: konsep-model-agent-human.md · rangka-pembangunan-sistem.md · 02-institutions/gap-mission-fi-statistik.md · 03-processes/process-maps.md
---

# Bahagian A — Modul Pematuhan & Audit (Compliance as Guardrails)

## A1. Tujuan
Guardrails statutori bukan sekadar "peraturan dalaman" — ia **rujukan & panduan** yang mengikat setiap keputusan dan pengurusan kes, dan **sedia untuk audit** pada bila-bila masa (dalaman, kewangan, mahkamah/agensi, auditor luar). Prinsip: *pematuhan yang tidak direkod dianggap tidak berlaku*.

## A2. Tiga Lapisan Pematuhan

| Lapisan | Komponen | Fungsi |
|---|---|---|
| **L1 — Norma Deontik** | Perpustakaan Norma (WAJIB/DIBENAR/DILARANG + CTD) | Dikuatkuasa MESIN sebelum setiap tindakan (A8 pra-semak); tanpa lulus → tindakan disekat |
| **L2 — Daftar Pematuhan (Compliance Register)** | Metadata setiap norma + jadual fi | **Rujukan & panduan**: siapa/pa bila/mana terpakai; keadaan kuat kuasa; kitaran semakan; pemilik |
| **L3 — Laporan Pematuhan (Audit Pack)** | Auto-generate per kes | Bukti audit: setiap peringkat → norma disemak → keputusan → citation → rekod pintu |

## A3. Daftar Pematuhan — struktur rekod

```
norma_id | domain (probat/pusaka_kecil/ARB/fi/kewangan)
terpakai_laluan[] | terpakai_agama (Islam/bukan/semua) | terpakai_negeri[]
asas_statutori (akta/seksyen/warta/peraturan + citation URL)
tarikh_kuat_kuasa | tarikh_tamat | kitaran_semakan (cth 12 bulan)
status: TERVERIFIKASI (aktif produksi) / PERLU SAHKAN (DISEKAT) / DIPERSOALKAN (flag)
pemilik_peranan | versi | panel_kelulusan (siapa, bila)
```

**Kebolehterpakaian ditentukan oleh atribut kes** (agama si mati · negeri · jenis harta · nilai · **tarikh peristiwa**) — jurisdiksi sebagai fungsi data, bukan andaian. Pelajaran diterapkan daripada kes s.29: **tempoh 14 vs 30 hari bergantung tarikh perintah** → setiap norma & jadual fi mesti membawa tarikh kuat kuasa dan kiraan menggunakan tarikh peristiwa yang betul (retroactive correctness).

## A4. Tadbir urus perubahan norma & fi (change control)
1. Cadangan → **citation wajib** (tiada citation → auto-tolak)
2. Semakan panel (Penyelia Kanan + Pakar Syariah/Peguam ikut domain)
3. Kelulusan → **versi baharu + tarikh kuat kuasa**; norma lama TIDAK dipadam — kekal aktif bagi kes larian (grandfathering) sehingga tarikh-tamat
4. Notifikasi sistem + kemas kini indeks RAG; perubahan direkod dalam audit (siapa/citation/kelulusan)
5. **Fi juga tertakluk kepada kitaran ini** — jadual fi berubah melalui UI pentadbiran, bukan hard-code (lihat Bahagian B)

## A5. Aliran ketidakpatuhan (tak boleh "senyap")
A8 flag pelanggaran → **CTD**: norma pengganti diaktifkan (cth. dokumen hilang → WAJIB salinan rasmi; fi luar-jadual → WAJIB justifikasi + kelulusan) → eskalasi berperingkat (Petugas → Penyelia → Pakar luar → Agensi) → **semua pelanggaran + pengecualian masuk Laporan Pematuhan & Exception Register** (siapa lulus, kenapa, asasnya apa). Ketiadaan asas statutori pada mana-mana keputusan = kecacatan audit, bukan pilihan.

## A6. Empat jenis audit disokong
| Audit | Soalan | Output sistem |
|---|---|---|
| Dalaman (mutu) | Adakah pintu dipatuhi? | Spot-check queue, kadar tolak & punca, laporan QC |
| **Kewangan** | Adakah fi & wang pusaka sah? | Laporan audit fi (B7) + Penyata Akaun Pusaka + rekonsiliasi |
| Pematuhan statutori | Adakah setiap tindakan berpaksikan seksyen? | Audit Pack per kes (L3) — setiap rekod pintu → citation |
| Luaran (mahkamah/agensi/auditor) | Boleh semak semula? | Eksport PDF/CSV baca-sahaja; **rekomputasi bebas** (auditor jalan semula kiraan dengan input sama → hasil mesti seragam; hash input/output direkod) |

Peranan **Auditor** (dalaman/luaran): capaian baca-sahaja + alat rekayak; tiada keupayaan mengubah mana-mana rekod (append-only).

## A7. KPI pematuhan
- 100% tindakan membawa asas statutori terverifikasi (PERLU SAHKAN aktif dalam produksi = **0**)
- Pelanggaran kritikal tanpa CTD = 0; pengecualian fi 100% berjustifikasi & berkelulusan
- Norma melebihi kitaran semakan → amaran automatik kepada pemilik peranan
- Audit Pack lengkap 100% kes (tiada peringkat tanpa rekod pintu)

---

# Bahagian B — Enjin Fi & Kewangan

## B1. Prinsip
Fi = **fungsi deterministik**: `fi = f(laluan, jenis_harta, nilai, tarikh_peristiwa, negeri)` — sama falsafah dengan Enjin Kiraan faraid (A5): deterministik, bercitation, boleh diaudit, **bukan LLM**. Keluaran sentiasa menunjukkan: formula terbuka + versi jadual + citation + hash input.

## B2. Jadual Fi Berpusat (versioned) — kandungan sedia repo (terverifikasi)

| Jadual | Tarikh kuat kuasa | Struktur | Sumber (repo) |
|---|---|---|---|
| **Fi perintah pusaka kecil** (P.U.(A) 194/2024) | 15 Julai 2024 | RM30 / RM50 + 0.2% (harta alih) / 0.3% (tak alih) nilai | gap-mission-fi-statistik; process-maps |
| **Fi pentadbiran pusaka ARB** (RASMI — FAQ amanahraya.my) | semasa | Berperingkat: 5% (RM25k pertama) / 4% / 3% / 2% / 1% baki; deposit RM50 | gap-mission-fi-statistik (Misi 1) |
| ARB Fast Lane | semasa | RM50 / RM150 + 5% (30 hari) | sama |
| ARB cawangan (Kuching/Kota Kinabalu) | semasa | Kuching RM150/RM300/RM500; KK deposit RM1,500/RM2,000 | sama (PERLU SAHKAN skop pusaka am) |
| **Sijil faraid** | semasa | RM30/RM20/RM10 mengikut nilai; ~5 hari | syariah-law; **jadual negeri PERLU SAHKAN satu persatu** |
| **Fi mahkamah** (Lampiran B1 KKM 2012 via P.U.(A) 67/2013) | 1 Mac 2013 | Petisyen probat/SKM RM160; senarai aset RM16; resealing RM400 | gap-mission-fi-statistik (Misi 2) |
| **Komisen pentadbir** (Act 97 s.43(1)) | statut | Maksimum 5% nilai aset | civil-law |
| MAIS wasiat/pelaksanaan (Enakmen Wasiat Selangor 1999) | semasa | Wasiat RM300 (pindaan RM50); fi pelaksanaan wasi 2%→0.25% berperingkat | products; gap-mission-undang |
| MyAngkasa Amanah | semasa | RM540 termasuk SST; pentadbiran 2% | products |
| Yuran peguam probat (SRO 2023, kuat kuasa 15 Julai 2023) | 2023 | TIADA skala khusus — "fair and reasonable" (perenggan 2(f) Jadual 6); pasaran RM2,000–5,000 | products; bottlenecks |
| WTD BPN (Akta 370) | — | Tiada caj (eGUMIS UMA-7) | process-maps |
| KWSP | — | Tiada fi; bantuan kematian RM2,500 (s.58(1)) — bukan fi, tetap direkod | process-maps |

**Peraturan status:** hanya jadual TERVERIFIKASI aktif dalam kiraan produksi; jadual PERLU SAHKAN papar sebagai anggaran berlabel & tidak boleh dijadikan bil rasmi.

## B3. Struktur data peraturan fi

```json
{
  "jadual_id": "FEES-PPKP-194-2024",
  "laluan": "pusaka_kecil",
  "jenis_harta": ["alih","tak_alih","gabungan"],
  "struktur": [
    {"jenis":"tetap","nilai":"RM50","syarat":"permohonan"},
    {"jenis":"peratusan","kadar":"0.003","asas":"nilai_harta_tak_alih","kecuali":"RM50_tetap"}
  ],
  "tarikh_kuat_kuasa": "2024-07-15",
  "tarikh_tamat": null,
  "negeri": ["Semenanjung","Labuan"],
  "citation": "P.U.(A) 194/2024 [rujuk: 03-processes/process-maps.md]",
  "status": "TERVERIFIKASI",
  "versi": 1
}
```

## B4. Fleksibiliti & perubahan fi (keperluan teras)
1. **Bukan hard-code** — jadual fi ialah data berversi; perubahan (warta baharu, kemas kini ARB) dimasukkan melalui UI pentadbiran: rujukan warta + citation + kelulusan panel (kitaran A4) — tanpa pembangunan semula/deploy.
2. **Tarikh peristiwa menentukan versi** — kiraan untuk kes larian menggunakan jadual yang berkuat kuasa pada tarikh peristiwa kewangan (permohonan/perintah/pembayaran). Perubahan fi tidak mengubah kes selesai.
3. **Konflik/jangkawan** — jika dua jadual bertindih: versi berkuat kuasa terkini pada tarikh peristiwa menang; sistem flag pertindihan untuk semakan panel.
4. **Fi luar-jadual (contoh: yuran peguam "fair and reasonable")** — laluan **pengecualian berstruktur**: quotation + justifikasi item + kelulusan berperingkat (Petugas → Penyelia) + direkod dalam **Exception Register** (audit kewangan, B7). Sistem TIDAK membenarkan fi tanpa sama ada (a) jadual bercitation, atau (b) pengecualian berkelulusan.
5. **Rekomputasi** — jika nilai harta berubah selepas penilaian rasmi (JPPH/agensi), fi dikira semula automatik; kedua-dua kiraan (anggaran & akhir) disimpan dengan jejak penuh.

## B5. Nilaian harta/aset (valuation input)
| Punca nilai | Status label | Kegunaan |
|---|---|---|
| Nilai rasmi agensi (penilaian PTG/JPPH/geran) | `NILAI_RASMI` | Fi akhir, bil rasmi |
| Anggaran pasaran (waris/agen) | `ANGGARAN` | Anggaran kos awal (S1) — di-paparkan jelas sebagai anggaran |
| Harga jualan sebenar | `TERJUAL` | Penyelesaian akhir aset dijual |

Aliran: S1 anggaran (transparansi kos kepada pemohon sebelum komit) → S6 nilai rasmi masuk kertas kes → fi final + bil → S8 pembayaran sebenar → S9 rekonsiliasi.

## B6. Proses kewangan & perakaunan
1. **Bil (invoice)**: dijana automatik daripada enjin fi — berperingkat & berlabel: (i) fi/rasmi agensi, (ii) yuran profesional (peguam/pentadbir), (iii) duti & caj (cth SST); formula terbuka pada setiap bil.
2. **Pembayaran**: status tracking (draf → dikeluarkan → dibayar → diterima), rujukan resit (cth MyLAND ePayment), jumlah, tarikh, pembayar; rekod pembayaran hash-linked ke audit.
3. **Lejar Pusaka (estate ledger) — perakaunan fiduciary**: harta si mati ialah amanah; sistem menjejak:
   `DITERIMA` (akaun si mati · hasil jualan · KWSP · takaful/insurans) → `DIBAYAR` (hutang si mati · kos jenazah · fi & duti · yuran) → `DIAGIH` (faraid / Akta 300) — dengan penyata per-aset & per-waris.
   **Penyata Akaun Pusaka** (Estate Account Statement) dijana di S9 — ini juga menunaikan **tugas fiduciary pentadbir untuk merekod akaun** (duty to account — asas: tugas amanah pentadbir, Act 97; pelanggaran = kes breach of trust dalam 06-case-studies).
4. **Rekonsiliasi deterministik**: `Diterima − Dibayar − Diagih = 0` — **syarat PINTU S9**: lejar tak seimbang → rumusan TIDAK boleh dihantar (kawalan kewangan terbina dalam aliran, bukan lepasan).
5. **Eksport perakaunan**: jurnal CSV/lembaran kerja (kategori GL: hasil agensi · yuran profesional · duti rasmi · pulangan waris) untuk sistem perakaunan luar; sokongan pelaporan pejabat (management report) bulanan.
6. **Wang pemohon/stakeholder**: wang terkumpul pusaka disimpan akaun amanah berasingan per kes (cadangan; pengesahan peraturan akaun peguam/client-account PERLU SAHKAN dengan peguam).

## B7. Audit kewangan
- Setiap kiraan fi menyimpan: formula + versi jadual + nilai input (hash) + hasil + tarikh peristiwa → **boleh dihitung semula** oleh auditor (rekomputasi bebas, hasil mesti seragam).
- **Exception Register**: semua fi luar-jadual — siapa lulus, justifikasi, kelulusan berperingkat, tarikh.
- **Laporan Audit Fi per kes**: senarai penuh item (asas, jumlah, bukti bayar, resit) — dilampirkan dalam Audit Pack L3.
- Amati: pengecualian tanpa kelulusan / fi tanpa jadual = pelanggaran norma kewangan (L1) → CTD menghalang penyerahan.

## B8. Integrasi dengan Model Pasangan (S0–S10)
| Peringkat | Peranan Enjin Fi & Kewangan |
|---|---|
| S1 | **Anggaran kos & fi awal** kepada pemohon (transparansi; label `ANGGARAN`) — bahan makluman pintu |
| S4 | (tiada — kiraan bahagian, bukan fi) |
| S6 | Jadual fi akhir + nilai rasmi → masuk kertas kes; bil draf dijana |
| S7–S8 | Pembayaran fi agensi & pelaksanaan direkod; resit rujukan |
| S9 | **Penyata Akaun Pusaka + rekonsiliasi** → syarat pintu rumusan |
| S10 | Pakej penyampaian termasuk penyata akaun & jadual pengagihan kepada pemohon |

Human partner: **Pegawai Kewangan/Akaun** (peranan baharu; wajib bagi kes bernilai tinggi, boleh digabung Petugas bagi kes kecil) — semak lejar & bil; Q&A konsensus dengan A5-Fi & A8.

## B9. KPI fi & kewangan
- 0 bil rasmi berasaskan jadual PERLU SAHKAN; 0 fi tanpa jadual/pengecualian
- 100% pembayaran ada resit rujukan; rekonsiliasi lulus 100% kes sebelum S9
- Purata varian fi (anggaran vs final) diukur & dilaporkan (metrik kualiti data nilai awal)
- Exception rate (fi luar-jadual) dipantau bulanan oleh Penyelia

---

# Bahagian C — Sketsa Model Data & Kaitan

**Entiti utama:** `fee_schedule` (versi, kuat kuasa, citation) · `fee_rule` (struktur band/rate/syarat) · `fee_computation` (input hash, formula, hasil, tarikh peristiwa, versi jadual) · `payment` (status, resit, rujukan pintu) · `estate_ledger` (per kategori DITERIMA/DIBAYAR/DIAGIH, per-aset, per-waris) · `compliance_norm` (Daftar Pematuhan A3) · `compliance_check` (norma × tindakan × keputusan) · `audit_pack` (eksport per kes) · `exception_register`.

**Kaitan modul:** Enjin Fi = ahli keluarga A5 (deterministik + kiraan semak human); pematuhan = A8 + Daftar Pematuhan + human panel; pembayaran & lejar = input ke audit trail hash-chain (rangka §6). Perubahan norma & fi berkongsi SATU kitaran tadbir urus (A4) — satu sumber kebenaran untuk "apa yang dibenarkan & berapa harga".

## Jurang & Kebenaran yang tinggal (Gaps)
1. Jadual fi sijil faraid per negeri (warta negeri) belum disahkan satu persatu — kini label anggaran sahaja.
2. Fi pendaftaran pemindahan tanah (Borang 14A, NLC) & duti setem — tiada kadar bersumber tunggal dalam repo (PERLU SAHKAN) — bila disahkan, masuk jadual tanpa perubahan kod.
3. Skop "pusaka am Semenanjung" bagi skala fi ARB 5%→1% (rasmi untuk kenderaan/Sabah) — PERLU SAHKAN dengan ARB.
4. Peraturan akaun amanah/client-account untuk wang pusaka (peguam/ARB) PERLU SAHKAN dengan peguam sebelum modul pembayaran live.
5. Fi transmission syer (Bursa/CDS) & SLA KWSP/bank belum bersumber (warisan gaps Fasa 2).
6. Kitaran semakan jadual fi (tahunan?) dicadangkan — menunggu kelulusan pemilik projek.

*Disediakan Zizi, 2026-11-01 — lengkapkan konsep-model-agent-human.md (pintu S1/S9) dan rangka-pembangunan-sistem.md (perkhidmatan ⑫⑬). Untuk semakan pemilik projek bersama D-1/D-2.*
