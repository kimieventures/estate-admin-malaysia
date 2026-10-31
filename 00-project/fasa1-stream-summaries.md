---
title: "Fasa 1 — Ringkasan Hasil 7 Stream Research (agent-reported + disk-verified)"
category: 00-project
updated: 2026-10-31
status: final-fasa-1 (stream 3 rebuild tertanggung)
nota: "Key findings & gaps di bawah seperti dilaporkan agent (atau dikesan semasa recovery 402). Kandungan fail domain adalah ground truth; summary sebahagiannya bersilang antara stream 1–2 semasa recovery sistem — diperlakukan sebagai petunjuk sahaja."
---

# Fasa 1 — Ringkasan Hasil 7 Stream Research

## Status keseluruhan

| Stream | Status final | Fail | Disk-verified |
|---|---|---|---|
| 1. Undang-undang civil | ✅ fail siap; summary gagal 402 | `civil-law.md` | 50KB, sources_count 34 |
| 2. Syariah + bidang kuasa | ✅ fail siap; summary gagal 402 | `syariah-law.md`, `jurisdiction-civil-vs-syariah.md` | 3,379 + 3,141 patah; 36 + 22 sitasi |
| 3. Institusi + peta proses | ❌ gagal 402 sebelum tulis | — (salvage 32 URL) | folder kosong; rebuild dijalankan |
| 4. Produk EA | ✅ siap penuh | 3 fail `04-products/` | 3,998/3,071/2,566 patah; 194 sitasi; 21 PERLU SAHKAN |
| 5. Statistik + demografi | ✅ siap penuh | 2 fail `05-statistics/` | angka + trend; konflik direkodkan berpasangan |
| 6. Kes rujukan | ✅ fail siap; summary gagal 402 | 3 fail `06-case-studies/` | 4,177/4,963/3,346 patah; 19/27/39 sitasi; Templat A–F |
| 7. Bottleneck/solutions/roadmap | ✅ siap penuh | 3 fail `07-limitations/` + `08-improvements/` | angka backlog, pindaan akta, benchmark |

---

## Stream 1 + 2 (summary bersilang semasa recovery — isi pusat: syariah + jurisdiction)

**Key findings (agent-reported):**
- Pembahagian asas: undang-undang pewarisan/wasiat/hibah orang Islam di bawah Perkara 1 Senarai Negeri (Jadual Kesembilan); mesinari probat kekal federal/sivil (Senarai Persekutuan item 4(e)(i)) — disahkan dalam *Latifah Mat Zin v Rosmawati Sharibun* [2007] 5 CLJ 253 / [2007] 5 MLJ 101 (Mahkamah Agung Persekutuan).
- Perkara 121(1A) (kuat kuasa 10 Jun 1988) menyingkirkan bidang kuasa mahkamah sivil atas perkara dalam bidang kuasa Mahkamah Syariah, tetapi mahkamah sivil menentukan sempadannya sendiri; *Indira Gandhi* [2018] 1 MLJ 545 dan *SIS* [2022] 3 MLRA 131 mengesahkan judicial review kekal eksklusif kepada Mahkamah Tinggi Sivil (s.66A Enakmen Selangor 2003 diisytiharkan terbatal).
- Prinsip *Latifah* (para 82): penentuan sama ada harta ialah hibah ialah isu undang-undang Islam untuk Mahkamah Syariah; mahkamah sivil "shall give effect" dalam geran SKM dan pengagihan — model dua-laluan (twin-track).
- Sijil faraid (s.50 Akta 505): Mahkamah Syariah mengesahkan waris & kadar faraid apabila mahkamah/pihak berkuasa lain perlukannya; diperlukan dalam petisyen SKM (senarai semak JBG) dan dikemukakan kepada Pejabat Tanah, bank, JPJ.
- Faraid: 12 waris ashab al-furud dengan bahagian tetap (1/2 hingga 1/6) berdasarkan Al-Nisa' ayat 11, 12, 176; baki kepada asabah; tiada waris → Baitulmal (amalan Malaysia, walaupun ada waris dhawi al-arham).
- Wasiat Islam: had maksimum 1/3 harta bersih selepas kos jenazah & hutang; wasiat kepada waris tidak sah melainkan waris lain bersetuju selepas kematian; Wills Act 1959 s.2(2) mengecualikan wasiat orang Islam.
- Penama (nominee): Fatwa Kebangsaan 1973 & 2000, s.167 Insurance Act 1996, Jadual 10 FSA 2013 — penama orang Islam ialah pentadbir/wasi yang wajib mengagih mengikut faraid, bukan penerima mutlak (KWSP, insurans, takaful — dengan ketegangan praktis operator takaful yang menggabungkan nominasi dengan hibah).
- Harta sepencarian: takrifan s.2(1) Akta 303; s.122 menyebut sumbangan/hutang/keperluan anak, kecenderungan 'equality of division'; tuntutan selepas kematian dibenarkan melalui Arahan Amalan JKSM No. 5/2003; Muzakarah MKI Kali Ke-128 (September 2025): tuntutan sepencarian ke atas KWSP diharuskan tertakluk perintah Mahkamah Syariah.
- Laluan pentadbiran: pusaka besar >RM5 juta → Mahkamah Tinggi Sivil; pusaka kecil ≤RM5 juta → JKPTG (tidak terpakai di Sabah/Sarawak); pusaka ringkas harta alih ≤RM600,000 → Amanah Raya Berhad (Akta 532); Distribution Act 1958 tidak terpakai kepada orang Islam (s.1(2)).
- s.46(2)(b) Akta 505: bidang kuasa Mahkamah Syariah (semua pihak Islam) atas wasiat, hibah, wakaf/nazr, pembahagian pewarisan, penetapan waris & kadar faraid.
- Kes konflik: *Moorthy/Kaliammal* [2006] 1 MLJ 685 (balu bukan Islam tanpa forum); *MAIWP v Lim Ee Seng* [2000] 2 MLJ 572 (bukan Islam tak boleh mewarisi harta orang Islam; harta ke Baitulmal; asas *Re Timah* [1941] MLJ 51).
- 16 pelajaran lintas-kasus + 6 templat operasi (A–F) dihasilkan untuk rujukan webapp/agent.

