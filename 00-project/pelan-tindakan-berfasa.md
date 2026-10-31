---
title: "Pelan Tindakan Berfasa — Projek EA-MY (Pentadbiran Pusaka Malaysia)"
project: EA-MY
version: 0.1
updated: 2026-10-31
status: aktif — Fasa 1 berjalan
rujukan: 00-project/journal-research-report.md (jurnal penyelidikan induk)
---

# Pelan Tindakan Berfasa — Projek EA-MY

## 1. Gambaran Keseluruhan

**Objektif projek:** Membangunkan sistem webapp + kumpulan agent pakar (agentic AI) yang (i) menjadi **expert advisory** — penasihat legal (civil) dan syariah seperti peguam, dengan kepakaran fiduciary Islamic & non-Islamic jurisdiction; (ii) menjadi **pegawai pentadbir** yang mengurus dan melaksanakan arahan/tindakan mahkamah syariah/civil; (iii) mengautomasikan proses/prosedur pentadbiran pusaka menerusi logik deontik; dan (iv) mengira bahagian syer faraid/hibah (undang-undang Islam) atau wasiat/intestate (undang-undang civil) secara deterministik dan boleh diaudit.

**Prinsip pelaksanaan:**
- BM formal untuk konteks ilmu; rujukan civil dalam English dibenarkan.
- Setiap fakta bercitation; tiada fabrikasi (`PERLU SAHKAN` untuk fakta belum disahkan).
- Human-in-the-loop: agent menasihati & menyediakan; mahkamah/agensi & manusia bertauliah memutuskan.
- Repo git (`estate-admin-malaysia/`) ialah single source of truth.

## 2. Struktur Fasa

| Fasa | Takrif | Output utama | Anggaran tempoh* | Status |
|---|---|---|---|---|
| 1 | Kajian kes, research problems/statements & analisis | Repo ilmu 01–08 + jurnal v0.x + daftar RP | 1–3 hari | **BERJALAN** (mulai 2026-10-31) |
| 2 | Research report/writing, fact findings/data & analisis | Jurnal v2.0 verified, data pack, matriks RP↔bukti, draf SOP & norma | 3–7 hari | Baris gilir |
| 3 | Develop solution: structured processes/procedures + automation agentic AI/deontic logic + webapp platform | SOP digital, Perpustakaan Norma, agent A1–A8, enjin pengiraan, webapp MVP, pilot | 4–8 minggu | Baris gilir |

\* Anggaran berasaskan aliran kerja agent (bukan manual); boleh diubah. Setiap fasa berakhir dengan semakan bersama pemilik projek (go/no-go).

---

## 3. FASA 1 — Kajian Kes, Research Problems & Analisis *(STATUS: BERJALAN)*

**Objektif:** Membina asas ilmu EA Malaysia yang menyeluruh dan bercitation; menetapkan research problems; menganalisis punca–kesan.

### 3.1 Aktiviti

| # | Aktiviti | Kaedah | Status |
|---|---|---|---|
| 1.1 | Riset 7 stream (undang-undang civil; syariah+jurisdiction; institusi+proses; produk; statistik+demografi; kes rujukan; bottleneck+penyelesaian+penambahbaikan) | 7 research agents selari → tulis fail repo bercitation | 7 agent berjalan sejak 2026-10-31 |
| 1.2 | Verifikasi & kawalan kualiti (citation gate) | Semak setiap fail: (a) setiap fakta ada sitasi; (b) sumber sah/berasaskan; (c) tandakan `PERLU SAHKAN` dijangka; (d) spot-check fakta kritikal (had pusaka kecil, angka statistik utama, nama akta/seksyen) | Selepas semua agent selesai |
| 1.3 | Klasifikasi & indeks | Kemas kini README index; klasifikasi kes mengikut isu (hibah, wasiat, penama, sepencarian, waris hilang...) | Selepas 1.2 |
| 1.4 | Daftar jurang (gap register) | Kumpul semua seksyen "Jurang maklumat" → senarai misi Fasa 2 | Selepas 1.2 |
| 1.5 | Kemas kini jurnal & RP | Jurnal v0.x dikemas kini dengan data bercitation; setiap RP diberi bukti awal | Selepas 1.2 |

### 3.2 Kriteria penerimaan Fasa 1

