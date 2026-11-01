---
title: "Rangka Pembangunan Sistem — Webapp EA-MY (Web + Mobile, Frontend + Backend)"
project: EA-MY (Fasa 3 blueprint)
version: 1.0
updated: 2026-10-31
status: draft — untuk semakan pemilik projek
kategori: 09-webapp-blueprint
rujukan: konsep-model-agent-human.md (model pasangan stage-gate) · journal-research-report.md §6 · process-maps.md
---

# Rangka Pembangunan Sistem EA-MY

## 1. Gambaran & Matlamat

Sistem web + mobile yang melaksanakan **Model Pasangan Agent–Human (11 peringkat × pintu semakan)** — dari pendaftaran pemohon hingga penyampaian keputusan — dengan audit trail penuh, pentadbiran berperanan, sandaran & pemulihan bencana. Bahasa utama: BM. Keutamaan reka bentuk: **ketepatan & kebolehaudit-an > kelajuan**; guardrails statutori di-mesin.

## 2. Seni Bina Keseluruhan (lapisan)

```
[ PELANGGAN ]
  Web App (responsive) · Mobile (PWA-first → native kemudian)
        ↓ HTTPS
[ API GATEWAY ] — authn (MFA), rate limit, routing
        ↓
[ PERKHIDMATAN BACKEND ]
  ① Modul Pengguna & Peranan (RBAC)
  ② Modul Kes & Kitaran Hidup (workflow engine stage-gate)
  ③ Agent Runtime (A1–A8: RAG atas repo ilmu + LLM gateway)
  ④ Enjin Norma (deontik — evaluator deterministik)
  ⑤ Enjin Kiraan (faraid/hibah/wasiat/Act 300 — deterministik)
  ⑥ Modul Dokumen (jana borang, simpan, tandatangan)
  ⑦ Modul Q&A & Konsensus (transkrip, eskalasi)
  ⑧ Modul Notifikasi
  ⑨ Modul Audit (event store append-only, hash-chain)
  ⑩ Modul Pentadbiran (admin)
  ⑪ Modul Sandaran/DR (scheduler + runbook)
  ⑫ Enjin Fi & Kewangan (jadual fi berversi + lejar pusaka + rekonsiliasi — modul-pematuhan-enjin-fi.md)
  ⑬ Daftar Pematuhan & Laporan Audit (compliance register + audit pack per kes)
  ⑭ Enjin Pengagihan Aset (alokasi in-kind/jual/buyout/partition + Penyata Agihan berasaskan nilai — modul-pengagihan-aset.md)
  ⑮ Enjin Penentuan Faraid (silsilah berstruktur + rule engine waris + pecahan KPK/'aul/radd + ALGORITMA FARAID BERLAPIS + musyahamah — modul-penentuan-faraid.md)
        ↓
[ DATA ]
  PostgreSQL (kes, pengguna, norma) + pgvector (RAG repo ilmu)
  Object storage (dokumen/artifak kes)
  Audit store (append-only / WORM)
  Redis (cache/queue)
        ↓
[ LUARAN ] GitHub (mirror repo ilmu) · sistem agensi (tiada integrasi pada MVP — serahan manual berstruktur)
```

## 3. Modul mengikut Peranan Pengguna

### 3.1 Pemohon / Penfail (customer) — Web + Mobile
- **Registrasi & KYC**: daftar akaun, verify identiti (dokumen), profil waris
- **Intake Wizard**: klasifikasi kes terbantu (S0/S1) — soalan berperingkat, muat naik dokumen, anggaran harta
- **Fail Kes Saya**: status pintu semasa (11 peringkat, jelas & BM mesra), senarai dokumen & status kesahan
- **Q&A dengan Pasukan Kes**: soal/jawab dengan agent+petugas (diluluskan human), notifikasi (push/emel)
- **Terima Keputusan**: pakej akhir (salinan disahkan, jadual pengagihan, rumusan)

### 3.2 Petugas Kes (case officer) — Web (desktop-first)
- **Bar Kerja Semakan (review queue)**: output agent menunggu semakan, turut prioriti & SLA
- **Antara muka Pintu**: lulus / tolak (wajib alasan) / kemaskini / eskalasi
- **Panel Q&A Konsensus**: transkrip, minta bukti, bantah
- **Pengesahan Dokumen**: papar asal vs salinan, tanda kesahihan
- **Kiraan Semak**: papar justifikasi A5 langkah demi langkah + borang kiraan semak manual

### 3.3 Peguam / Pakar Syariah (reviewer profesional) — Web
- Bar semakan khas: nasihat (S3), kiraan (S4), kertas kes (S6)
- Anotasi hujah + citation semak
- Flag khilaf → panel (kitaran semakan norma/pakar)
- Statutory basis viewer: setiap cadangan → seksyen akta (pautan ke repo ilmu)

### 3.4 Penyelia Kanan — Web
- Spot-check rawak pintu (QC), dashboard mutu (kadar tolak, punca, tempoh per pintu)
- Pemutus kebuntuan (eskalasi tingkat 1), panel norma (pentauliahan norma baharu + citation gate)