**Gaps utama (gabungan stream 1+2):**
1. Enakmen Wasiat Orang Islam (Selangor) 1999 s.26(1) — hanya sumber sekunder (PERLU SAHKAN).
2. Muzakarah MKI Ke-67 (2005) berhubung KWSP bukan sepencarian — teks rasmi JAKIM belum disemak (PERLU SAHKAN).
3. Fi sijil faraid RM30/RM20/RM10 & "5 hari" — berbeza ikut negeri, tidak nyatakan negeri rujukan (PERLU SAHKAN).
4. Tiada fatwa kebangsaan seragam bagi hibah bersyarat/nominasi takaful merentas operator (PERLU SAHKAN).
5. Peraturan KWSP terkini (penama sebagai pemegang amanah) tidak disemak dari teks akta/peraturan (PERLU SAHKAN).
6. Protokol/pekeliling rujuk-balik Mahkamah Tinggi↔Mahkamah Syariah tidak ditemui dalam sumber awam — hanya s.50 Akta 505 + prinsip Latifah (PERLU SAHKAN).
7. Kes hibah-vs-pusaka pasca-Latifah di mahkamah rayuan tidak dikenal pasti tanpa pangkalan MLJ/CLJ (PERLU SAHKAN).
8. s.61(3) Enakmen Pentadbiran Ugama Islam (Selangor) 2003 — hanya petikan dalam Latifah (PERLU SAHKAN).
9. Kedudukan Sabah/Sarawak (Intestate Succession Ordinance 1960 Sabah, native courts, tiada mesinari pusaka kecil seragam) — perlu research lanjut (PERLU SAHKAN).
10. Tiada statistik rasmi kes pertindihan bidang kuasa sivil–syariah / kelewatan dua-laluan.
11. Keputusan MR kes Moorthy (20 Ogos 2010) hanya sumber sekunder (PERLU SAHKAN).
12. Keputusan Mahkamah Syariah jarang diterbitkan terbuka — teks penuh perlu semak di esyariah.gov.my/repositori JKSM sebelum dipetik sebagai autoriti.

---

## Stream 3 — Institusi + peta proses (GAGAL — REBUILD)