- ≥8 sumber unik bagi setiap fail domain (kecuali fail analisis tulen).
- 100% fakta membawa sitasi atau ditanda `PERLU SAHKAN`; tiada fakta "gostan".
- Semua fail ikut frontmatter + konvensyen (README repo).
- Daftar jurang lengkap; kes rujukan dikelaskan mengikut isu.
- Jurnal v0.x dengan RP bersama bukti awal diterbitkan dalam repo.

---

## 4. FASA 2 — Research Report, Fact-Finding, Data & Analisis

**Objektik:** Menukar repo menjadi **laporan penyelidikan lengkap** — setiap research problem disokong bukti data, dan setiap proses disokong preseden/kes.

### 4.1 Aktiviti

| # | Aktiviti | Output |
|---|---|---|
| 2.1 | Sintesis jurnal v2.0 — integrasi penuh data/citation ke setiap seksyen jurnal; ringkasan eksekutif | `00-project/journal-research-report.md` v2.0 (verified) |
| 2.2 | Data pack & analisis trend — jadual angka bertahun (harta tak dituntut, backlog, kematian, demografi); carta ringkas | `05-statistics/data-pack.md` (atau CSV tambahan) |
| 2.3 | Deep-dive kes + template — setiap kategori kes dihubungkan ke template prosedur (bukti keputusan → langkah amalan) | `06-case-studies/lessons-and-templates.md` dikembangkan |
| 2.4 | Matriks RP↔bukti — setiap RP dipautkan ke data & kes yang mengesahkannya; skor keyakinan (kuat/sederhana/lemah) | `00-project/rp-bukti-matriks.md` |
| 2.5 | Misi pengisian jurang — research tambahan bagi item dalam daftar jurang (angka rasmi, seksyen akta, sistem digital agensi) | Fail domain dikemas kini; daftar jurang dikosongkan/berkurangan |
| 2.6 | Semakan pakar (cadangan) — peguam/pegawai pentadbir berpengalaman menyemak draf jurnal & template | Nota semakan; status `verified` dinaik taraf |

### 4.2 Kriteria penerimaan Fasa 2

- Setiap RP disokong ≥2 sumber bebas (atau dijelaskan mengapa tidak).
- Angka statistik menunjukkan ≥3 titik tahun (trend) untuk metrik utama, atau jurang dijustifikasikan.
- Template prosedur boleh diuji secara kering (walkthrough) ke atas kes contoh.
- Jurnal v2.0 diluluskan oleh pemilik projek (go/no-go ke Fasa 3).

---

## 5. FASA 3 — Pembangunan Penyelesaian (Proses Berstruktur + Automasi Agentic AI/Deontic Logic + Webapp)

**Objektif:** Membina penyelesaian kepada masalah yang dibuktikan dalam Fasa 2, melalui proses/prosedur berstruktur yang diautomasikan oleh agent dan ditetapkan dalam platform webapp.

### 5.1 Sub-fasa