### 3.4b Pegawai Kewangan / Akaun — Web
- Semak bil (enjin fi), lejar pusaka (DITERIMA/DIBAYAR/DIAGIH) & rekonsiliasi pra-pintu S9
- Q&A konsensus bagi pengecualian fi (Exception Register) — rujuk modul-pematuhan-enjin-fi.md Bahagian B

### 3.5 Admin Sistem — Web
- Pengurusan pengguna & peranan (RBAC), audit log pengguna
- Konfigurasi kitaran hidup (peringkat, pintu, SLA, routing pasangan)
- **Tadbir urus Perpustakaan Norma**: tambah/ubah norma HANYA dengan citation + kelulusan panel; versi & rollback
- Tadbir urus repo ilmu (sync dari git), indeks RAG
- Laporan & KPI (metrik baseline: kadar dokumen lengkap kali pertama, ralat kiraan, tempoh per pintu)
- Konsol sandaran & pemulihan

### 3.6 Peranan sokongan
- **Pegawai Agensi / Mahkamah (portal luar, read-limited + muat naik pengesahan)**: terima pakej kes, muat naik perintah/sijil → status dikemaskini
- **Auditor (dalaman/luaran)**: capaian baca audit trail sahaja

## 4. Modul Proses Teras (backend)

1. **Workflow Engine (stage-gate)**: mesin keadaan konfigurasi — 11 peringkat, syarat lulus per pintu, routing pasangan (agent+human), eskalasi, SLA timer & peringatan. Sumber konfigurasi berasaskan `process-maps.md` + norma
2. **Agent Runtime (A1–A8)**: setiap agent = peranan dengan: prompt+RAG scoped ke fail repo masing (citation wajib), had kuasa (jurnal §6.2), penolakan automatik tanpa citation; A8 pra-semak semua output agent
3. **Enjin Norma**: norma JSON (WAJIB/DIBENAR/DILARANG, bersyarat, CTD) + evaluator + pengesan konflik; hanya norma `terverifikasi` aktif dalam production; `PERLU SAHKAN` disekat
4. **Enjin Kiraan**: pecahan munasabah (Fraction) deterministik + audit langkah + test vectors; output: jadual pengagihan + justifikasi
5. **Case File**: fail kes bersepadu (dokumen, Q&A, keputusan pintu, kiraan, kertas kes) — sumber tunggal status (jawab RP-06)
6. **Dokumen**: templat borang agensi (auto-fill), tandatangan digital, salinan disahkan
7. **Q&A & Konsensus**: sesi berstruktur (cadangan→soalan→jawaban→keputusan), transkrip penuh, mekanisme eskalasi 2-pusingan

## 5. Teknologi Cadangan (cadangan, boleh ganti setanding)

| Lapisan | Cadangan | Nota |
|---|---|---|
| Frontend | Next.js (React) + Tailwind; **PWA** (installable, offline shell) untuk mobile | Satu codebase web+mobile; native (React Native/Flutter) fasa kemudian jika perlu |
| Backend | Python (FastAPI) — sesuai enjin kiraan/norma; atau Node (NestJS) | API REST + WebSocket (status live) |
| DB | PostgreSQL 16 + pgvector | Transaksi (ACID) + RAG dalam satu sistem |
| Agent/LLM | LLM gateway (model diganti-ganti); RAG atas repo (26+ fail markdown, chunked + cited) | Layer abstraksi model — elak vendor lock-in |
| Objek | S3-compatible (MinIO on-prem / cloud) | Dokumen versi + encryption |
| Audit | PostgreSQL append-only + hash-chain; eksport WORM (parquet/PDF) | §6 |
| Infra | Docker Compose (MVP) → Kubernetes (scale); reverse proxy + TLS | |
| Sandaran | pg_dump harian + snapshot objek + mirror git (GitHub) | §8 |

## 6. Audit Trail & Log (reka bentuk)

- **Prinsip**: append-only, tidak boleh diubah/dihapus oleh sesiapa (termasuk admin); tamper-evident.
- **Rekod pintu (gate record)**: `gate_id | kes_id | peringkat | pasangan (agent_id + user_id + peranan) | input_hash | output_hash | asas_statutori (senarai) | qna_transcript_ref | keputusan + alasan | timestamp | signature`.
- **Rantai hash**: setiap rekod memuat hash rekod terdahulu (chain) — pengubahan silam dikesan.
- **Event log umum**: login, kebenaran, perubahan konfigurasi, perubahan norma (siapa+citation+kelulusan), query agent (token, model, citation yang dipulangkan).
- **Pengeksporan**: laporan audit PDF/CSV per kes (untuk mahkamah/auditor) & KPI agregat (tanpa PII).
- **Retensi**: rekod kes ≥ tempoh had kuasa undang-undang relevan; konfigurasi retention dikaji dengan peguam (flag — PERLU SAHKAN tempoh statutori simpanan).

## 7. Keselamatan & Privasi