Tiada fail dihasilkan (HTTP 402 sebelum penulisan). Research diselamatkan ke `00-project/salvage/stream-3-research-notes.md` (32 URL, 12 petikan hasil carian, 20 nota narasi). Rebuild sedang dijalankan dengan bantuan nota tersebut.

---

## Stream 4 — Produk EA ✅

**Key findings:**
- Wasiat ARB: MyGOV menyenaraikan caj RM500–RM1,200 (14 hari bekerja); PDS Bank Islam: Wasiat Asas RM500 tunai / RM300 kad Bank Islam / RM350 saluran silang — tidak termasuk fi pentadbiran pusaka selepas kematian.
- ARB TIADA produk bernama 'MyEstate' — portfolio sebenar dari laman rasmi: Will Writing (Asas/Komprehensif), Voluntary Trust, Estate Administration, Pewarisan Bertakaful, HiBAHKU, Pending Fund Management, Investment Management; domain arb.com.my tidak lagi aktif (laman semasa amanahraya.my).
- HiBAHKU (hibah ARB): RM1,500 aset pertama + RM500 aset tambahan, merangkumi aset bercagar, pengesahan di Mahkamah Syariah; Pewarisan Bertakaful (ARB × Takaful IKHLAS) serendah RM10/bulan (media: sehingga RM54,000 — PERLU SAHKAN).
- Penama: Fatwa MKI Ke-15 (6 Mac 1978) — penama orang Islam hanyalah wasi; IFSA 2013 Jadual 10 perenggan 3(1) membenarkan penama takaful sebagai wasi ATAU benefisiari hibah bersyarat; KWSP: penama Muslim = wasi, ARB boleh dilantik pentadbir 100% simpanan.
- FSA 2013 Jadual 10: trust policy (luar pusaka & luar hutang) HANYA bagi pemilik polisi bukan Islam dengan penama suami/isteri/anak (atau ibu bapa); pemilik polisi Islam tiada trust — penama sentiasa executor, diagih mengikut undang-undang Islam.
- Rockwills (jadual fi wef 01/04/2026): Will Basic RM600 (9 klausa) hingga RM30,000 (48+ klausa); penyimpanan seumur hidup RM1,388–RM1,888; executor korporat RM120; fi trustee tahunan 0.75% RM1j pertama (min RM2,000); fi executor 1.5% (min RM5,000) — sumber ketiga.
- SRO 2023 (kuat kuasa 15 Julai 2023) TIADA skala fi probat khusus — "fair and reasonable" (perenggan 2(f) Jadual Keenam); pasaran RM3,500–RM7,500 GP mudah; pemindahan executor→benefisiari ≤50% fi skala Jadual Pertama.
- Fi pentadbiran pusaka ARB berperingkat 5% (RM25k pertama) → 1% (baki); laluan JKPTG 2% (harta tak alih ≤RM2j) — media/akademik sahaja (PERLU SAHKAN).
- Produk Islamik lain bercost rasmi: MAIS wasiat RM300 (pindaan RM50; fi pelaksanaan wasi 2%→0.25% berperingkat, bawah Enakmen Wasiat Orang Islam Selangor 1999); MyAngkasa Amanah RM540 termasuk SST (pentadbiran 2%); Maybank 'as low as RM298' + EzyWasiat digital.
- Instrumen luar faraid disahkan: Pri-Hibah/Pri-TI/JAAA (as-Salihin — 11 perkhidmatan bawah Trust Companies Act 1949), Hibah Amanah TH, Hibah Amanah ASNB (pendekatan hibah ruqba akaun bersama), wakaf WANCorp/PWS/BSN, kalkulator faraid rasmi JKPTG (MyGOV/MyLand Portal).