| Sub | Komponen | Aktiviti utama | Output | Kriteria penerimaan |
|---|---|---|---|---|
| 3.1 | SOP digital | Tukar `03-processes/process-maps.md` + template kes kepada checklist digital berperingkat setiap laluan (probat/LA; pusaka kecil; ARB; BPN; EPF/insurans/takaful; tanah; syer) | `09-webapp-blueprint/sop-digital/*.md` | Setiap langkah punya: input, output, dokumen, norma berkaitan, status boleh dijejak |
| 3.2 | Perpustakaan Norma (deontic rules) | Kod WAJIB/DIBENAR/DILARANG sebagai norma JSON + evaluator + ujian unit (konflik, contrary-to-duty) | `09-webapp-blueprint/norma/` + evaluator | 100% norma bercitation; evaluator lulus ujian; pengesan konflik berfungsi |
| 3.3 | Agent A1–A8 | Spesifikasi & binaan agent (RAG atas repo; peranan & had kuasa; audit trail; perisai grounding — tolak jawapan tanpa citation) | Spesifikasi + prototaip agent | Setiap jawapan agent boleh dikesan ke sumber; eskalasi manusia berfungsi |
| 3.4 | Enjin pengiraan | Faraid (ashab al-furud, asabah, 'aul, radd), hibah, wasiat 1/3, Distribution Act; test vectors daripada sumber bercitation | Enjin + set ujian | Lulus 100% test vectors; disemak panel pakar syariah/civil |
| 5.3.5 | Webapp MVP | Modul: wizard klasifikasi kes; penasihat laluan; checklist tracker; kalkulator bahagian; case file & dokumen; chat advisorial; eskalasi pakar; peranan pengguna (waris/pentadbir/pegawai/admin) | MVP boleh diguna | Aliran end-to-end (jurnal Seksyen 6.5) berjalan penuh atas kes simulasi |
| 3.6 | Pilot & validasi | Kes simulasi end-to-end (Muslim pusaka kecil; non-Muslim berwasiat; kes waris hilang; kes hibah dicabar); semakan peguam/pakar syariah; keselamatan + PDPA + disclaimers | Laporan pilot + log rombakan | ≥3 senario lulus; tiada pelanggaran norma kritikal; kelulusan panel |

### 5.2 Susunan keutamaan Fasa 3

1. **3.2 + 3.4 dahulu** (norma & enjin pengiraan — teras logik yang boleh diuji berasingan).
2. **3.1** (SOP digital — rangka proses yang dilalui agent).
3. **3.3** (agent) bersebelahan dengan **3.5** (webapp) secara berperingkat.
4. **3.6** pilot terakhir sebelum sebarang penggunaan luar.

---

## 6. Tatakelola & Kawalan

- **Versi:** git commit setiap kemas kini fail; jurnal & pelan ini dinomborkan versi (semantic).
- **Kawalan perubahan norma:** norma hanya ditambah/diubah melalui cadangan + citation + semakan (bukan suntingan bebas).
- **Panel semakan (dicadang):** peguam (civil), pakar syariah (faraid/wasiat/hibah), pegawai pentadbir berpengalaman — menyemak enjin & norma sebelum pengeluaran.
- **Data:** minimum peribadi; kebenaran pengguna; akuan PDPA `[status: kewajiban perlu disahkan]`; sandaran berkala (repo git + salinan luar — pilihan pemilik projek).
- **Disclaimers platform:** "maklumat & sokongan proses; bukan nasihat guaman berlesen; keputusan muktamad oleh mahkamah/agensi berautoriti".

## 7. Metrik Kejayaan (KPI)

| Metrik | Sasaran | Ukuran |
|---|---|---|
| Coverage norma | ≥90% langkah laluan utama dipetakan ke norma bercitation | Audit SOP ↔ norma |
| Ralat pengiraan enjin | 0 dalam test vectors bercitation | Ujian 3.4 |
| Grounding jawapan agent | ≥95% jawapan membawa citation sah | Sampelan audit |
| Masa penyediaan pakej permohonan | Berkurangan berbanding manual (sasaran diukur semasa pilot) | Perbandingan pilot |
| Kelulusan pakar | Enjin & norma diluluskan panel semakan | Minit panel 3.6 |

## 8. Risiko & Mitigasi (ringkas — penuh dalam jurnal Seksyen 8)

| Risiko | Mitigasi |
|---|---|
| Fabrikasi ilmu oleh LLM | Grounding wajib + citation gate + semakan pakar |
| Kelewatan agen agensi luar | Platform fokus pada penyediaan & penjeakan; integrasi agensi secara berperingkat |
| Perbezaan pendapat syariah (khilaf) | Sumber berautoriti disahkan + panel semakan; pendedahan dalil |
| Nasihat guaman berlesen | Pemosisian "maklumat & sokongan proses"; eskalasi peguam; modul profesional |
| Keselamatan & data peribadi | Kawalan akses peranan, enkripsi, audit trail, ujian keselamatan MVP |

---

## 9. Semakan Status (checkpoint)

| Tarikh | Fasa | Catatan |
|---|---|---|
| 2026-10-31 | Fasa 1 | 7 research agents diatur gerak; repo + jurnal v0.1 + pelan ini diterbitkan; fail awal produk/statistik/limitasi mula ditulis oleh agent |
| 2026-10-31 | Fasa 2 | DIMULAKAN — jurnal v2.0 (sintesis penuh) diterbitkan untuk semakan pemilik projek; 4 misi selari berjalan: data pack & trend, matriks RP↔bukti, misi jurang undang-undang, misi jurang fi & statistik |

*Kemas kini seterusnya: selepas 7 stream selesai — verifikasi, klasifikasi, jurnal v0.2.*