- AuthN: MFA wajib (petugas/profesional/admin); pemohon boleh mulakan tanpa MFA (progressive)
- AuthZ: RBAC + case-level ACL (hanya pasangan & penyelia nampak kes; pemohon nampak status tersaring sahaja)
- Encryption: TLS 1.3 in-transit; at-rest (DB + objek); kunci dalam vault (managed KMS / HashiCorp)
- PII minimization: simpan apa yang perlu sahaja; waris memberi kebenaran; hak akses/pemadaman PDPA (asas statutori PERLU SAHKAN — disclaimers + peguam data sebelum pelancaran)
- Tandatangan digital atas setiap rekod pintu; anti-tamper cadangan: server-side timestamp (RFC 3161)
- Ujian: SAST/DAST + penetration test pra-pilot; audit kebergantungan

## 8. Sandaran & Pengurusan Bencana (backup & DR)

| Item | Sasaran (cadangan) |
|---|---|
| RPO (data hilang maks diterima) | 24 jam (MVP) → 1 jam (fasa 2 operasi) |
| RTO (masa pulih) | 8 jam (MVP) → 2 jam |
| Kekerapan | pg_dump penuh harian + WAL berterusan; snapshot object storage harian; mirror git repo ilmu (GitHub, sedia berjalan) |
| Lokasi | On-site + **off-site berasingan** (cloud storage encrypted) — 3-2-1 rule |
| Ujian pemulihan | Restore drill suku-tahunan (dijadual admin; hasil direkod) |
| Runbook DR | Dokumen langkah pemulihan + senarai hubutan; disimpan juga cetakan luar sistem |
| Kesinambungan | Degraded mode: jika agent/LLM gagal → pintu manual tetap berfungsi (kertas semakan PDF); jika DB utama gagal → failover read-replica |

## 9. Pelan Pembangunan Berperingkat

| Fasa | Skop | Keluaran |
|---|---|---|
| **F3.a — Asas** (2–3 minggu) | Workflow engine stage-gate + case file + modul pengguna/RBAC + audit v1 + DB schema | Kerangka sistem; 1 peringkat berjalan end-to-end (kertas) |
| **F3.b — Enjin** (2–3 minggu) | Enjin norma (norma terverifikasi sahaja) + enjin kiraan + test vectors + templat dokumen | S4/S5 boleh diuji; kiraan faraid bercitation |
| **F3.c — Agent + Pintu** (3–4 minggu) | Agent runtime A1–A8 (RAG, citation-mandatory) + antara muka pintu petugas + Q&A konsensus + PWA pemohon | Aliran S0–S6 berjalan atas kes simulasi |
| **F3.d — Penyampaian & Pentadbiran** (2 minggu) | Modul admin, tadbir norma, notifikasi, portal agensi (read), pakej penyampaian, laporan | S7–S10 (dengan serahan manual berstruktur) |
| **F3.e — Keselamatan, DR, Pilot** (2–3 minggu) | Pen test, DR drill, panel pakar lantik, **pilot 3 kes simulasi end-to-end** + laporan pilot | Keputusan go-live dalaman |

Anggaran keseluruhan: ± 11–15 minggu pembangunan aktif (agent-assisted, 1-2 pembina). Modul boleh disusun ikut keutamaan D-2 pemilik projek.

## 10. KPI & Kriteria Penerimaan Sistem

- 100% rekod pintu ada asas statutori terverifikasi (PERLU SAHKAN = 0 dalam produksi)
- 0 ralat enjin kiraan atas test vectors bercitation; kiraan semak human sepadan
- Dokumen lengkap kali-pertama ≥ 80% (ukur lepas pilot)
- Tempoh per pintu diukur & dilapor (baseline metrik — cadangan dari cross-examination gaps)
- Audit trail: lulus ujian tamper (ubah rekod silam → dikesan)
- DR: restore drill lulus dalam RTO; backup verify setiap bulan
- Pematuhan & fi: 0 tindakan tanpa asas statutori; 0 bil berasaskan jadual PERLU SAHKAN; rekonsiliasi lulus 100% kes (rujuk modul-pematuhan-enjin-fi.md §A7/§B9)

## 11. Had & Gaps

1. Integrasi sistem agensi (MyLAND/e-Syariah/eGUMIS) TIADA pada MVP — serahan manual berstruktur; integrasi API memerlukan kerjasama/kebenaran agensi (luar kawalan projek).
2. Kuasa & format tandatangan digital + tempoh retensi statutori PERLU SAHKAN dengan peguam sebelum F3.a muktamad.
3. Kos infrastruktur & operasi LLM (token) belum dianggarkan — perlu bajet operasi.
4. Lantikan panel pakar (peguam + pakar syariah) prasyarat pilot — keputusan D-5.
5. Model ini mensasarkan Semenanjung (D-4); modul Sabah/Sarawak (ordinan berasingan) fasa lanjutan.

*Disediakan Zizi, 2026-10-31 — untuk semakan pemilik projek bersama konsep-model-agent-human.md (model pasangan) dan jurnal v2.1.*