**Gaps utama:**
1. Fi tidak diterbitkan rasmi oleh Wasiyyah Shoppe, as-Salihin, Maybank Trustees, CIMB Islamic, ASNB — angka pasaran pihak ketiga sahaja (PERLU SAHKAN).
2. Jadual fi pentadbiran ARB & JKPTG (0.2%/0.3%) hanya media/akademik (PERLU SAHKAN).
3. Manfaat Pewarisan Bertakaful 'sehingga RM54,000' — satu laman media sahaja (PERLU SAHKAN).
4. Status capaian Sistem e-Faraid JKSM (efaraid.esyariah.gov.my) tidak disahkan sendiri — dilaporkan tidak dapat diakses pada 12 September 2026 oleh sumber ketiga.
5. Yuran Hibah Amanah TH (RM190) tanpa label fungsi jelas — perlu pengesahan.
6. Kesesuaian khidmat wasiat Islam Rockwills tidak dapat disahkan dari jadual fi (PERLU SAHKAN).
7. Produk wakaf negeri lain (Perak, Kedah, Kelantan, Pulau Pinang) belum diresearch; cukai/stamp duty penubuhan trust tidak didokumenkan.
8. Percanggahan label MyGOV 'Partition Act 1958' vs Distribution Act 1958 — perlu pengesahan teks akta.
9. Fi corporate trustee bank lain (CIMB Commerce, RHB) & trustee bebas (CSS, V3, Informa) tidak diperiksa.

---

## Stream 5 — Statistik + demografi ✅

**Key findings:**
- Angka 'harta pusaka tidak dituntut' yang kerap dipetik: RM38 bilion (2006) → RM60 bilion (2016) → RM70 bilion (2020) → RM90 bilion (2022–2025); TETAPI MAMPU (2015) dan Ketua Pengarah JKPTG (2022) menafikan kesahihannya (anggaran JKPTG ~RM13.7 bilion); pecahan separuh-rasmi terkini RM65 bilion oleh AmanahRaya (Feb 2025: RM500 juta ARB + RM60 bilion hartanah PTG + RM4.5 bilion WTD JANM).
- Wang Tak Dituntut (JANM/Akta 370): RM9.4 bilion (2021) → RM11 bilion (Okt 2022) → RM12.8 bilion (31 Okt 2024) → RM12.7 bilion (31 Jan 2025, jawapan Parlimen PM) → RM13.3 bilion (April 2025) → >RM13 bilion (Jan 2026); ~70% akaun bank tidak aktif ≥7 tahun; hanya RM4 bilion dituntut sejak 1977; pindaan 2024: tempoh larasan ke Akaun Hasil Disatukan dikurangkan 15 → 10 tahun.
- JKPTG: 84,384 kes pusaka kecil bernilai RM19.01 bilion diselesaikan pada 2025; backlog 46,707 kes (31 Dis 2025), turun ~35% daripada 72,348 (2021); sasaran sifar menjelang 2028; had pusaka kecil dinaikkan RM2 juta → RM5 juta melalui Akta A1643 berkuat kuasa 15 Julai 2024; JKPTG menerima 54–60% permohonan daripada tiga agensi (2023–2025).
- Konflik statistik direkodkan berpasangan: kes selesai 2021 = 25,988 (Ketua Pengarah) vs 43,519 kes/RM11.2 bilion (Menteri); nilai tak dituntut RM65 bilion vs RM90 bilion; pecahan agensi 54–60% vs 65%.
- Tempoh pentadbiran: 4 bulan standard pusaka kecil lengkap tanpa pertikaian (Parlimen, Jan 2026); 4–6 bulan (FAQ JKPTG); probat tidak berbalah 2–3 bulan via e-filing; TIADA purata nasional rasmi.
- Kadar pemilikan wasiat: ~90% tanpa wasiat (Rockwills 1990-an) → 63% (2018) → >80% tanpa wasiat sah (MIEP 2022) → hanya 5% (1.7 juta/34 juta) ada perancangan pewarisan (ARB, Feb 2025) → Sun Life Asia 2026: 37% ada pelan legasi didokumenkan sepenuhnya (naik dari 15% pada 2025).
- KWSP: pengeluaran kematian 58,281 tuntutan / RM1.52 bilion (2020; naik dari RM1.23 bilion/52,127 pada 2018); 16.5 juta ahli / RM1.31 trilion (Ogos 2025); simpanan ahli capai 100 tahun dipindahkan ke Pendaftar WTD.
- DOSM: 198,992 kematian (2024; CDR 5.8/1,000, turun dari puncak pandemik 224,931/6.9 pada 2021); Islam 63.5% (Banci 2020) — faraid saluran dominan; 65+ mencapai 8.0% (2025) — negara menua, unjuran aged society (14%) menjelang 2048.
- Kes pusaka kecil selesai 2025 (84,384) ≈ 42.4% daripada kematian 2024 (~199,000) — jurang besar volum kematian vs pentadbiran formal.
- Statistik probat/LA terbaik ialah 2013 (Semenanjung; kertas Tun Abdul Hamid): Mahkamah Tinggi 7,982, AmanahRaya 8,341, Pejabat Tanah 42,663 permohonan; >90% permohonan mahkamah oleh bukan Islam; >90% Pejabat Tanah oleh orang Islam.

**Gaps utama:**
1. Tiada siri tahunan rasmi kes probat/SKM Mahkamah Tinggi.
2. Tiada angka purata tempoh pentadbiran nasional rasmi.
3. Tiada angka rasmi nilai harta tidak dituntut — MAMPU/JKPTG menyanggah; hanya pecahan ARB RM65 bilion separuh-rasmi.
4. Tiada angka KWSP simpanan si mati belum dituntut.
5. Titik backlog JKPTG 2022–2024 tiada; kes selesai 2021 konflik (25,988 vs 43,519).
6. Pecahan demografi WTD tidak diterbitkan JANM.
7. DOSM tidak menerbitkan kematian mengikut agama — angka kematian Muslim 2024 (~126,360) ialah kiraan ilustratif.
8. Statistik tahunan sijil faraid (JKSM) & permohonan pusaka ringkas ARB tidak diperolehi.
9. Umur penengah 31.3 tahun (Utusan 2026) — tahun rujukan perlu disahkan; 65+ 2024 berkonflik kecil (7.6% vs 7.7%).

---

## Stream 6 — Kes rujukan ✅ (fail lengkap; summary tidak diterima)

**Disk-verified:** 3 fail lengkap — civil-cases (7 kategori + jadual prinsip + 7 gaps), syariah-cases (6 kategori termasuk kes Nyonya binti Tahir + jadual + 7 gaps), lessons-and-templates (16 pelajaran + TEMPLAT A–F + nota pembinaan webapp + 7 gaps).

**Templat yang dihasilkan:** (A) bukti bila hibah dicabar; (B) mekanisme waris hilang/tidak dikenali (s.108 Akta Bukti 1950 — anggapan kematian 7 tahun; s.18 Akta Pendaftaran Kelahiran & Kematian 1957); (C) checklist tuntutan harta sepencarian; (D) sebab wasiat void & pencegahan (termasuk suspicious circumstances — Savatery 2023; wasiat Islam >1/3 — Sabri 2017/2018); (E) langkah elak pertikaian penama KWSP/insurans/takaful (How Yew Hock 1996; Divyyaa Machap [2024] 5 MLRH 406 — penamaan terkini menang, penggabungan akaun tak mematikan penamaan; Noridah 2009 — penama KWSP Muslim = wasi); (F) duti & risiko pembuangan pentadbir.

**Gaps utama:** teks penuh keputusan syariah tidak terbuka (perlu esyariah.gov.my/repositori JKSM); citation penuh beberapa kes perlukan MLJ/CLJ; tempoh rayuan s.29 Akta 98 percanggahan 14 vs 30 hari; tiada kes CBT jenayah pentadbir yang bernama disahkan.

---

## Stream 7 — Bottleneck + solutions + roadmap ✅

**Key findings:**
- Backlog rasmi (Bernama/Hansard 29 Jan 2026): 84,384 kes/RM19.01 bilion selesai 2025; baki 46,707 kes (31 Dis 2025); sasaran sifar 2028; tempoh standard 4 bulan (kes lengkap tanpa pertikaian).
- Harta beku ~RM90 bilion (2023–2025) meningkat dari RM60 bilion (2016–2019) dan RM70 bilion (2020); RM100 bilion (IKIM) dianggap 'tidak tepat' oleh kerajaan (jawapan Parlimen 23 Okt 2024); WTD JANM RM13.3 bilion (Apr 2025).
- Tempoh terdokumen: pusaka kecil JKPTG 4–6 bulan (min 5½ bulan Borang A s.8); geran probat 3–6 bulan; SKM 6–9 bulan hingga 6 bulan–2 tahun+ (kompleks).
- Pindaan disahkan: Small Estates (Distribution) (Amendment) Act 2022 [Act A1643] berkuat kuasa 15 Julai 2024 — had RM2 juta → RM5 juta, merangkumi harta alih/tak alih/gabungan; jadual fi baharu P.U.(A) 194/2024: RM30/RM50/0.2%/0.3% (cth. RM100,000 → fi RM200).
- Kesedaran rendah: ~2% penduduk menulis wasiat (BNM 2018), ~5% (ARB 2025), ~1% umat Islam (2011); kekangan utama: kejahilan (70%) dan sikap bertangguh (43.3%) (UiTM Sarawak).
- Konflik bidang kuasa terdokumen: sijil faraid/perintah Mahkamah Syariah BUKAN instrumen boleh daftar di pejabat tanah (Surat Edaran Ketua Pengarah Tanah dan Galian, Bar Circular 077/2026) — waris Islam masih perlu geran probat/SKM sivil.
- Digitalisasi: sistem pusaka kecil JKPTG = MyeTaPP dialih ke MyLAND (permohonan online, ePayment FPX, kalkulator faraid & Akta 300, semakan status); e-Syariah V3 semua negeri KECUALI Sarawak; TIADA 'e-Probate' awam di Malaysia — probat via e-Filing (e-Kehakiman) oleh peguam; 'Carian Probet' capaian dalaman mahkamah sahaja.
- Kos pentadbiran: komisen pentadbir maksimum 5% (s.43(1) PAA 1959 [Act 97]); yuran peguam RM2,000–RM5,000 (pusaka kecil) / RM4,000+ (mahkamah); pemfailan senarai aset RM16 (Kaedah Mahkamah 2012); bon pentadbiran 2 penjamin jika harta >RM50,000; bantuan guaman JBG (pendaftaran RM10).
- Waris hilang: anggapan kematian 7 tahun tanpa khabar (s.108 Akta Bukti 1950); JPN tidak keluarkan sijil kematian tanpa mayat (s.18 Akta Pendaftaran Kelahiran & Kematian 1957) — perlu deklarasi Mahkamah Tinggi.
- Benchmark: Singapura Probate eService (12 April 2023) — online penuh tanpa peguam bagi pusaka ≤S$2 juta (pra-isi MyInfo/ICA); UK wajib probat digital via MyHMCTS sejak 2 Nov 2020 (fi £526, geran 48 jam) — model yang belum wujud untuk probat awam Malaysia.

**Gaps utama:** backlog probat Mahkamah Tinggi tidak diterbitkan; angka RM90–100 bilion ialah anggaran industri; jadual fi mahkamah penuh probat/LA tidak ditemui dalam satu sumber rasmi; median penyelesaian per pejabat tidak diterbitkan; yuran ARB terkini PERLU SAHKAN; statistik Sabah/Sarawak + Mahkamah Anak Watan tidak ditemui; statistik penggunaan sistem digital tidak diterbitkan; tarikh tepat kuat kuasa 121(1A) perlu sumber primer; SOP pendengaran probat online belum diumumkan tarikh pelaksanaan; tiada program AI dalam pentadbiran pusaka Malaysia direkodkan setakat 2026-10-31.

---

## Daftar jurang Fasa 1 → input Fasa 2

Semua seksyen "Jurang maklumat" dalam fail domain + senarai di atas membentuk **daftar jurang** untuk misi pengisian Fasa 2 (aktiviti 2.5 pelan tindakan). Keutamaan tertinggi:
1. Kesahihan enakmen wasiat Islam negeri (Selangor s.26 dsb.) — sumber primer.
2. Teks akta terkini: Small Estates Distribution Act 1955 (seksyen rayuan s.29: 14 vs 30 hari), FSA 2013 Jadual 10, peraturan KWSP.
3. Jadual fi rasmi terkini: ARB (pentadbiran pusaka), JKPTG (pusata kecil), mahkamah (probat/LA).
4. Statistik rasmi: backlog probat Mahkamah Tinggi, sijil faraid tahunan JKSM, siri backlog JKPTG 2022–2024.
5. Kedudukan Sabah/Sarawak menyeluruh (ordinan probat, native courts, pusaka kecil).
6. Keputusan syariah berteks penuh (esyariah.gov.my, repositori JKSM).
