---
title: "Cross-Examination: Penyelesaian Klasik Mahkamah/Pihak Berkuasa vs Penyelesaian Berstruktur oleh Agent EA-MY (A1–A8) — Kes Civil"
category: case-studies
updated: 2026-10-31
status: draft
sources_count: 18
---

# Cross-Examination: Klasik vs Agent — Kes Civil Pentadbiran Pusaka Malaysia

Fail ini menjalankan **cross-examination**: membandingkan cara KLASIK mahkamah sivil/pihak berkuasa menyelesaikan kes pusaka (sebagaimana direkodkan dalam fail-fail repo ini) dengan cara **AGENT EA-MY (A1–A8)** akan menyelesaikan kes yang sama secara berstruktur, mengikut aliran kes end-to-end dalam `00-project/journal-research-report.md` §6.5 (klasifikasi A3 → norma pra-syarat A8 → nasihat A1/A2 → pengiraan A5 → analitis kes A4 → dokumen A7 → serahan human-in-the-loop → orkestrasi status A6).

**Prinsip kerangka (wajib bagi setiap kes):** (1) Kes & isu; (2) Penyelesaian klasik; (3) Simulasi penyelesaian agent; (4) Jadual perbandingan; (5) Penambahbaikan agent; (6) Kelemahan proses klasik yang boleh dipertikaikan; (7) Guardrails statutori; (8) Verdict jujur.

**Prinsip statutori agent:** agent TIDAK mencipta undang-undang; ia **memoperasikan** undang-undang sedia ada; keputusan muktamad kekal dengan mahkamah/agensi (human-in-the-loop); item bertanda **PERLU SAHKAN TIDAK boleh digunakan sebagai guardrail**. Semua angka seksyen diangkat daripada fail repo sahaja — tiada fakta direka; fakta yang tidak lengkap dalam repo dinyatakan sebagai tidak direkodkan.

---

## (A) INDEKS INDUK — Semua Kes dalam Repo (Civil + Syariah + Situasi Khas)

Indeks ini mengumpulkan semua kes yang direkodkan dalam `civil-cases.md`, `syariah-cases.md`, `lessons-and-templates.md`, `01-legal-framework/jurisdiction-civil-vs-syariah.md` dan `01-legal-framework/gap-mission-undang-undang.md` (termasuk kes *Darius Hoindi* [2025]).

### A.1 Kes mahkamah sivil

| Kes | Mahkamah | Isu | Keputusan ringkas | Fail sumber |
|---|---|---|---|---|
| *Latifah bte Mat Zin v Rosmawati bte Sharibun & Anor* [2007] 5 MLJ 101; [2007] 5 CLJ 253 | Mahkamah Persekutuan | Penetapan hibah dalam petisyen pentadbiran pusaka orang Islam — bidang kuasa siapa? | Isu hibah ditentukan menurut undang-undang Islam oleh Mahkamah Syariah; mahkamah sivil memberi kesan dalam geran SKM & pengagihan (twin-track) | civil-cases.md §1.1; jurisdiction §5.1 |
| *Dato' Kadar Shah bin Tun Sulaiman v Datin Fauziah binti Harun* [2008] 4 CLJ 504 | Mahkamah Tinggi KL | Tuntutan amanah sivil yang berbalut isu hibah — forum? | Bidang kuasa sivil kekal bagi tuntutan amanah; pakar undang-undang Islam dibenarkan; permohonan defendan ditolak | civil-cases.md §1.2 |
| *Savatery a/p Jayaraman v Teoh Ying Rin* [2024] 7 MLJ 163 (diputuskan 29.9.2023) | Mahkamah Tinggi Shah Alam | Suspicious circumstances & undue influence dalam wasiat 2019 | Wasiat batal dan tidak sah; pewasiat dianggap mati tanpa wasiat | civil-cases.md §2.1 |
| *Sabri bin Hasan lwn Ghori Mohammed bin Abd Majeed Mustaffa* [2018] 8 CLJ 788 [HC] | Mahkamah Tinggi | Wasiat seluruh harta kepada bukan waris; geran probet diketepikan? | Wasiat seluruh harta tidak sah (had syarak 1/3); geran probet diketepikan; kos RM15,000/RM5,000 | civil-cases.md §2.2; syariah-cases.md §2.2 |
| *Lionel Lau Siang Kok v Datuk Seri Panglima Lau Chon Kun* [2013] 1 CLJ 619 | Mahkamah Rayuan | "Person interested" s.41 PAA 1959; adakah DNA disyaratkan | Rayuan dibenarkan; s.41 tidak mensyaratkan DNA; pelaksana tidak boleh sembunyikan wasiat | civil-cases.md §2.3 |
| Pusaka Lim Siew Kim (RM1.6 bilion; tiada citation — media) | Mahkamah Tinggi KL | Kesahihan wasiat ketiga; keteranan s.60 Akta Keterangan; pentadbir sementara membayar >RM2j tanpa kelulusan | Bantahan awal ditolak (Mac 2026); kes bersambung; pentadbir terikat perintah mahkamah | civil-cases.md §2.4 |
| *Mak Chee Chong v Rockwills Trustee Bhd* [2016] 10 MLJ 124 | Mahkamah Tinggi Kota Kinabalu | Pembuangan pelaksana korporat (s.54 & s.89 Ordinan Probet Sabah Cap. 109) | Pembuangan dibenarkan — kebajikan benefisiari paramount; kebuntuan = "sufficient cause" | civil-cases.md §3.1 |
| Pusaka Loh Mui Fah / Loh Gwo Burne (tiada citation — media, 2026) | Mahkamah Tinggi KL | Pematuhan tugas fidusiari pentadbir; akaun pusaka | Saman ditolak — pentadbir kekal; mahkamah perintah akaun lengkap | civil-cases.md §3.2 |
| *Mohamed Sulaiman bin Abdul Aziz v Mohamed Batcha bin Abdul Aziz* (mylaw.my; tahap mahkamah PERLU SAHKAN) | Mahkamah (PERLU SAHKAN) | Kebenaran s.60 PAA 1959 untuk melupuskan harta tak alih pusaka | Dibenarkan — kesukaran pelaksanaan hadapan bukan alasan cukup | civil-cases.md §3.3 |
| *Wee Ku Wing lwn Amira Umaira Teng binti Abdullah* (MT Kota Bharu 31.7.2024; MR 23.7.2026) | Mahkamah Tinggi → Mahkamah Rayuan | Anak mualaf mewarisi pusaka bukan Islam (Akta Pembahagian 1958); aliran s.29 | Perintah Borang E & F diketepikan; agama SI MATI menentukan undang-undang; rayuan balu ditolak (kos RM30,000); s.29 hanya bagi pihak dalam bicara | civil-cases.md §4.1 |
| *Ahmad bin Abd Majeed lwn Habibah bte Abdul Majid* (MR; citation penuh PERLU SAHKAN) | Mahkamah Rayuan | Adakah s.29 Akta 98 satu-satunya remedi | s.29 tidak terpakai kepada tuntutan tersebut; saman pemula kekal tersedia | civil-cases.md §4.2 |
| *How Yew Hock v Lembaga Kumpulan Wang Simpanan Pekerja* [1996] 2 MLJ 474 | Mahkamah Persekutuan | Adakah penamaan KWSP pemupusan wasiat | Ditolak — penamaan KWSP berkanun; bukan harta pusaka; wasiat tidak mengatasi penamaan | civil-cases.md §5.1 |
| *Krishnaveni a/p Munusamy & Anor v Bawaneswary* [2013] 10 MLJ 106 | Mahkamah Tinggi KL | Penamaan KWSP yang mana sah | Penamaan kedua menghapuskan penamaan pertama (reg. 7(1)(b),(c) EPFR 2001) | civil-cases.md §5.2 |
| *Divyyaa Machap v Lembaga Kumpulan Wang Simpanan Pekerja* [2024] 5 MLRH 406 (JE 28/2024) | Mahkamah Tinggi | Penamaan selepas penggabungan akaun KWSP | Penamaan kekal sah; reg. 9(2)(a)(i) — SKM tidak mengatasi akaun bernama | civil-cases.md §5.3 |
| *Kaliammal a/p Sinnasamy v MAIWP* (kes Moorthy) [2006] 1 MLJ 685 | Mahkamah Tinggi KL (→ MR, penghakiman direkodkan 20.8.2010) | Semakan perintah syariah ex parte atas status agama si mati | Tiada bidang kuasa menyemak; jenazah dikebumikan mengikut rite Islam; balu tiada forum berkesan | civil-cases.md §6.1; jurisdiction §5.2 |
| *Yap Yen Piow v Hee Wee Eng* [2017] 1 MLJ 17 | Mahkamah Rayuan | KWSP sebagai "matrimonial asset" s.76(1) LRA 1976 | KWSP bukan matrimonial asset ketat; isteri dianugerahkan 1/4 baki KWSP atas ekuiti | civil-cases.md §7.1 |
| *Teo Chee Cheong v Chiam Siew Moi* [2024] MLJU 2936 | Mahkamah Rayuan | Wang KWSP terkumpul selepas perkahwinan boleh dibahagi? | Wang KWSP selepas tempoh perkahwinan boleh dibahagi sebagai harta perkahwinan | civil-cases.md §7.1 (kes berkaitan) |

### A.2 Kes mahkamah syariah

| Kes | Mahkamah | Isu | Keputusan ringkas | Fail sumber |
|---|---|---|---|---|
| *Shaikh Abdul Latif lwn Shaikh Elias Bux* (1915) 1 FMSLR 204 | Mahkamah FMS | Had maksimum wasiat Islam | Wasiat maksimum 1/3 harta; baki faraid kepada waris (asas had 1/3) | syariah-cases.md §2.1 |
| *Katchi Fatimah lwn Mohamed Ibrahim* (1962) 28 MLJ 374 | — (sumber sekunder) | Baki 2/3 wasiat melebihi 1/3 | Baki 2/3 hak waris faraid; >1/3 sah hanya dengan persetujuan waris | syariah-cases.md §2.1 (kes berkaitan) |
| *Jumaaton & Raja Delila lwn Raja Hazaruddin* [1419H] JH 201 | Mahkamah Tinggi Syariah WP | Bolehkah Mahkamah Syariah keluarkan probet/SKM | Tidak — probet/SKM kekal bidang kuasa Mahkamah Sivil | syariah-cases.md §2.3 |
| *Abu Talib Muda v Che Alias Che Muda* [2007] 1 CLJ (SYA) 327 | Mahkamah Syariah | Kesahihan hibah rumah melalui surat perjanjian | Hibah disahkan — dokumen bertulis + tinggal bersama membuktikan ijab-kabul & qabd | syariah-cases.md §3.1 |
| *TM Feroze Khan & Lain-lain v Meera Hussain* [2006] 1 CLJ (SYA) 250 | Mahkamah Tinggi Syariah PP | Hibah dengan penghibah kekal nama & hasil sewa | Hibah sah; perintah letakhak selepas mati dibenarkan (asas hibah amanah hartanah) | syariah-cases.md §3.2 |
| *Aini Abdul Hamid v Syarul Azrim Shariff* (Kes Mal 14100-044-0606-2007) | Mahkamah Tinggi Syariah WP | Penghibah menikmati manfaat selepas hibah | Dibenarkan dengan persetujuan bersama (asas hibah 'umra/ruqba) | syariah-cases.md §3.3 |
| *Wan Shahriman Wan Suleiman & Anor v Siti Norhayati* [2010] 1 CLJ (Sya) 85 | MTS KL → MRS KL | Wang ex gratia: pusaka atau hibah | MTS: hibah; dibalikkan di Mahkamah Rayuan Syariah (hakim berijtihad) | syariah-cases.md §3.4 |
| *Noridah bt Ab Talib v Hishamuddin bin Jamaluddin* [2009] 4 ShLR 115 | MTS Shah Alam | KWSP/Tabung Haji sebagai harta sepencarian | KWSP = harta pusaka faraid; penama = wasi; bukan sepencarian | syariah-cases.md §4.1 |
| *Wan Ismail Wan Endut v Wan Puziah Wan Awang* [2007] 1 CLJ (Sya) 548 | MTS Trengganu → MRS | Penamaan Tabung Haji (anak angkat) | Penamaan TH berfungsi sebagai lafaz wasiat; permohonan hidupkan semula ditolak | syariah-cases.md §4.2 |
| Kes KWSP tanpa nama (repositori Perpustakaan JKSM) | Mahkamah Syariah | Status wang KWSP bernama | Wang KWSP wajib difaraidkan (rujuk Fatwa MKI ke-49/2000); PERLU SAHKAN butiran | syariah-cases.md §1 |
| *Tengah lwn Ibrahim* (1982) 5 JH (2) 300 | MS → MRS | Adakah isteri berhak separuh harta sepencarian | 1/3 : 2/3 dikekalkan — bahagian ikut takat sumbangan | syariah-cases.md §5.1 |
| *Yang Chik lwn Abdul Jamal* [1985] 6 JH 146 | Mahkamah Syariah | Takrif harta sepencarian | Diperoleh semasa perkahwinan + sumbangan bersama (tenaga ATAU wang) | syariah-cases.md §5.2 |
| Kes sepencarian Kelantan & Johor Bahru (tiada nama; kajian akademik) | MTS | Tuntutan sepencarian selepas kematian | 3/4 : 1/4 (JB); 70% : 30% (USIM); tiada tempoh khusus tuntutan | syariah-cases.md §5.3 |
| *Dalam Perkara Nyonya binti Tahir* [2006] 1 CLJ (Sya) 335 | MTS Seremban | Status agama si mati; keterangan waris bukan Islam | Nyonya bukan Islam semasa mati (atas fakta); jenazah kepada keluarga (upacara Buddha) | syariah-cases.md §6 |

### A.3 Kes konflik bidang kuasa & status agama

| Kes | Mahkamah | Isu | Keputusan ringkas | Fail sumber |
|---|---|---|---|---|
| *MAIWP v Lim Ee Seng* [2000] 2 MLJ 572 | Mahkamah Tinggi (probat) | Bukan Islam mewarisi harta orang Islam | Defendan bukan Islam tiada beneficial interest; harta diserahkan kepada MAIWP | jurisdiction §5.3 |
| *Re Timah Binti Abdullah* [1941] MLJ 51 | Mahkamah (era kolonial) | Waris bukan Islam atas pusaka Muslim | "An infidel is excluded from and cannot succeed to the estate of a Muhammadan" (mazhab Syafie) | jurisdiction §5.3 |
| *Indira Gandhi v Pengarah JAIP* [2018] 1 MLJ 545 | Mahkamah Persekutuan | Semakan perlembagaan selepas Art. 121(1A) | Kuasa semakan perlembagaan mahkamah sivil tidak boleh disingkirkan | jurisdiction §1.2 |
| *SIS Forum (Malaysia) v Kerajaan Negeri Selangor* [2022] 3 MLRA 131 | Mahkamah Persekutuan | s.66A ARIE 2003 (semakan oleh MTS) | Terbatal — kuasa kehakiman eksklusif dua Mahkamah Tinggi Sivil | jurisdiction §5.5 |

### A.4 Situasi khas & administratif

| Situasi | Forum/pihak berkuasa | Isu | Keputusan/rumusan ringkas | Fail sumber |
|---|---|---|---|---|
| Rayuan perintah pusaka kecil s.29 Akta 98 (tiada kes bernama dengan alasan penuh dicapai) | Pegawai Pembahagian Pusaka → Mahkamah Tinggi (keputusan muktamad) | Tempoh rayuan: 14 vs 30 hari | Selepas A1643 (kuat kuasa 15.7.2024): 30 hari + prosedur Kaedah Mahkamah MT; pra-pindaan: ikut tempoh rayuan Sessions Court (lazimnya 14 hari); risalah JBG usang | civil-cases.md §4; gap-mission-undang-undang.md Misi 1 |
| *Darius Hoindi v Thomas Hinjiang & Ors* [2025] 11 MLJ 695 (ringkasan sekunder — teks penuh PERLU SAHKAN) | Mahkamah (Sabah) | Bidang kuasa pentadbiran estet native | "Both the Native Court and the High Court have jurisdiction over the administration and distribution of native estates"; pemohon ada pilihan ANSEO (Cap. 1) atau P&A Ordinance (Cap. 109) | gap-mission-undang-undang.md Misi 4 |
| Penama insurans bukan Islam (Akta Perkhidmatan Kewanan 2013 s.130 & Jadual 10) | Insurer (statutori) | Status wang polisi bernama | Dibayar kepada penama; penama selain pasangan/anak/ibu bapa menerima sebagai wasi | civil-cases.md §5.4 |
| Fatwa MKI 1973/2000 + penama Muslim | Fatwa kebangsaan (diperakui mahkamah) | Status penama KWSP/insurans Muslim | Penama = wasi — wajib faraidkan wang | syariah-cases.md §4; lessons-and-templates.md Templat E |

**Nota kaedah indeks:** kes yang tiada citation penuh dalam repo kekal dilabelkan (media/sumber sekunder/PERLU SAHKAN) — tiada nama kes direka. Untuk citation penuh, rujuk fail sumber dalam direktori `06-case-studies/` dan `01-legal-framework/`.

---

---

## (B) CROSS-EXAMINATION PENUH — 7 Kes/Situasi Civil Utama

Setiap kes di bawah mengikut kerangka 8 bahagian yang seragam. Simulasi agent mematuhi aliran §6.5 jurnal: **A3 (klasifikasi) → A8 (norma pra-syarat, Perpustakaan Norma) → A1/A2 (nasihat bercitation) → A5 (pengiraan, jika berkaitan) → A4 (analitis kes, Templat A–F) → A7 (dokumen) → serahan human-in-the-loop → A6 (orkestrasi status)**.

---

### KES 1 — *Latifah bte Mat Zin v Rosmawati bte Sharibun & Anor* [2007] 5 MLJ 101; [2007] 5 CLJ 253 (hibah vs pusaka; twin-track)

#### 1. Kes & isu

**Mahkamah:** Mahkamah Persekutuan (25 Julai 2007; Abdul Hamid Mohamad FCJ). **Fakta (dari repo):** Rosmawati (anak si mati daripada isteri kedua, Dato' Sharibun bin Wahab) memfailkan petisyen surat kuasa mentadbir di Mahkamah Tinggi Sivil. Latifah (isteri ketiga, caveator) mendakwa wang akaun bersama si mati di Standard Chartered Bank dan Bumiputra Commerce Bank telah dihibahkan kepadanya (hibah), maka bukan harta pusaka untuk difaraidkan. Mahkamah Tinggi memutuskan undang-undang Islam hibah terpakai tetapi tiada hibah atas fakta; Mahkamah Rayuan membalikkan — isu hibah antara orang Islam adalah bidang kuasa Mahkamah Syariah mengikut Perkara 121(1A), dan perintah Mahkamah Tinggi batal (null and void). **Isu:** Adakah penetapan kewujudan hibah dalam petisyen pentadbiran pusaka orang Islam perkara bidang kuasa Mahkamah Syariah? [Sumber: teks penuh penghakiman MP, malikimtiaz.com.my — https://www.malikimtiaz.com.my/doc/latifah.pdf, dicapai 2026-10-31; Repositori Tun Abdul Hamid — https://www.tunabdulhamid.my/index.php/judgments/item/145-mahkamah-persekutuan-malaysia-rayuan-sivil-02-39-2006w-latifah-bt-mat-zin-v-rosmawati-binti-sharibun-anor, dicapai 2026-10-31]

#### 2. Penyelesaian KLASIK (apa yang sebenarnya berlaku)

- **Laluan:** petisyen SKM di Mahkamah Tinggi Sivil → kaveat oleh Latifah (tuntutan hibah) → pertikaian bidang kuasa dibicarakan di **tiga peringkat mahkamah** (Mahkamah Tinggi → Mahkamah Rayuan [2006] 4 MLJ 705 → Mahkamah Persekutuan 2007). Mahkamah Rayuan membatalkan perintah Mahkamah Tinggi **walaupun mendapati hibah terbukti** atas fakta, semata-mata kerana bidang kuasa [Sumber: penghakiman FC, tunabdulhamid.my — https://www.tunabdulhamid.my/index.php/judgments/item/download/1053_b1ca787d987ba08d8e96593613d82dd9, dicapai 2026-10-31].
- **Hasil:** rayuan ke Mahkamah Persekutuan ditolak: (1) isu hibah mesti ditentukan menurut undang-undang Islam; (2) penetapannya (dan penerima/kadar) dalam bidang kuasa Mahkamah Syariah; (3) mahkamah sivil memberi kesan kepada keputusan itu dalam pemberian SKM dan pembahagian harta pusaka.
- **Tempoh & kos:** tidak direkodkan dalam repo (jurang). Yang direkod: keputusan MR pra-FC [2006] 4 MLJ 705 dan FC 2007; pertikaian berlaku bertahun-tahun selepas kematian. Akaun bersama kekal beku sepanjang tempoh prosiding (fakta spesifik pembekuan tidak direkodkan — inferens daripada proses SKM dalam `03-processes/process-maps.md`: probat 3–6 bulan bagi kes lurus; kes dipertikaikan 6 bulan–2 tahun+).
- **Komplikasi:** forum salah pada peringkat pertama membatalkan seluruh prosiding pertama; model dua-laluan (twin-track) hanya dikukuhkan SELEPAS litigasi bertingkat — iaitu waris pada masa itu belajar melalui keputusan rayuan, bukan melalui panduan awal.

#### 3. Simulasi penyelesaian AGENT (A1–A8, ikut jurnal §6.5)

| Langkah | Tindakan agent | APA YANG BERBEZA vs klasik |
|---|---|---|
| A3 Klasifikasi | Intake: si mati orang Islam; harta = akaun bersama bank; wujud tuntutan hibah oleh pihak ketiga keluarga → flag **"pertikaian aktif — hibah"** sebelum sebarang pemfailan | Klasik: pertikaian hanya terserlah selepas petisyen difailkan dan caveat masuk; klasifikasi awam tiada |
| A8 Norma pra-syarat | Perpustakaan Norma mengaktifkan: (i) penetapan hibah = undang-undang diri Islam → Mahkamah Syariah (Perkara 121(1A); Senarai Negeri item 1); (ii) N-PK-01 — WAJIB sijil faraid sebelum pembahagian pusaka kecil Muslim; (iii) Templat A langkah 1: **JANGAN bahagi harta yang dipertikaikan** sehingga penetapan Mahkamah Syariah | Klasik: tiada semakan norma pra-syarat sebelum tindakan; pemfailan di forum salah tidak disekat |
| A1/A2 Nasihat | A2 (syariah): rukun hibah + senarai bukti Templat A (akad bertulis, ijab-qabul, qabd, saksi, kelayakan penghibah, tabiat selepas hibah, pakar undang-undang Islam dibenarkan — *Dato' Kadar Shah*). A1 (civil): mesinari probat kekal sivil (Senarai Persekutuan 4(e)(i)); cadangkan fail penetapan hibah di Mahkamah Syariah DAHULU, kemudian petisyen SKM dengan keputusan syariah dilampirkan | Klasik: nasihat bergantung sama ada peguam tahu twin-track — pengetahuan tersirat |
| A5 Pengiraan | Belum terpakai (hibah belum ditetapkan). Agent sediakan **dua senario jadual faraid** (hibah disahkan / tidak disahkan) dengan justifikasi langkah demi langkah | Klasik: pengiraan hanya dibuat selepas perintah; waris tiada gambaran senario awal |
| A4 Analitis kes | Petik preseden repo: *Latifah* sendiri, *Dato' Kadar Shah* (bentuk tuntutan menentukan forum), *Jumaaton* (Mahkamah Syariah tiada kuasa probet) — risiko forum & bukti dibenderangkan sejak hari satu | Klasik: analisis preseden dibuat peguam secara manual, kos tinggi |
| A7 Dokumen | Draf senarai aset yang **mengasingkan harta dipertikaikan** (ditanda "menunggu penetapan Mahkamah Syariah") + checklist bukti hibah Templat A untuk kedua-dua pihak | Klasik: senarai aset lazimnya memasukkan harta dipertikaikan → risiko perintah batal kemudian (*Wee Ku Wing*: pengguguran/masalah waris membatalkan seluruh perintah) |
| Serahan human-in-the-loop | Keluarga & peguam memutuskan strategi; Mahkamah Syariah memutuskan penetapan hibah; Mahkamah Sivil/PPKP memutuskan geran | Kedudukan sama — agent TIDAK memutuskan |
| A6 Orkestrasi | Jejak status DUA laluan serentak (petisyen penetapan hibah di Mahkamah Syariah → perintah → petisyen SKM sivil → pengagihan) dengan eskalasi manusia pada setiap titik serahan | Klasik: tiada status kes tunggal; waris menunggu tanpa gambaran (RP-06) |

#### 4. Jadual perbandingan

| Dimensi | Klasik | Agent (simulasi) |
|---|---|---|
| Kelajuan | 3 peringkat mahkamah (MT→MR→MP) sebelum struktur sah ditetapkan; tempoh sebenar tidak direkodkan | Klasifikasi & laluan betul pada hari pertama; litigasi bidang kuasa dielakkan (jika fakta tidak dipertikaikan hebat) |
| Ketepatan/konsistensi | Bergantung kepakaran peguam yang mengendalikan — *Latifah* membuktikan forum boleh silap di peringkat MT & MR | Norma deterministik; rujukan forum automatik; konsisten antara kes |
| Kos | Yuran peguam tiga peringkat rayuan + mahkamah (angka tidak direkodkan — jurang); peguam RM2,000–RM5,000 bagi kes pusaka kecil, RM4,000+ bagi mahkamah [Sumber: ASCOLAW — https://ascolaw.co/blog/surat-kuasa-mentadbir-panduan-lengkap-yang-anda-perlu-tahu-untuk-rumah-tanah-pusaka-pada-2024, dicapai 2026-10-31] | Kos nasihat berasaskan ilmu jauh lebih rendah; litigasi bidang kuasa dielakkan = penjimatan terbesar |
| Kebolehaudit-an | Jejak hanya dalam fail mahkamah; waris tidak nampak proses | Audit trail penuh: setiap norma yang mencetuskan setiap cadangan direkod (P4 journal) |
| Risiko pertikaian | Tinggi — pembahagian prematur harta dipertikaikan membatalkan perintah | Rendah — norma pra-syarat menyekat pembahagian sebelum penetapan |
| Akses kepakaran | Hanya melalui peguam; kepakaran dwi-jurisdiction terhad (RP-04) | Checklist & nasihat bercitation tersedia kepada waris awam; eskalasi ke peguam bila perlu |
| Kepatuhan norma | Bergantung disiplin pihak | A8 menandakan pelanggaran WAJIB/DILARANG sebelum tindakan berlaku |

#### 5. Penambahbaikan yang agent perkenalkan

1. Klasifikasi dwi-jurisdiction automatik pada intake (agama si mati + jenis tuntutan) — mencegah pemfailan di forum salah.
2. Norma pra-syarat "JANGAN agih harta dipertikaikan sebelum penetapan syariah" dikuatkuasakan sebelum tindakan, bukan selepas litigasi.
3. Checklist bukti hibah (Templat A) diberikan kepada kedua-dua pihak pada hari pertama — memendekkan persediaan bukti.
4. Pengasingan harta dipertikaikan dalam senarai aset — menghalang perintah dibatalkan sepenuhnya kemudian.
5. Status kes dwi-laluan (syariah + sivil) dalam satu penjejak — waris nampak kedudukan sebenar.
6. Jadual faraid dua-senario untuk pengurusan jangkaan waris.

#### 6. KELEMAHAN/FLAW proses klasik yang BOLEH DIPERDEBATKAN

1. **Forum ditentukan melalui litigasi bertingkat (trial-and-error kehakiman).** Mahkamah Tinggi dan Mahkamah Rayuan kedua-duanya tersilap tentang forum sebelum Mahkamah Persekutuan membetulkan — hujah: jika mahkamah bertingkat pun berbeza pendapat, sangat tidak adil untuk meletakkan beban memilih forum pada waris awam tanpa panduan berstruktur.
2. **Keputusan MR membatalkan perintah walaupun mendapati hibah terbukti** — pembaziran proses substantif akibat isu prosedur; nilai perbicaraan pertama hilang sepenuhnya.
3. **Tiada protokol rujuk-balik bertulis antara mahkamah sivil-syariah dalam kes pusaka** — hanya s.50 Akta 505 dan prinsip *Latifah* didokumenkan; jurang ini direkodkan sendiri oleh repo (`jurisdiction-civil-vs-syariah.md` Gaps butir 1: PERLU SAHKAN).
4. **Kebergantungan pengetahuan tersirat:** twin-track wujud sejak 1988 (Perkara 121(1A) berkuat kuasa 10 Jun 1988), namun amalan hanya terbentuk selepas kes 2007 — 19 tahun kebergantungan pada pengetahuan peguam secara individu.
5. **Waris tidak faham dwi-jurisdiction** — sebahagian punca utama kerumitan sistem (RP-03, satu-satunya research problem berskor KUAT penuh dalam jurnal).

#### 7. GUARDRAILS STATUTORI (kes ini)

| Langkah agent | Asas statutori/asas undang-undang | Status |
|---|---|---|
| Klasifikasi: mesinari probat sivil bagi semua rakyat | Senarai Persekutuan item 4(e)(i) Jadual Kesembilan, Perlembagaan Persekutuan | ✅ terverifikasi |
| Klasifikasi: hibah/wasiat orang Islam = kandungan negeri/syariah | Senarai Negeri item 1 Jadual Kesembilan; Perkara 121(1A) (kuat kuasa 10 Jun 1988) | ✅ terverifikasi |
| Arah rujuk Mahkamah Syariah untuk penetapan hibah | s.46(2)(b) Akta Pentadbiran Undang-Undang Islam (WP) 1993 [Akta 505] — hibah inter vivos & penetapan waris/kadar | ✅ terverifikasi |
| Sijil faraid sebelum pembahagian (norma N-PK-01) | s.50 Akta 505 + amalan PPKP | ✅ terverifikasi |
| Larangan membahagi harta dipertikaikan sebelum penetapan | Prinsip *Latifah* [2007] MP (preseden; "civil court shall give effect", para 82) | ✅ terverifikasi (preseden) |
| Geran SKM hanya selepas keputusan syariah diberi kesan | Akta Probet dan Pentadbiran 1959 [Act 97] s.3, s.30 | ✅ terverifikasi |
| Kemas kini jadual fi/tempoh semasa di paparan nasihat | Pekeliling Majlis Peguam 265/2022; fi P.U.(A) 194/2024 | ✅ terverifikasi (dokumen rasmi) |
| Penerangan amalan hibah bersyarat negeri tertentu (cth. khilaf fatwa) | Sumber syariah berautoriti + panel semakan | ⚠️ PERLU SAHKAN (khilaf pendapat — bukan guardrail sehingga disemak panel) |

#### 8. VERDICT

**SEBAHAGIAN.** Agent lebih baik dalam: klasifikasi forum hari pertama, pencegahan pembahagian prematur, konsistensi, audit trail, dan kos — semuanya konkrit dan boleh diukur. Tetapi kejujuran menuntut tiga pengakuan: (i) **pembentukan undang-undang tetap kerja mahkamah** — penghakiman *Latifah* sendiri yang mencipta kejelasan twin-track; tanpa FC, agent tiada prinsip untuk dimoperasikan; (ii) **penilaian fakta hibah (kredibiliti saksi, qabd, ijab-qabul) kekal dengan Mahkamah Syariah** — agent hanya menyediakan bukti berstruktur; (iii) jika pertikaian benar-benar bermaharajah, litigasi tidak boleh dielakkan — agent memendekkan persediaan, bukan menghapuskan mahkamah.

---

### KES 2 — *Savatery a/p Jayaraman v Teoh Ying Rin* [2024] 7 MLJ 163 (wasiat — suspicious circumstances)

#### 1. Kes & isu

**Mahkamah:** Mahkamah Tinggi Shah Alam (Faizah Jamaludin J; BA-22NCVC-167-06-2020; diputuskan 29 September 2023). **Fakta (dari repo):** Balu (kahwin ±36 tahun, tiada anak) mencabar wasiat 2019 suaminya yang dilaksanakan oleh defendan — bekas pegawai akaun syarikat pewasiat yang menaip sendiri wasiat itu (dan didakwa wasiat 2017/2018), lalu menerima sebahagian besar harta: saham tanah dan kilang, 1,500,000 saham, 60% wang/akaun simpanan tetap dan baki pusaka. Sebulan sebelum kematian pewasiat memindahkan 20,000 dan menjual 1,250,000 saham kepada defendan. **Isu:** Adakah wujud keadaan mencurigakan (suspicious circumstances) dalam penyediaan/pelaksanaan wasiat sehingga ia tidak boleh diprobetkan; adakah wujud undue influence. [Sumber: Malayan Law Journal 2024 Vol. 7, ms. 163, archive.org — https://archive.org/stream/mlj_2024_7/MLJ%202024%207%20163_djvu.txt, dicapai 2026-10-31]

#### 2. Penyelesaian KLASIK (apa yang sebenarnya berlaku)

- **Laluan:** litigasi probat penuh di Mahkamah Tinggi — balu mencabar wasiat selepas kematian; defendan (penyedia-penerima manfaat) mempertahankan wasiat. Nombor kes bertarikh 2020 (BA-22NCVC-167-06-2020) dan keputusan 29 September 2023 — kira-kira **tiga tahun** dari pendaftaran kes ke penghakiman (tempoh tepat pemfailan awal tidak direkodkan dalam repo).
- **Hasil:** wasiat 2019 diisytiharkan batal dan tidak sah — defendan memainkan peranan menonjol dalam penyediaan wasiat dan menerima manfaat besar, lalu gagal menghapuskan syak (termasuk gagal mengemukakan wasiat 2018 dan dokumen arahan pewasiat); beban undue influence tidak beralih kepada plaintif; **pewasiat dianggap mati tanpa wasiat**.
- **Kos:** tidak direkodkan dalam repo (jurang). Yuran peguam bagi kes probat dipertikaikan dalam pasaran: RM4,000+ (firma guaman) hingga lebih tinggi bagi kes berperingkat [rujuk angka pasaran dalam `03-processes/process-maps.md` — jurang fi sebenar kes ini tidak direkodkan].
- **Komplikasi:** dua wasiat terdahulu (2017/2018) gagal dihasilkan oleh defendan — pentadbiran tergendala sementara pertikaian kesahihan; harta kekal beku ±3+ tahun; hasil akhir — intestasi (Akta Pembahagian 1958 bagi bukan Islam), bukan hasrat wasiat 2019.

#### 3. Simulasi penyelesaian AGENT (A1–A8, ikut jurnal §6.5)

| Langkah | Tindakan agent | APA YANG BERBEZA vs klasik |
|---|---|---|
| A3 Klasifikasi | Dua titik masuk yang mungkin. **(a) Waktu wasiat dibuat (pencegahan):** intake wasiat — penyedia wasiat = calon benefisiari utama → flag merah automatik. **(b) Selepas kematian (pertikaian):** intake probat — wasiat + balu mencabar → klasifikasi "wasiat dicabar — suspicious circumstances" | Klasik: tiada mekanisme pencegahan pada waktu wasiat dibuat; syak hanya dinilai mahkamah bertahun-tahun kemudian |
| A8 Norma pra-syarat | Norma formaliti: N-WC-01 — WAJIB wasiat civil bertulis, ditandatangani pewasiat, disaksikan 2 saksi serentak (s.5 Wills Act 1959; Semenanjung sahaja, tidak terpakai kepada Muslim s.2(2)). Ditambah norma Templat D: penyedia wasiat yang menerima manfaat besar menimbulkan suspicious circumstances yang wajib disingkirkan | Klasik: formaliti diperiksa mahkamah secara retrospektif; tiada "gate" sebelum wasiat ditandatangani |
| A1 Nasihat | (a) Waktu wasiat: A1 mengesyorkan wasiat disediakan peguam bebas; simpan draf, arahan bertulis pewasiat, bukti keupayaan (pemeriksaan perubatan bagi pewasiat berusia/sakit). (b) Selepas kematian: A1 menerangkan doktrin suspicious circumstances & beban pembuktian (beban pada penyedia-penerima manfaat untuk menghapuskan syak); remedi s.41 PAA 1959 jika wasiat disembunyikan (*Lionel Lau*) | Klasik: nasihat hanya sampai kepada pihak yang mampu bayar peguam, dan selepas pertikaian bermula |
| A5 Pengiraan | Selepas wasiat diisytiharkan batal: enjin pengiraan intestat deterministik — Akta Pembahagian 1958 s.6(1): balu tiada anak → skema s.6(1) dikenakan mengikut senarai waris yang sah (keputusan akhir waris oleh mahkamah/agensi) | Klasik: pengiraan dibuat peguam secara manual; keputusan boleh berbeza antara praktisi |
| A4 Analitis kes | Petik preseden repo: *Savatery* (penyedia=penerima manfaat), *Sabri bin Hasan* (had 1/3 syarak — jika melibatkan wasiat orang Islam), kes Genting/Lim Siew Kim (wasiat ubah radikal menjelang mati), *Lionel Lau* (s.41) — risiko dinilai atas fakta yang dimasukkan | Klasik: analisis preseden dibuat peguam kes kes |
| A7 Dokumen | Checklist pencegahan (Templat D): draf wasiat, dokumen arahan, rekod keupayaan; bagi pencabar — senarai dokumen yang perlu dituntut daripada penyedia (wasiat 2018, dokumen arahan) — tepat kelemahan yang menewaskan defendan | Klasik: penemuan dokumen berlaku secara sedia ada dalam litigasi |
| Serahan human-in-the-loop | Penilaian kredibiliti & penghakiman suspicious circumstances → Mahkamah Tinggi; agent tidak memutuskan kesahihan wasiat | Kedudukan sama |
| A6 Orkestrasi | Jejak status: geran/probet → cabaran → perintah → pentadbiran intestat; pengiraan bahagian dikemaskini serta-merta selepas perintah | Klasik: tiada status tunggal; waris menunggu |

#### 4. Jadual perbandingan

| Dimensi | Klasik | Agent (simulasi) |
|---|---|---|
| Kelajuan | ±3 tahun litigasi probat (2020→2023) sebelum wasiat diisytiharkan batal | Pencegahan ex ante (flag pada masa wasiat dibuat) boleh menghapuskan litigasi sepenuhnya; bagi kes sedia ada — persediaan dokumen pantas, tempoh mahkamah tetap |
| Ketepatan/konsistensi | Doctrin suspicious circumstances konsisten tetapi bergantung kualiti bar & bench | Norma formaliti & checklist standard; keputusan muktamad tetap mahkamah |
| Kos | Yuran peguam litigasi 3 tahun (tidak direkodkan; jurang) | Kos pencegahan minimum (senarai semak + nasihat); litigasi dielakkan dalam majoriti kes yang dicegah awal |
| Kebolehaudit-an | Rekod mahkamah sahaja | Checklist pencegahan direkod; keputusan menyimpan draf & dokumen arahan = jejak keupayaan pewasiat |
| Risiko pertikaian | Tinggi — wasiat ubah radikal & penyedia-penerima manfaat hampir pasti dicabar (Templat D #1, #8) | Rendah ex ante — pilihan penyediaan bebas diberi sebagai keperluan prosedur |
| Akses kepakaran | Litigasi = hanya melalui peguam | Senarai semak pencegahan percuma/murah kepada pembuat wasiat awam |
| Kepatuhan norma | Formaliti diperiksa retrospektif | Norma N-WC-01 disemak sebelum pelaksanaan |

#### 5. Penambahbaikan yang agent perkenalkan

1. Flag automatik "penyedia wasiat = penerima manfaat" pada masa wasiat dibuat — mencegah corak *Savatery* sebelum berlaku.
2. Senarai semak pencegahan Templat D (draf, arahan bertulis, bukti keupayaan, saksi bebas) sebagai prosedur standard.
3. Pengesanan "wasiat ubah radikal menjelang kematian" (Templat D #8 — pola kes Genting) sebagai amaran berperingkat.
4. Enjin pengiraan intestat deterministik (A5) sedia untuk senario batal — waris tahu kedudukan sandaran sejak awal.
5. Akses remedi s.41 PAA 1959 (memaksa pengeluaran wasiat tersembunyi) sebagai pilihan nasihat awal.
6. Audit trail dokumen wasiat (lokasi salinan, versi draf) untuk mengelak "wasiat hilang".

#### 6. KELEMAHAN/FLAW proses klasik yang BOLEH DIPERDEBATKAN

1. **Tiada pintu kawalan pada masa wasiat dibuat.** Undang-undang menyediakan formaliti s.5 (bertulis, tandatangan, 2 saksi) tetapi tiada mekanisme amaran apabila penyedia wasiat ialah penerima manfaat utama — syak hanya dinilai selepas kematian, apabila bukti (draf, arahan, keupayaan) telah hilang. Hujah: formaliti tanpa pencegahan procedural melindungi instrumen, bukan pewasiat.
2. **Beban pertikaian jatuh kepada pihak paling lewat bertindak.** Balu hanya boleh mencabar selepas kematian — dokumen arahan pewasiat berada di tangan penyedia (yang gagal mengemukakannya dalam kes ini). Hujah: proses klasik mewariskan bukti kepada pihak yang berkepentingan menahannya.
3. **Tempoh litigasi probat ±3 tahun** untuk isu yang, pada pencegahan, kosnya hampir sifar — harta beku & balu lanjut usia menanggung akibat.
4. **Kebergantungan pengetahuan tersirat pembuat wasiat.** Majoriti rakyat tidak tahu doktrin suspicious circumstances wujud sehingga disaman — sejajar dengan statistik repo: ~5% sahaja ada perancangan pewarisan dan kejahilan 70% punca utama harta beku (UiTM/ARB, dirumus dalam jurnal §4 RP-01/RP-04).
5. **Pertindihan instrumen tidak diselaraskan semasa hidup** — wasiat dibuat tanpa semakan penamaan KWSP/insurans (Templat E) — punca kes keluarga How Yew Hock/Krishnaveni; tiada prosedur klasik yang memaksa semakan silang ini.

#### 7. GUARDRAILS STATUTORI (kes ini)

| Langkah agent | Asas statutori/asas undang-undang | Status |
|---|---|---|
| Semakan formaliti wasiat (bertulis; tandatangan pewasiat; ≥2 saksi serentak) | s.5 Wills Act 1959 [Act 346] — teks disahkan (Misi Jurang 2) | ✅ terverifikasi |
| Pengecualian wasiat orang Islam daripada Wills Act | s.2(2) Wills Act 1959 | ✅ terverifikasi |
| Nasihat had wasiat Islam ≤1/3 (jika melibatkan wasiat orang Islam — kes *Sabri*) | Prinsip syarak diperakukan mahkamah probet sivil (*Sabri bin Hasan* [2018] 8 CLJ 788); Enakmen Wasiat Orang Islam (Selangor) 1999 s.26 | ✅ terverifikasi |
| Skema pembahagian intestat selepas wasiat batal | Distribution Act 1958 [Act 300] s.6(1) | ✅ terverifikasi |
| Remedi paksa pengeluaran wasiat oleh waris berkepentingan | s.41 Akta Probet dan Pentadbiran 1959 [Act 97] (*Lionel Lau*) | ✅ terverifikasi |
| Keupayaan pewasiat & kedudukan saksi bawah umur dsb. | s.3, s.4, s.9, s.12 Wills Act 1959 | ✅ terverifikasi |
| Penilaian suspicious circumstances/undue influence | Doktrin undang-undang kes (mahkamah memutuskan; agent tidak menilai kredibiliti) | ✅ terverifikasi (preseden) — keputusan muktamad mahkamah |
| Butir penuh revokasi/perkahwinan dsb. pra-Misi 2 | (Telah disah Misi 2; wasiat istimewa s.26 belum disemak penuh) | ⚠️ PERLU SAHKAN (s.26 privileged wills) — tidak digunakan sebagai guardrail |

#### 8. VERDICT

**SEBAHAGIAN (condong ke YA bagi pencegahan).** Dalam mod pencegahan (wasiat dibuat dengan semakan agent), agent jelas lebih baik: kes *Savatery* tidak akan wujud jika penyedia wasiat bukan penerima manfaat dan dokumen arahan disimpan — itu prosedur, bukan undang-undang baru. Dalam mod pertikaian (kes sudah berlaku), agent hanya mempercepat persediaan dan menurunkan kos; **penilaian kredibiliti saksi dan penghakiman "syak yang tidak dihapuskan" adalah fungsi mahkamah yang agent tidak boleh dan tidak mampu ganti** — dan keputusan Faizah Jamaludin J atas fakta halus (gagal mengemukakan wasiat 2018) memerlukan timbangan kehakiman, bukan checklist. Agent juga tidak boleh menjanjikan hasil (had kuasa A4).

---

### KES 3 — *Divyyaa Machap v Lembaga Kumpulan Wang Simpanan Pekerja* [2024] 5 MLRH 406 (penama KWSP vs wasiat/pentadbiran)

#### 1. Kes & isu

**Mahkamah:** Mahkamah Tinggi (JE 28/2024). **Fakta (dari repo):** Ahli KWSP (Macha a/l Suppiah) menamakan Dharsyaini a/p Vijaya Kumar (7 April 2014, Akaun 13716036); akaun itu kemudian digabungkan dengan Akaun 10458236 tanpa penamaan. Pentadbir memohon wang tergabung diagih melalui surat kuasa mentadbir. **Isu:** Adakah penamaan kekal sah selepas penggabungan akaun. [Sumber: eLaw Malaysia, JE 28/2024 — https://elaw.my/JE/01/JE_2024_28.pdf, dicapai 2026-10-31]

#### 2. Penyelesaian KLASIK (apa yang sebenarnya berlaku)

- **Laluan:** pentadbir (dilantik melalui SKM) memfailkan **originating summons** di Mahkamah Tinggi untuk menuntut wang KWSP tergabung diagih melalui surat kuasa mentadbir — laluan litigasi penuh untuk soal yang berjawapan statutori.
- **Hasil:** OS ditolak — tiada keadaan reg. 7(1) tercetus; penamaan kekal sah dan di bawah reg. 9(2)(a)(i) Dharsyaini berhak kepada baki akaun yang digabungkan — surat kuasa mentadbir tidak mengatasi akaun bernama. "Pentadbir jangan masukkan wang KWSP bernama dalam inventory pusaka — saman akan sia-sia" (pelajaran praktikal repo).
- **Tempoh & kos:** tidak direkodkan dalam repo (jurang) — tetapi kos peguam + fi mahkamah + masa pentadbiran terpakai untuk saman yang dipastikan gagal dari mula.
- **Komplikasi:** jurang kefahaman antara rejim penamaan KWSP (statutori, luar pusaka) dan rejim pentadbiran pusaka (probat/SKM); keluarga percaya SKM memberi hak ke atas wang bernama — kepercayaan yang salah tapi lazim.

#### 3. Simulasi penyelesaian AGENT (A1–A8, ikut jurnal §6.5)

| Langkah | Tindakan agent | APA YANG BERBEZA vs klasik |
|---|---|---|
| A3 Klasifikasi | Intake pentadbiran: inventori aset memasukkan akaun KWSP → agent memeriksa **status penamaan** setiap instrumen (KWSP, insurans, takaful, ASB) sebelum mengira pusaka. Akaun bernama → dikelaskan "luar pusaka" | Klasik: pentadbir memasukkan wang KWSP ke dalam inventory dan menyaman; tiada semakan penamaan awal |
| A8 Norma pra-syarat | Norma Templat E: (i) KWSP bernama (bukan Islam) = bukan harta pusaka; (ii) penamaan tidak boleh dibatalkan oleh wasiat (reg. 7(2) EPFR 2001); (iii) penamaan kekal merentasi penggabungan akaun (*Divyyaa*); (iv) bagi Muslim, penama = wasi (Fatwa MKI 1973/2000; *Noridah*) | Klasik: norma ini tersebar dalam preseden mahkamah & fatwa — tidak dipapar kepada pentadbir awam |
| A1 Nasihat | Nasihat bercitation: wang KWSP bernama terus dibayar kepada penama melalui Pengeluaran Kematian KWSP (percuma) — bukan melalui SKM; pentadbir hanya mentadbir bahagian TAK bernama | Klasik: nasihat bergantung peguam; pentadbir awam bertindak atas anggapan salah |
| A5 Pengiraan | Enjin mengira bahagian faraid/Akta 300 hanya atas baki aset yang benar-benar pusaka — mengelak pengiraan yang memasukkan wang yang bukan pusaka (ralat kategori yang menyebabkan saman) | Klasik: pengiraan manual campur aduk aset bernama dengan pusaka |
| A4 Analitis kes | Preseden: *How Yew Hock* (penamaan berkanun), *Krishnaveni* (penamaan terkini menang), *Divyyaa* (penggabungan tidak mematikan penamaan), *Yap Yen Piow* (KWSP bukan matrimonial asset ketat) — peta lengkap rejim penama | Klasik: preseden dicari peguam semasa pertikaian |
| A7 Dokumen | Senarai aset dwi-kolum: "harta pusaka" vs "harta luar pusaka (bernama)" + dokumen Pengeluaran Kematian KWSP bagi penama | Klasik: borang SKM piawai tidak memaksa pemisahan kategori ini |
| Serahan human-in-the-loop | KWSP memutuskan bayaran kepada penama; mahkamah hanya jika benar-benar dipertikaikan sahnya penamaan (cth. dakwaan pemalsuan — *Krishnaveni*) | Kedudukan sama |
| A6 Orkestrasi | Jejak berasingan: (i) tuntutan penama KWSP (laluan percuma, luar pentadbiran); (ii) pentadbiran baki pusaka (PPKP/MT/ARB ikut nilai) | Klasik: satu laluan sahaja (SKM) digunakan untuk semuanya |

#### 4. Jadual perbandingan

| Dimensi | Klasik | Agent (simulasi) |
|---|---|---|
| Kelajuan | Saman OS + tempoh mahkamah untuk jawapan yang tersedia statutori | Semakan penamaan pada intake — jawapan dalam minit; tiada saman |
| Ketepatan/konsistensi | Pentadbir salah kategori aset → saman sia-sia | Pemisahan kategori "pusaka vs bernama" deterministik |
| Kos | Fi peguam + mahkamah untuk OS yang gagal | Kos semakan minimum; tuntutan penama KWSP percuma |
| Kebolehaudit-an | Rekod saman sahaja | Audit trail klasifikasi setiap instrumen (bernama/tidak) |
| Risiko pertikaian | Tinggi — keluarga beranggapan SKM mengatasi penamaan | Rendah — kedudukan undang-undang dipapar dengan citation sebelum tindakan |
| Akses kepakaran | Preseden MP/MT dalam laporan berlangganan | Nasihat bercitation daripada korpus kes repo |
| Kepatuhan norma | Norma luar-pusaka KWSP tidak diperiksa sebelum saman | A8 menyekat kemasukan aset bernama ke inventory |

#### 5. Penambahbaikan yang agent perkenalkan

1. Semakan penamaan WAJIB pada intake pentadbiran (KWSP/insurans/takaful/ASB) — aset bernama diasingkan sebelum pengiraan.
2. Pemisahan dwi-laluan: tuntutan penama (agensi, percuma) vs pentadbiran pusaka (PPKP/MT/ARB).
3. Pencegahan saman sia-sia — jaminan proses, bukan jaminan hasil.
4. Bagi Muslim: nasihat "penama = wasi, wajib faraidkan" (Templat E) dengan kalkulator faraid bersambung — mengelak penama merogol wang.
5. Jadual perbandingan penamaan (reg. 7 EPFR 2001: penamaan kemudian hapuskan penamaan terdahulu) untuk pertikaian tarikh.

#### 6. KELEMAHAN/FLAW proses klasik yang BOLEH DIPERDEBATKAN

1. **Dwi-rejim yang tidak dipaparkan kepada awam:** penamaan KWSP (statutori, luar pusaka) dan wasiat/pentadbiran (pusaka) beroperasi secara terpisah, tetapi tiada agensi yang memberi penerangan bersepadu — pentadbir yang jujur (seperti dalam *Divyyaa*) menyaman kerana yakin SKM merangkumi segalanya. Hujah: sistem yang membenarkan saman yang pasti gagal dari mula adalah sistem yang gagal memaklumkan.
2. **"Wasiat tidak membetulkan penamaan lama"** (reg. 7(2) EPFR 2001; *How Yew Hock*) — tiada mekanisme peringatan silang apabila wasiat dibuat/keadaan berubah (perceraian/kahwin); penukaran penamaan memerlukan tindakan berasingan yang lazimnya terlupa.
3. **Kesimpulan teknikal penggabungan akaun** hanya boleh didapati melalui penghakiman mahkamah — KWSP tidak menerbitkan panduan awam yang jelas tentang kesan penggabungan terhadap penamaan (jurang maklumat; hanya tersirat dalam JE 28/2024).
4. **Bergantung kepakaran peguam bagi isu deterministik** — jawapan reg. 9(2)(a)(i) tidak memerlukan budi bicara; membebankan sistem mahkamah untuk soal kategori adalah pembaziran sumber kehakiman.

#### 7. GUARDRAILS STATUTORI (kes ini)

| Langkah agent | Asas statutori/asas undang-undang | Status |
|---|---|---|
| Klasifikasi penamaan KWSP berkanun (bukan pemupusan wasiat) | s.54(1A) Akta KWSP 1991 [Act 452] (dimasukkan Akta A1300/2007) | ✅ terverifikasi |
| Nasihat "wasiat tidak mengatasi penamaan" | reg. 7(2) Peraturan-Peraturan KWSP 2001 (EPFR 2001) | ✅ terverifikasi (dalam repo via *How Yew Hock*/ZIC/Gavin Jayapal) |
| Nasihat penamaan kekal selepas penggabungan akaun | reg. 9(2)(a)(i) EPFR 2001 (*Divyyaa Machap* [2024] 5 MLRH 406) | ✅ terverifikasi |
| Nasihat penamaan terkini menghapuskan penamaan terdahulu | reg. 7(1)(b), (c) EPFR 2001 (*Krishnaveni* [2013] 10 MLJ 106) | ✅ terverifikasi |
| Nasihat penama Muslim = wasi (faraidkan) | Fatwa Majlis Raja-Raja ke-96 (20.9.1973) & Muzakarah MKI ke-49 (19.9.2000); diperakui *Noridah* [2009] 4 ShLR 115 | ✅ terverifikasi (fatwa + preseden) |
| Nominasi ahli Islam luput 1 tahun selepas kematian jika tiada permohonan (mulai 1.1.2017) | Laman rasmi KWSP | ⚠️ PERLU SAHKAN (nilai operasi KWSP — disemak semasa pelaksanaan; bukan guardrail keputusan) |
| Pemakaian Akta 300 (intestat bukan Islam) | Distribution Act 1958 s.6(1); pengecualian Muslim s.2 | ✅ terverifikasi |

#### 8. VERDICT

**YA (bagi pentadbiran yang betul), dengan satu sempadan.** Ini kes di mana agent paling jelas mengatasi proses klasik: jawapan kepada isu *Divyyaa* bersifat kategori/deterministik (statut + peraturan), tidak melibatkan budi bicara fakta — dan pentadbir klasik tetap menyaman kerana tiada paparan ilmu berstruktur. Agent menjimatkan mahkamah, peguam, masa, dan mengelak kecewa keluarga. Sempadannya: jika sahnya penamaan benar-benar dipertikaikan atas fakta (dakwaan pemalsuan seperti *Krishnaveni*), forum mahkamah tetap diperlukan — dan keputusan mahkamah tetap yang membentuk ilmu yang agent operasikan (JE 28/2024 sendiri kini sebahagian korpus repo).

---

### KES 4 — *How Yew Hock v Lembaga Kumpulan Wang Simpanan Pekerja* [1996] 2 MLJ 474 (penggabungan rejim: wasiat vs penamaan)

#### 1. Kes & isu

**Mahkamah:** Mahkamah Persekutuan (1996). **Fakta (dari repo):** Si mati berwasiat melantik plaintif (anaknya) sebagai pemegang amanah wasiat, kemudian menamakan anak perempuannya sebagai penama KWSP. Plaintif memohon pengisytiharan penamaan itu batal. **Isu:** Adakah penamaan KWSP pemupusan wasiat (testamentary disposition) yang boleh diketepikan wasiat. [Sumber: ZIC Legal — https://www.ziclegal.com/resources/the-distribution-of-insurance-and-epf-in-malaysia, dicapai 2026-10-31; Gavin Jayapal — https://www.gavinjayapal.com/post/can-a-will-override-epf-insurance-nominations, dicapai 2026-10-31]

#### 2. Penyelesaian KLASIK (apa yang sebenarnya berlaku)

- **Laluan:** pertikaian keluarga (anak lelaki pemegang amanah wasiat vs adiknya penama KWSP) dibawa **sehingga ke Mahkamah Persekutuan** — peringkat tertinggi badan kehakiman — semata-mata untuk soal kategori statutori.
- **Hasil:** permohonan ditolak — penamaan KWSP ialah penamaan berkanun (statutory nomination; kini s.54(1A) Akta KWSP 1991 dan Peraturan 9 EPFR 2001), bukan wasiat; caruman dan faedah KWSP tidak menjadi sebahagian harta pusaka — harta terus berpindah daripada KWSP kepada penama (mengutip Mellows, *The Law of Succession*).
- **Tempoh & kos:** tidak direkodkan dalam repo (jurang); secara struktur — litigasi hingga Mahkamah Persekutuan melibatkan dua peringkat rayuan sebelumnya.
- **Komplikasi:** kekeliruan awam "wasiat mengatasi segalanya" — kepercayaan yang menyebabkan keluarga ini berperang; keputusan MP 1996 menjadi asas ilmu yang kemudiannya diulang masalahnya dalam *Krishnaveni* (2013) dan *Divyyaa* (2024) — iaitu kekeliruan yang sama berterusan ±28 tahun.

#### 3. Simulasi penyelesaian AGENT (A1–A8, ikut jurnal §6.5)

| Langkah | Tindakan agent | APA YANG BERBEZA vs klasik |
|---|---|---|
| A3 Klasifikasi | Intake: wasiat ada + penamaan KWSP ada → agent mengesan **pertindihan instrumen** serta-merta dan memaparkan kedudukan kedua-duanya | Klasik: pertindihan hanya ditemui apabila saman difailkan |
| A8 Norma pra-syarat | Norma Templat E #1: penamaan KWSP (bukan Islam) = luar pusaka; wasiat TIDAK mengatasi penamaan (reg. 7(2) EPFR 2001); penama = benefisiari | Klasik: norma wujud hanya dalam penghakiman |
| A1 Nasihat | Kepada pemegang amanah wasiat: nasihat bercitation bahawa permohonan pengisytiharan penamaan batal akan gagal (preseden *How Yew Hock* MP); nasihat pencegahan sebaliknya: "Kemas kini penamaan selepas peristiwa besar (perceraian/kahwin) — wasiat tidak membetulkan penamaan lama" | Klasik: tiada nasihat awal; keluarga bertelingkah dahulu, belajar undang-undang selepas kalah |
| A5 Pengiraan | Pemisahan aset: wang KWSP bernama → penama; baki pusaka → diagih ikut wasiat; kalkulator wasiat/intestat hanya atas baki | Klasik: keluarga beranggapan seluruh harta melalui wasiat |
| A4 Analitis kes | Preseden: *How Yew Hock*, *Krishnaveni*, *Divyyaa*, Fatwa MKI (jika Muslim), Jadual 10 FSA 2013 (insurans) — peta rejim penama lengkap | Klasik: analisis dibuat bar bertahap |
| A7 Dokumen | Nota pentadbiran berasingan bagi aset bernama + checklist "selaraskan wasiat dengan penamaan" (Templat E) | Klasik: tiada dokumen standard |
| Serahan human-in-the-loop | KWSP membayar penama; keluarga menerima/menerima nasihat; mahkamah tidak diperlukan bagi isu kategori | Klasik: mahkamah di peringkat tertinggi diperlukan |
| A6 Orkestrasi | Dwi-laluan: tuntutan penama KWSP + pentadbiran wasiat baki — jejak berasingan | Klasik: satu pertikaian menyatukan semuanya |

#### 4. Jadual perbandingan

| Dimensi | Klasik | Agent (simulasi) |
|---|---|---|
| Kelajuan | Litigasi bertingkat hingga Mahkamah Persekutuan (1996) | Jawapan pada intake — minit, bukan tahun |
| Ketepatan/konsistensi | Betul pada akhirnya — tetapi selepas 3 peringkat mahkamah | Kepastian preseden pada hari pertama; konsisten antara kes |
| Kos | Yuran rayuan bertingkat (tidak direkodkan — jurang) | Kos minimum |
| Kebolehaudit-an | Rekod mahkamah | Audit trail klasifikasi instrumen + citation preseden |
| Risiko pertikaian | Tinggi — kekeliruan asas "wasiat vs penamaan" berterusan hingga kini | Rendah — kedudukan dipapar dengan citation |
| Akses kepakaran | Hanya bar dapat jawapan pasti pada 1996 | Awam dapat jawapan yang sama hari ini, percuma |
| Kepatuhan norma | Rejim penama statutori tidak diperiksa sebelum saman | Norma pra-syarat menyekat saman sia-sia |

#### 5. Penambahbaikan yang agent perkenalkan

1. Pengesanan pertindihan wasiat ↔ penamaan pada intake (bukan selepas saman).
2. Nasihat pencegahan bermusim: "semak penamaan selepas peristiwa besar" — menghapuskan punca kes *How Yew Hock* dan *Krishnaveni* sebelum berlaku.
3. Pemisahan aset bernama daripada harta pusaka dalam semua pengiraan & dokumen.
4. Pendidikan berstruktur (Templat E) mengenai perbezaan rejim KWSP/insurans/Tabung Haji mengikut agama.
5. Standardisasi jawapan bagi isu kategori — membebaskan mahkamah daripada kes deterministik.

#### 6. KELEMAHAN/FLAW proses klasik yang BOLEH DIPERDEBATKAN

1. **Isu kategori dibicarakan di Mahkamah Persekutuan.** Soal bertaraf "adakah X wasiat?" mempunyai jawapan teks statutori; hujah: keperluan litigasi bertingkat mencerminkan kegagalan sistem maklumat, bukan kerumitan undang-undang.
2. **Kekeliruan berulang 28+ tahun.** Selepas *How Yew Hock* (1996), kes *Krishnaveni* (2013) dan *Divyyaa* (2024) timbul atas kekeliruan sama — bukti bahawa penghakiman semata-mata tidak mendidik; ia hanya menyelesaikan kes di hadapannya. Hujah: ilmu yang tidak dimoperasikan tidak mengubah tingkah laku.
3. **Tiada peringatan silang antara instrumen.** Wasiat dan penamaan KWSP diuruskan agensi/pegawai berbeza tanpa mekanisme semakan silang — waris menanggung akibat (RP-06: data silos).
4. **Beban pengetahuan pada pemegang amanah wasi.** Plaintif (pemegang amanah wasi yang dilantik sendiri pewasiat) bertindak atas kefahaman salah — tiada prosedur wajib penerangan kepadanya semasa pelantikan.

#### 7. GUARDRAILS STATUTORI (kes ini)

| Langkah agent | Asas statutori/asas undang-undang | Status |
|---|---|---|
| Klasifikasi penamaan KWSP = berkanun, bukan wasiat | s.54(1A) Akta KWSP 1991; Peraturan 9 EPFR 2001; *How Yew Hock* [1996] 2 MLJ 474 (MP) | ✅ terverifikasi |
| Larangan nasihat "wasiat mengatasi penamaan" | reg. 7(2) EPFR 2001 | ✅ terverifikasi |
| Nasihat insurans nyawa bukan Islam (trust policy / executor) | Akta Perkhidmatan Kewanan 2013 s.130 & Jadual 10 (para 5, 6, 8) | ✅ terverifikasi |
| Nasihat penama Muslim insurans = executor (diagih faraid) | Jadual 10 FSA 2013 para 6 (pemilik polisi Islam); Fatwa MKI 1973/2000 | ✅ terverifikasi |
| Nasihat nominasi KWSP ahli Islam berfungsi sebagai wasi | Fatwa MKI ke-49 (19.9.2000); *Noridah* [2009] 4 ShLR 115 | ✅ terverifikasi |
| Butir peraturan KWSP lama (r.34 Peraturan 1991) | Dirujuk dalam repo via *Krishnaveni* | ⚠️ PERLU SAHKAN teks penuh sebelum dipaparkan sebagai guardrail operasi |

#### 8. VERDICT

**YA — dengan penghormatan kepada fungsi mahkamah.** Kes ini jurang pengetahuan semata-mata: jawapannya deterministik dan telah pun dimuktamadkan oleh Mahkamah Persekutuan 1996; setiap saman seterusnya (2013, 2024) adalah kerosakan maklumat yang boleh dicegah. Agent menghapuskan kelas kes ini. Penghormatan yang jujur: penghakiman *How Yew Hock* itulah yang mencipta kepastian yang agent operasikan — agent tidak menghasilkan undang-undang; ia mengagihkan ilmu yang mahkamah sudah bayar mahal untuk terbitkan. Nilai tambah agent ialah **pengagihan ilmu deterministik pada kos sifar**, satu fungsi yang proses klasik tidak pernah lakukan dengan cekap.

---

### KES 5 — Kes Moorthy / *Kaliammal a/p Sinnasamy lwn MAIWP* [2006] 1 MLJ 685 (mualaf; tiada forum)

#### 1. Kes & isu

**Mahkamah:** Mahkamah Tinggi Kuala Lumpur (Raus Sharif J, 28 Disember 2005); kemudian Mahkamah Rayuan (R1-24-102 of 2005; penghakiman direkodkan 20 Ogos 2010). Proceeding sampingan: Mahkamah Tinggi Syariah KL (perintah ex parte 22 Disember 2005). **Fakta (dari repo):** M. Moorthy (36; bekas askar, pendaki Everest) meninggal 20 Disember 2005 di HKL. Balunya Kaliammal menyatakan suaminya Hindu; 21 Disember beliau memfailkan OS di Mahkamah Tinggi KL memohon antara lain: pengisytiharan beliau isteri sah, si mati Hindu dan bukan Islam semasa mati, dokumen pemelukan batal, perintah hospital melepaskan jenazah, dan injunksi terhadap JAWI. Keesokan harinya JAWI memperoleh perintah ex parte Mahkamah Syariah — si mati diisytiharkan Islam dan hendaklah dikebumikan mengikut undang-undang Islam — **tanpa Kaliammal dinamakan atau dimaklumkan**. **Isu:** Adakah Mahkamah Tinggi Sivil berkuasa menyemak perintah Mahkamah Syariah atas status agama si mati dan hak pengebumian. [Sumber: NECF Malaysia, "The Moorthy Story" — https://www.necf.org.my/view_file.cfm?fileid=125, dicapai 2026-10-31; Supreme Today AI (MarsdenLR 2026 87009) — https://supremetoday.ai/doc/judgement/MYS00000122174, dicapai 2026-10-31; Moustafa, *Constituting Religion* (Cambridge UP) — https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A42E97B1E10D72643D1E23C3D523E2AC/9781108423946c5_91-123.pdf/constructing-the-political-spectacle.pdf, dicapai 2026-10-31]

#### 2. Penyelesaian KLASIK (apa yang sebenarnya berlaku)

- **Laluan:** dua prosiding berjalan serentak dalam dua hari — OS balu di Mahkamah Tinggi Sivil (21 Dis) vs permohonan ex parte JAWI di Mahkamah Syariah (22 Dis). Mahkamah Tinggi membenarkan SATU permohonan (Kaliammal isteri sah) dan menolak selebihnya: tiada bidang kuasa menyemak, memansuhkan atau mengenepikan perintah Mahkamah Syariah. Jenazah diserahkan dan dikebumikan mengikut rite Islam di Tanah Perkuburan Islam Taman Ibukota, Gombak **petang itu juga**.
- **Hasil:** balu bukan Islam "was denied recourse to any legal forum" (per luaran akademik dalam repo) — beliau tidak berpihak dalam prosiding syariah (bukan Islam) dan mahkamah sivil menolak semakan. Keputusan akhir rayuan (penghakiman direkodkan 20 Ogos 2010) **PERLU SAHKAN** — teks penuh tidak berjaya dicapai (halaman captcha).
- **Tempoh & kos:** tidak direkodkan (jurang); yang jelas direkodkan — keluarga kehilangan jenazah dalam ±2 hari tanpa diri didengar.
- **Komplikasi:** status agama si mati membekukan pentadbiran pusaka (rejim faraid vs Akta Pembahagian 1958 bergantung status); nasib harta pusaka Moorthy selepas pengebumian (KWSP, GHB dsb.) **tiada laporan boleh diakses** (Gaps civil-cases butir 6); kes mencetuskan kemarahan awam dan perdebatan dasar.

#### 3. Simulasi penyelesaian AGENT (A1–A8, ikut jurnal §6.5) — dengan pengakuan had yang jujur

| Langkah | Tindakan agent | APA YANG BERBEZA vs klasik |
|---|---|---|
| A3 Klasifikasi | Intake sejurus kematian: status agama si mati DIPERSOALKAN → flag risiko tertinggi; agent memetakan serta-merta kedua-dua senario (si mati Islam → faraid + sijil faraid; bukan Islam → Akta Pembahagian 1958) dan keperluan bertindak pantas sebelum perintah ex parte (pelajaran praktikal repo) | Klasik: keluarga bertindak dalam kegelapan maklumat; ex parte didapati 24 jam kemudian |
| A8 Norma pra-syarat | Norma status: Perkara 121(1A) — mahkamah sivil tiada bidang kuasa atas perkara bidang kuasa syariah; MAHKAMAH SIVIL SENDIRI menentukan sempadannya (*Indira Gandhi* [2018]; *SIS* [2022] — semakan kehakiman kekal dengan Mahkamah Tinggi Sivil) | Klasik (2005): kedudukan pasca-*Indira/SIS* belum wujud — nasihat era itu tiada |
| A1/A2 Nasihat | A1: peta laluan lengkap — apa yang boleh dan tidak boleh disemak; kelewatan bertindak berbahaya; A2: senarai bukti status (rekod pemelukan, dokumen, keterangan) yang perlu dikumpul SEKARANG (kontras *Nyonya Tahir* — keterangan anak bukan Islam diterima MTS Seremban atas dokumen kukuh) | Klasik: keluarga tidak tahu ex parte boleh berlaku tanpa mereka; bukti dikumpul lewat |
| A5 Pengiraan | Dua jadual bersyarat (faraid / Akta 300) sedia — tidak boleh dilaksanakan sehingga status ditetapkan | Klasik: tiada gambaran sandaran |
| A4 Analitis kes | Preseden: *Nyonya Tahir* (penentuan status atas fakta; keterangan waris bukan Islam boleh diterima), *Wee Ku Wing* (waris mualaf kekal "child" di bawah Akta 1958), *MAIWP v Lim Ee Seng* (waris bukan Islam tiada beneficial interest dalam pusaka Islam) | Klasik: analisis pasca-peristiwa oleh peguam |
| A7 Dokumen | Checklist bukti status agama + draf OS/permohonan yang lengkap (bukti dokumen + saksi) sebelum ex parte diambil pihak lain | Klasik: OS balu difailkan sehari sebelum ex parte lawan — kalah laluan |
| Serahan human-in-the-loop | Mahkamah (sivil/syariah) memutuskan status; JAWI/MdI mahkamah syariah memutuskan pengebumian; **agent TIDAK dapat menambah forum yang tiada** | Kedudukan sama — kelemahan struktur, bukan proses |
| A6 Orkestrasi | Selepas status ditetapkan: ejen bertukar mod (faraid vs Akta 300) tanpa memulakan semula dari kosong; jejak semua prosiding | Klasik: pentadbiran terhenti serta-merta pada pertikaian status |

**Pengakuan had yang jujur:** agent TIDAK boleh (i) menghalang permohonan ex parte pihak lain, (ii) memberi Kaliammal forum yang tiada pada 2005, atau (iii) menyemak perintah syariah. Yang agent boleh: kelajuan maklumat, kesediaan bukti, dan peta akibat. Perkembangan undang-undang pasca-2005 (*Indira Gandhi* [2018]; *SIS* [2022]) menunjukkan struktur telah berubah — dan peta itulah yang agent papar hari ini.

#### 4. Jadual perbandingan

| Dimensi | Klasik | Agent (simulasi) |
|---|---|---|
| Kelajuan | Keluarga kalah dalam ±2 hari (ex parte 22 Dis → pengebumian petang sama) | Maklumat penuh dalam masa jam; persediaan bukti segera — tetapi TIDAK mengubah keputusan ex parte |
| Ketepatan/konsistensi | Hukum betul mengikut era (121(1A) pra-*Indira*) tetapi hasil tanpa forum | Peta hukum semasa (pasca-*Indira/SIS*) dipapar; konsisten |
| Kos | Tidak direkodkan; litigasi + kos emosi | Kos nasihat minimum; litigasi mungkin masih perlu |
| Kebolehaudit-an | Tiada jejak untuk keluarga | Audit trail klasifikasi & nasihat bertarikh |
| Risiko pertikaian | Maksimum — status dipertikaikan dalam krisis, bukan dirancang | Sama pada isu status; TETAPI risiko pentadbiran pasca-status lebih rendah (mod bertukar pantas) |
| Akses kepakaran | Tiada pada saat krisis (masa ±24 jam) | Nasihat 24/7 bercitation |
| Kepatuhan norma | Norma bidang kuasa dikesan secara litigasi | Norma dipapar sebelum tindakan |

#### 5. Penambahbaikan yang agent perkenalkan

1. Flag risiko status-agama sejurus kematian dengan senarai tindakan kecemasan (kumpul bukti status sekarang — pelajaran repo: "kumpul bukti status awal dan bertindak pantas").
2. Peta dwi-senario (Islam/bukan Islam) dengan jadual pengiraan bersyarat kedua-dua rejim.
3. Paparan kedudukan undang-undang SEMASA (pasca-*Indira Gandhi* [2018] & *SIS* [2022]: semakan kehakiman kekal dengan mahkamah sivil) — membetulkan kefahaman awam yang beku pada era Moorthy.
4. Pencegahan pentadbiran: senarai waris Borang A mestilah memasukkan SEMUA anak sah taraf tanpa mengira agama (*Wee Ku Wing*) — pengguguran waris membatalkan perintah.
5. Orkestrasi pasca-status: pertukaran mod faraid ↔ Akta 300 tanpa memulakan pentadbiran semula.

#### 6. KELEMAHAN/FLAW proses klasik yang BOLEH DIPERDEBATKAN

1. **Prosesiding ex parte tanpa notis kepada pihak terkesan.** Perintah Mahkamah Syariah 22 Dis 2005 diperoleh tanpa Kaliammal dinamakan atau dimaklumkan — padahal balu bukan Islam TIDAK boleh menjadi pihak dalam prosiding syariah (kekejaman struktur yang kemudiannya diredakan sebahagiannya melalui kontras *Nyonya Tahir*: keterangan waris bukan Islam diterima atas dokumen kukuh). Hujah: sistem yang mengebumikan jenazah dalam pertikaian sebelum pihak berkepentingan didengar boleh dipertikaikan dari segi prosedural fairness.
2. **Tiada forum berkesan bagi keluarga bukan Islam pada 2005.** Mahkamah sivil menolak semakan; mahkamah syariah tidak terbuka kepada bukan Islam — "denied recourse to any legal forum". Hujah: jurang forum ialah kelemahan reka bentuk perlembagaan yang hanya dirawat sebahagian oleh *Indira Gandhi* [2018] dan *SIS* [2022].
3. **Kelajuan asimetri.** Pihak yang tahu prosedur (JAWI) bergerak dalam 24 jam; keluarga yang tidak tahu kalah sebelum mula — kelemahan keadilan prosedural bagi pihak tanpa peguam.
4. **Kesan beku ke atas pentadbiran pusaka.** Pertikaian status membekukan seluruh pentadbiran; nasib harta Moorthy tidak direkodkan setahun-tahun (Gaps butir 6) — hujah: tiada mekanisme klasik yang menguruskan harta sementara status dipertikaikan.
5. **Ketiadaan penerangan awam dwi-jurisdiction** — keluarga tidak tahu bahawa status agama si mati menentukan keseluruhan rejim pusaka sehingga krisis berlaku (RP-03, KUAT).

#### 7. GUARDRAILS STATUTORI (kes ini)

| Langkah agent | Asas statutori/asas undang-undang | Status |
|---|---|---|
| Larangan nasihat "mahkamah sivil boleh semak perintah syariah atas status" (era pra-2018) | Perkara 121(1A) Perlembagaan Persekutuan (kuat kuasa 10 Jun 1988); *Kaliammal* [2006] 1 MLJ 685 | ✅ terverifikasi |
| Nasihat semakan kehakiman kekal dengan Mahkamah Tinggi Sivil | *Indira Gandhi* [2018] 1 MLJ 545; *SIS* [2022] 3 MLRA 131 | ✅ terverifikasi |
| Nasihat status agama si mati menentukan rejim pusaka | Prinsip *Kaliammal/Moorthy* + *Nyonya Tahir* [2006] 1 CLJ (Sya) 335 | ✅ terverifikasi (preseden) |
| Nasihat agama SI MATI (bukan waris) menentukan undang-undang terpakai bagi pusaka bukan Islam | s.2 Akta Pembahagian 1958 (mengecualikan harta orang Islam, bukan waris); *Wee Ku Wing* (MR 2026) | ✅ terverifikasi |
| Nasihat waris bukan Islam tiada beneficial interest dalam pusaka Islam | *Re Timah* [1941] MLJ 51; *MAIWP v Lim Ee Seng* [2000] 2 MLJ 572 | ✅ terverifikasi (preseden) |
| Kedudukan undang-undang keluarga pasca-mualaf (forum tuntutan) | Bergantung akta perkahwinan (LRA 1976 vs enakmen Islam) | ✅ terverifikasi (kerangka; USIM) |
| Keputusan akhir rayuan Kaliammal (MR, direkodkan 20.8.2010) | Teks penuh tidak dicapai | ⚠️ PERLU SAHKAN — TIDAK digunakan sebagai guardrail |

#### 8. VERDICT

**TIDAK — untuk isu utama kes ini; SEBAHAGIAN — untuk pentadbiran pasca-status.** Kejujuran mutlak diperlukan di sini: **kelemahan terburuk kes Moorthy (tiada forum, ex parte tanpa notis, kehilangan jenazah dalam 48 jam) berada di luar kuasa mana-mana agent** — ia kelemahan struktur perlembagaan yang hanya badan perundangan/mahkamah boleh ubah (dan sebahagianya telah diubah melalui *Indira Gandhi* [2018] & *SIS* [2022]). Agent tidak menawarkan penyelesaian kepada tragedi itu; ia hanya menawarkan keluarga peta maklumat dan kesediaan bukti dalam masa jam. Di mana agent benar-benar membantu ialah pentadbiran selepas status ditetapkan (pertukaran mod faraid/Akta 300 yang pantas, pencegahan pengguguran waris mualaf daripada Borang A). Propaganda pro-agent di sini akan tidak jujur: ini kes di mana **reformasi undang-undang, bukan automasi, ialah penyelesaian sebenar**.

---

### KES 6 — *MAIWP v Lim Ee Seng* [2000] 2 MLJ 572 (bukan Islam mewarisi harta orang Islam)

#### 1. Kes & isu

**Mahkamah:** Mahkamah (kes probat — dilaporkan sebagai [2000] 2 MLJ 572; tahap mahkamah dalam repo tidak diperincikan — jurang). **Fakta (dari repo):** Si mati, Chew Toong Lee @ Ali Cheow bin Abdullah, memeluk Islam pada 23 Januari 1973 dan meninggal dunia pada 28 Julai 1988 sebagai orang Islam. Surat kuasa mentadbir harta pusakanya dikeluarkan kepada Lim Ee Seng (bekas isteri di bawah undang-undang sivil) dan seorang anak perempuan. MAIWP mencabar pemberian itu. **Isu:** Bolehkah bukan Islam (isteri sivil & anak) mewarisi harta orang Islam melalui SKM sivil. [Sumber: The administration of Muslim's and non-Muslim's ownerless estate (bona vacantia) in West Malaysia (artikel akademik) — https://scispace.com/pdf/the-administration-of-muslim-s-and-non-muslim-s-ownerless-2opoaqbmz3.pdf, dicapai 2026-10-31]

#### 2. Penyelesaian KLASIK (apa yang sebenarnya berlaku)

- **Laluan:** SKM dikeluarkan terlebih dahulu kepada keluarga sivil (isteri & anak perempuan) → MAIWP mencabar → mahkamah memutuskan — iaitu **geran dikeluarkan dahulu, dicabar kemudian**. 
- **Hasil:** memandangkan si mati meninggal sebagai orang Islam dan defendan bukan Islam, prinsip "orang bukan Islam dilarang mewarisi harta orang Islam" terpakai — defendan tiada faedah benefisial (beneficial interest) dalam harta si mati, dan mahkamah memerintahkan harta diserahkan kepada MAIWP. Asas berturut-turut kepada *Re Timah Binti Abdullah* [1941] MLJ 51 (mazhab Syafie di Malaya; "an infidel is excluded from and cannot succeed to the estate of a Muhammadan"). Statut sivil menyokong: Akta Pembahagian 1958 tidak terpakai kepada harta orang Islam (s.2).
- **Tempoh & kos:** tidak direkodkan (jurang). Si mati meninggal 1988; kes dilaporkan [2000] — pentadbiran keluarga terganggu ±12 tahun selepas kematian sebelum kepastian muktamad (tempoh prosiding sebenar tidak direkod — jurang).
- **Komplikasi:** keluarga sivil telah mentadbir (atau berazam mentadbir) di bawah SKM yang kemudian terjejas; harta akhirnya ke Baitulmal (MAIWP) — hasil yang keras dari perspektif keluarga; kes menunjukkan pemberian geran pentadbiran sivil TIDAK menetapkan hak faraid substantif.

#### 3. Simulasi penyelesaian AGENT (A1–A8, ikut jurnal §6.5)

| Langkah | Tindakan agent | APA YANG BERBEZA vs klasik |
|---|---|---|
| A3 Klasifikasi | Intake: status agama si mati = Islam (rekod pemelukan 1973) waris pemohon = bukan Islam → **flag automatik risiko "tiada beneficial interest"** sebelum SKM dimohon | Klasik: SKM dikeluarkan tanpa semakan silang status; cabaran MAIWP datang kemudian |
| A8 Norma pra-syarat | Norma repo: (i) Akta Pembahagian 1958 tidak terpakai kepada harta orang Islam (s.2); (ii) prinsip *Re Timah*/*Lim Ee Seng* — bukan Islam tidak mewarisi harta Islam; (iii) prinsip kebalikan *Wee Ku Wing* — waris mualaf KEKAL benefisiari pusaka bukan Islam (asimetri direkodkan jelas) | Klasik: norma hanya ditemui melalui cabaran MAIWP selepas geran |
| A1/A2 Nasihat | A2: analisis waris Muslim si mati (adakah wujud waris faraid — isteri Islam kedua? anak Islam? — fakta tidak direkodkan dalam repo; jika tiada waris Muslim, laluan vesting/Baitulmal); A1: nasihat jujur kepada keluarga sivil tentang kedudukan undang-undang SEBELUM mereka membelanjakan masa/wang pentadbiran | Klasik: keluarga mendapat kepastian hanya selepas MAIWP mencabar |
| A5 Pengiraan | Jika wujud waris Islam: jadual faraid deterministik; jika tiada: laluan pengiraan Baitulmal — A5 tidak mengira bahagian kepada pihak yang tiada hak | Klasik: pengiraan dibuat atas anggapan keluarga yang kemudiannya terbatal |
| A4 Analitis kes | Preseden: *Re Timah* (1941), *Lim Ee Seng* (2000), *Wee Ku Wing* (2026 — arah bertentangan bagi pusaka BUKAN Islam) — peta asimetri lengkap dipapar | Klasik: analisis per mahkamah |
| A7 Dokumen | Draf permohonan yang betul dari mula (pemohon yang layak; peruntukan ARB/MdI bagi pusaka tanpa waris Muslim); senarai bukti waris faraid untuk MdI | Klasik: dokumen disediakan atas premis salah |
| Serahan human-in-the-loop | Mahkamah/MAIWP/Baitulmal memutuskan hak muktamad; MdI mengesahkan waris faraid | Kedudukan sama |
| A6 Orkestrasi | Jejak: penetapan waris Islam → sijil faraid → pentadbiran/vesting — tiada pentadbiran sia-sia oleh keluarga yang tiada hak | Klasik: keluarga mentadbir kemudian kehilangan semuanya |

#### 4. Jadual perbandingan

| Dimensi | Klasik | Agent (simulasi) |
|---|---|---|
| Kelajuan | Geran dikeluarkan → dicabar → kepastian ±12 tahun selepas kematian (angka kasar; tempoh prosiding tidak direkod) | Kedudukan diketahui pada intake — keluarga dapat kepastian dalam masa hari |
| Ketepatan/konsistensi | Prinsip konsisten (*Re Timah* 1941 → *Lim Ee Seng* 2000) tetapi tidak disemak pra-geran | Norma pra-syarat menyekat permohonan salah dari mula |
| Kos | Kos pentadbiran keluarga + litigasi cabaran, akhirnya sia-sia bagi keluarga | Kos minimum; elak pentadbiran atas premis salah |
| Kebolehaudit-an | Rekod mahkamah | Audit trail status agama + klasifikasi waris bercitation |
| Risiko pertikaian | Tinggi — geran sedia ada dicabar MAIWP | Rendah — cabaran dicegah ex ante |
| Akses kepakaran | Prinsip asimetri jauh daripada pengetahuan awam | Peta asimetri (Islam→bukan Islam vs bukan Islam→mualaf) dipapar |
| Kepatuhan norma | s.2 Akta 300 tidak disemak sebelum geran | A8 menguatkuasakan pengecualian itu pada intake |

#### 5. Penambahbaikan yang agent perkenalkan

1. Semakan status agama si mati + status agama calon waris pada intake — flag asimetri pewarisan sebelum pemfailan.
2. Nasihat jujur awal kepada keluarga bukan Islam tentang tiada beneficial interest — mencegah pembaziran pentadbiran & litigasi.
3. Laluan alternatif dipetakan serta-merta (ARB/MdI bagi pusaka tanpa waris Muslim; vesting Baitulmal) — kepatuhan tanpa penderitaan prosedural.
4. Pencegahan penerbitan SKM yang pasti dicabar — menjimatkan sumber mahkamah & MAIWP.
5. Pendidikan awam tentang asimetri dwi-hala (diperlengkap *Wee Ku Wing*).

#### 6. KELEMAHAN/FLAW proses klasik yang BOLEH DIPERDEBATKAN

1. **Geran dikeluarkan sebelum hak substantif disemak.** Mesinari sivil boleh mengeluarkan SKM tanpa menyemak prinsip faraid substantif — hasilnya geran yang terpakai dicabar selepas keluarga melabur usaha/kos. Hujah: pintu pentadbiran sivil yang tidak berkomunikasi dengan hukum substantif ialah kelemahan reka bentuk dwi-jurisdiction.
2. **Kepastian terlambat bagi pihak paling lemah.** Keluarga sivil (isteri & anak) menunggu ±12 tahun untuk tahu mereka tiada hak — hujah: sistem yang membenarkan seseorang mentadbir harta yang bukan haknya (kerana tiada penerangan) kemudian menarik semula semuanya tidak adil dari segi proses, walaupun betul dari segi hukum.
3. **Asimetri tidak didokumenkan secara awam.** Bahawa waris bukan Islam tidak mewarisi orang Islam TETAPI waris mualaf mewarisi bukan Islam (*Wee Ku Wing*) — kedudukan asimetri ini tidak terdapat dalam mana-mana risalah agensi awam dalam repo; hanya dalam penghakiman.
4. **Tiada laluan maklumat pra-geran antara MAIS/MdI dan pejabat probat** — cabaran datang selepas geran, bukan semakan sebelum geran (sekali lagi jurang protokol rujuk-balik, Gaps jurisdiction butir 1).

#### 7. GUARDRAILS STATUTORI (kes ini)

| Langkah agent | Asas statutori/asas undang-undang | Status |
|---|---|---|
| Pengecualian harta orang Islam daripada Akta Pembahagian 1958 | s.2 Distribution Act 1958 [Act 300] | ✅ terverifikasi |
| Nasihat larangan pewarisan bukan Islam → orang Islam | *Re Timah* [1941] MLJ 51; *MAIWP v Lim Ee Seng* [2000] 2 MLJ 572 | ✅ terverifikasi (preseden) |
| Nasihat waris mualaf kekal "child" (pusaka bukan Islam) | s.2 & s.3 (takrif "child") Akta Pembahagian 1958; *Wee Ku Wing* (MR 2026) | ✅ terverifikasi |
| Nasihat vesting/tuntutan MdI/ARB bagi pusaka tanpa waris | s.81 Akta Probet dan Pentadbiran 1959 (LA kepada ARB selepas 6 bulan); s.39 PAA (harta intestat vest dalam ARB); s.13, s.17 Akta 532 | ✅ terverifikasi |
| Nasihat senarai pemohon PPKP termasuk MdI | Senarai pemohon Akta 98 (JBG/JKPTG) | ✅ terverifikasi |
| Hadis larangan Muslim–kafir (rujukan dalam *Wee Ku Wing*) tidak dikanunkan dalam Akta 1958/enakmen Kelantan | Penghakiman MR dalam repo | ✅ terverifikasi (dalam konteks kes; agent memetik sebagai fakta penghakiman, bukan hukum baharu) |
| Kuasa MAIWP bertindak sebagai wasi/pentadbir | Enakmen pentadbiran undang-undang Islam negeri (cth. s.5(4) Enakmen Selangor — dirujuk dalam repo) | ⚠️ PERLU SAHKAN nombor seksyen bagi setiap negeri sebelum dipaparkan |

#### 8. VERDICT

**SEBAHAGIAN.** Agent lebih baik dalam satu dimensi yang besar: **kepastian awal** — keluarga mengetahui kedudukan undang-undang (tiada beneficial interest) pada hari pertama, bukan ±12 tahun kemudian; ini menghapuskan pentadbiran & litigasi yang sia-sia, dan memetakan laluan alternatif yang sah. Tetapi dua pengakuan jujur: (i) **hasil substantif tidak berubah** — harta tetap ke Baitulmal; agent memoperasikan hukum yang keras bagi keluarga ini, dan keadilan hasil itu di luar kuasa agent (ia soal hukum substantif & dasar, bukan proses); (ii) **pemberian geran pentadbiran sivil tidak menjamin hak substantif** — itu cabaran struktur yang hanya mahkamah/badan perundangan boleh rawat (cth. skema penyelesaian atau pindaan). Agent tidak menambah hak; ia hanya menghalang pembaziran mengejar hak yang tiada.

---

### KES 7 — Rayuan perintah pusaka kecil s.29 Akta 98 (situasi administratif; 30 hari, A1643)

#### 1. Situasi & isu

**Bukan kes bernama tunggal** — situasi administratif berulang yang direkodkan dalam repo: pihak yang tidak berpuas hati dengan perintah Pegawai Pembahagian Pusaka (Pentadbir Tanah) merayu ke Mahkamah Tinggi; keputusan Mahkamah Tinggi **muktamad** [Sumber: Panduan JBG, JPM — https://www.jbg.gov.my/images/doc/risalah/2026/19.%20Panduan%20Permohonan%20Tuntutan%20Pembahagian%20Harta%20Pusaka%20Kecil.pdf, dicapai 2026-10-31]. Tiada kes rayuan s.29 dengan alasan penghakiman penuh yang berjaya dicapai percuma dalam repo (Gaps civil-cases butir 5) — kes berkaitan yang direkodkan: *Wee Ku Wing lwn Amira* (rayuan s.29 hanya untuk pihak dalam perbicaraan; MR 2026) dan *Ahmad bin Abd Majeed lwn Habibah* (s.29 bukan satu-satunya remedi; citation penuh PERLU SAHKAN). **Isu utama:** tempoh rayuan — risalah rasmi JBG menyatakan **14 hari**, teks akta selepas pindaan menyatakan **30 hari**; jurang ini kini diselesaikan dalam `gap-mission-undang-undang.md` Misi 1.

#### 2. Penyelesaian KLASIK (apa yang sebenarnya berlaku)

- **Laluan:** waris menerima perintah pembahagian Borang E → tidak berpuas hati → merayu **melalui Pegawai Pembahagian Pusaka** ke Mahkamah Tinggi (s.29(1) Akta 98); pegawai menahan perintah sepanjang tempoh rayuan (s.16(1) Act 98 — perintah "shall lie in his office for the period within which notice of appeal may be given"); keputusan Mahkamah Tinggi muktamad.
- **Kekeliruan tempoh (diselesaikan Misi Jurang 1):** **(i) Teks semasa** — perintah pada/Selepas 15 Julai 2024: "may appeal to the High Court **within thirty days** from the date the order, decision or act is made or done" (pindaan s.23(a) Akta A1643); prosedur rayuan mengikut Kaedah Mahkamah Mahkamah Tinggi (s.23(b) menggantikan s.29(2)) [Sumber: mylaw.my — SEDA s.29 — https://mylaw.my/legislation/small-estates-distribution-act-1955/section-29, dicapai 2026-10-31; mylaw.my — A1643 — https://mylaw.my/legislation/akta-harta-pusaka-kecil-pembahagian-pindaan-2022, dicapai 2026-10-31]. **(ii) Punca angka 14 hari** — teks pra-pindaan s.29(2) (cetak semula 2006): tempoh & prosedur ikut rayuan sivil daripada Mahkamah Sesyen (lazimnya 14 hari menurut amalan) [Sumber: JKPTG — Act 98 Reprint 2006 — https://www.jkptg.gov.my/images/pdf/perundangan-tanah/Act_98.pdf, dicapai 2026-10-31]. **(iii) Klausa simpanan** — rayuan atas perintah sebelum 15.7.2024 diteruskan seolah-olah s.29 tidak dipinda (s.25(3) A1643).
- **Kos & tempoh:** fi perintah pembahagian P.U.(A) 194/2024 (≤RM1,000 → RM30; RM1,000–RM50,000 → RM50; RM50,001–RM2 juta → 0.2%; RM2 juta–RM5 juta → 0.3%) [Sumber: AGC — P.U.(A) 194/2024 — https://lom.agc.gov.my/ilims/upload/portal/akta/outputp/2209997/PUA%20194_2024.pdf, dicapai 2026-10-31]; keseluruhan proses pusaka kecil 4–6 bulan (JKPTG FAQ; tempoh standard 4 bulan, Parlimen Jan 2026) — rayuan pula menambah peringkat Mahkamah Tinggi (tempoh rayuan tidak diterbitkan — jurang).
- **Komplikasi:** waris pada zaman peralihan menerima maklumat **percanggahan daripada dua sumber rasmi** (risalah JBG "14 hari" vs akta dipinda "30 hari"); Borang K1 lama dipotong oleh P.U.(A) 194/2024, rayuan kini ikut prosedur Mahkamah Tinggi [Sumber: Solusi Pusaka — https://solusipusaka.com/borang-borang-di-bawah-akta-pembahagian-harta-pusaka-kecil-1995/, dicapai 2026-10-31]; tiada statistik rayuan s.29 diterbitkan (Gaps lessons butir 4).

#### 3. Simulasi penyelesaian AGENT (A1–A8, ikut jurnal §6.5)

| Langkah | Tindakan agent | APA YANG BERBEZA vs klasik |
|---|---|---|
| A3 Klasifikasi | Input: tarikh perintah + status pihak (adakah pemohon pihak dalam perbicaraan pusaka kecil?) → klasifikasi laluan remedi: **(a)** pihak dalam bicara → rayuan s.29; **(b)** pihak disisih → saman pemula (*Wee Ku Wing*; *Ahmad Abd Majeed*) | Klasik: waris tidak tahu laluan mana terpakai; sesetengah merayu s.29 dan ditolak kerana bukan pihak bicara |
| A8 Norma pra-syarat | **Percabangan tarikh deterministik (diprogram)**: perintah pada/Selepas 15.7.2024 → tempoh **30 hari** (A1643 s.23; berkuat kuasa 15.7.2024 [P.U.(B) 267/2024]); perintah sebelum itu → tafsir lama (tempoh rayuan Sessions Court; nilai tepat **PERLU SAHKAN** teks s.46 CJA 1964 — dipapar DENGAN flag, bukan sebagai kepastian) | Klasik: waris membaca risalah JBG usang (14 hari) atau tidak tahu pindaan langsung → risiko rayuan terlewat masa |
| A1 Nasihat | Nasihat bercitation dengan kedua-dua teks (semasa & pra-pindaan) + amaran eksplisit: "tempoh pra-pindaan PERLU SAHKAN dengan peguam/PPKP sebelum difailkan" | Klasik: maklumat berselerak dalam risalah, pekeliling & akta — tiada satu pun menjelaskan percanggahan |
| A5 Pengiraan | Kalkulator tarikh: tarikh perintah + 30 hari → tarikh akhir rayuan, dikira automatik & dipaparkan | Klasik: waris mengira sendiri; risiko ralat manusia atas tempoh muktamad |
| A4 Analitis kes | Preseden: *Wee Ku Wing* (s.29 terhad kepada pihak bicara), *Ahmad Abd Majeed* (samaran pemula kekal tersedia) — ditanda status sumber (nota akademik; citation penuh PERLU SAHKAN) | Klasik: analisis preseden tidak tersedia kepada waris awam |
| A7 Dokumen | Draf notis rayuan + senarai dokumen (salinan perintah Borang E, bukti status pihak, asas ketidakpuasan) untuk diserahkan MELALUI Pegawai Pembahagian Pusaka | Klasik: borang berpindah-pindah; tiada senarai semak standard |
| Serahan human-in-the-loop | Pegawai & Mahkamah Tinggi memutuskan rayuan; waris menandatangani & menyerah sendiri | Kedudukan sama |
| A6 Orkestrasi | **Penjejak tempoh automatik**: peringatan berperingkat (hari-1, hari-7, hari-25) sebelum tarikh akhir; jejak status rayuan sehingga keputusan muktamad MT | Klasik: tiada peringatan; waris yang terlewat tempoh kehilangan remedi selamanya (keputusan MT muktamad) |

#### 4. Jadual perbandingan

| Dimensi | Klasik | Agent (simulasi) |
|---|---|---|
| Kelajuan | Waris mencari-cari maklumat tempoh daripada pelbagai sumber; risiko rayuan terlewat | Tempoh dikira & dipaparkan saat perintah dikeluarkan; peringatan automatik |
| Ketepatan/konsistensi | Dua sumber rasmi bertentangan (14 vs 30 hari) — waris mungkin bertindak atas maklumat usang | Percabangan tarikh deterministik; sumber usang (risalah JBG) DILARANG dipaparkan bagi perintah baharu (Implikasi Misi 1) |
| Kos | Kos rayuan + risiko hilang remedi jika terlewat tempoh | Kos minimum; remedi dipelihara |
| Kebolehaudit-an | Tiada jejak; tiada statistik rayuan diterbitkan | Audit trail tarikh perintah, pengiraan tempoh, peringatan |
| Risiko pertikaian | Sederhana — tetapi risiko PROSEDURAL tinggi (laluan salah: s.29 vs saman pemula) | Rendah — laluan remedi diklasifikasi pada intake |
| Akses kepakaran | Bergantung peguam/pegawai | Nasihat bercitation + kalkulator percuma |
| Kepatuhan norma | Norma tempoh tidak dimoperasikan — hanya ditulis | A8 menguatkuasakan tempoh sebagai norma operasi dengan peringatan |

#### 5. Penambahbaikan yang agent perkenalkan

1. Percabangan tarikh perintah (pra/pasca 15.7.2024) sebagai logik program — menghapuskan kekeliruan 14 vs 30 hari.
2. Kalkulator tarikh akhir rayuan + penjejak tempoh dengan peringatan berperingkat.
3. Klasifikasi laluan remedi (rayuan s.29 vs saman pemula) berdasarkan status pihak dalam perbicaraan (*Wee Ku Wing*).
4. Sekatan paparan maklumat usang (risalah "14 hari") bagi perintah baharu — disiplin ilmu yang proses klasik tiada.
5. Flag PERLU SAHKAN dipaparkan terang-terang bagi tempoh pra-pindaan — kejujuran epistemik sebagai ciri produk.

#### 6. KELEMAHAN/FLAW proses klasik yang BOLEH DIPERDEBATKAN

1. **Dua sumber rasmi bertentangan selama bertahun-tahun.** Risalah JBG (14 hari) terus beredar selepas akta dipinda (30 hari, berkuat kuasa 15.7.2024) — hujah: agensi yang mengeluarkan risalah usang selepas pindaan akta menyebabkan waris kehilangan remedi konstitusional mereka melalui kecuaian dokumen, bukan melalui undang-undang.
2. **Tempoh rayuan pra-pindaan tidak dinyatakan dalam akta sendiri** — s.29(2) lama menyerahkan kepada "tempoh rayuan daripada Mahkamah Sesyen" — hujah: parlimen membiarkan tempoh hak rayuan ditentukan oleh rujukan silang yang hanya peguam dapat selesaikan; ini kelemahan penggubalan.
3. **Kehilangan remedi tanpa peringatan.** Tiada apa-apa mekanisme agensi yang memberitahu waris tarikh akhir rayuan mereka — sebaliknya pegawai hanya "menahan perintah" (s.16(1)); hujah: sistem yang mengetahui tarikh luput remedi tetapi tidak memberi amaran adalah sistem yang membiarkan hak luput secara senyap.
4. **Tiada statistik rayuan diterbitkan** — tiada cara menilai sama ada backlog rayuan, kadar kejayaan, atau punca kegagalan (Gaps lessons butir 4); hujah: proses awam yang tidak diukur tidak boleh diperbaiki.
5. **Klasifikasi remedi bergantung pengetahuan preseden** — bahawa pihak disisih mesti guna saman pemula (*Wee Ku Wing*; *Ahmad Abd Majeed*) bukan maklumat yang tersedia di pejabat pusaka kecil.

#### 7. GUARDRAILS STATUTORI (situasi ini)

| Langkah agent | Asas statutori/asas undang-undang | Status |
|---|---|---|
| Nasihat tempoh rayuan 30 hari (perintah pada/Selepas 15.7.2024) | s.29(1) Akta 98 (sebagaimana dipinda oleh s.23(a) Small Estates (Distribution) (Amendment) Act 2022 [A1643]) | ✅ terverifikasi |
| Nasihat prosedur rayuan ikut Kaedah Mahkamah Mahkamah Tinggi | s.29(2) Akta 98 (diganti s.23(b) A1643) | ✅ terverifikasi |
| Nasihat rayuan pra-15.7.2024 diteruskan mengikut undang-undang lama | s.25(3) A1643 (klausa simpanan) | ✅ terverifikasi |
| Nasihat pegawai menahan perintah sepanjang tempoh rayuan | s.16(1) Akta 98 (cetak semula 2006) | ✅ terverifikasi |
| Nasihat keputusan Mahkamah Tinggi muktamad | Kerangka s.29 (Panduan JBG) | ✅ terverifikasi |
| Tarikh berkuat kuasa A1643 (15.7.2024) | P.U. (B) 267/2024 — dilaporkan melalui LawPlayer/mylaw; warta asal belum dibuka terus | ⚠️ PERLU SAHKAN — dipapar dengan flag sehingga warta disemak |
| Nilai tepat "14 hari" rayuan Sessions Court (era pra-pindaan) | s.46 Akta Mahkamah Kehakiman 1964 (teks belum disemak) | ⚠️ PERLU SAHKAN — TIDAK digunakan sebagai guardrail; dipapar sebagai "lazimnya 14 hari menurut amalan" dengan flag |
| Small Estates (Distribution) Rules (s.30) yang mungkin mengubah tempoh pra-2024 | Belum disemak | ⚠️ PERLU SAHKAN — disekat daripada modul pengeluaran |

#### 8. VERDICT

**YA — kemenangan paling jelas bagi agent dalam senarai ini, dengan satu syarat kejujuran.** Situasi ini murni administratif-deterministik: tempoh dikira daripada tarikh perintah mengikut teks akta; tiada budi bicara, tiada kredibiliti saksi, tiada diskresi. Kegagalan klasik di sini ialah kegagalan maklumat (risalah usang; tiada peringatan; tiada kalkulator) — tepat kelas masalah yang automasi selesaikan sepenuhnya, dan Misi Jurang 1 repo telah menyediakan logiknya (percabangan tarikh). Syarat kejujuran: sehingga dua item PERLU SAHKAN (warta P.U.(B) 267/2024; nilai 14 hari pra-pindaan) disahkan, agent WAJIB memaparkannya sebagai tidak disahkan dan mengarahkan pengesahan peguam/PPKP — prinsip "PERLU SAHKAN tidak boleh digunakan sebagai guardrail" mesti dikekalkan walaupun ia mengurangkan keanggunan pengalaman.

---

## (C) RUMUSAN CIVIL

### C.1 Senarai penambahbaikan yang agent perkenalkan (daripada kaedah klasik — konsolidat 7 kes)

1. **Klasifikasi dwi-jurisdiction automatik pada intake** (agama si mati, jenis harta, wasiat, penamaan, pertikaian aktif) — mencegah forum salah sebelum sebarang pemfailan (Kes 1, 5, 6).
2. **Semakan norma pra-syarat sebelum tindakan (A8)** — sijil faraid, formaliti wasiat, larangan membahagi harta dipertikaikan, pengecualian Akta 300 — bukan selepas litigasi (Kes 1, 2, 6).
3. **Semakan penamaan instrumen WAJIB** (KWSP/insurans/takaful/ASB) — pemisahan "harta pusaka vs harta luar pusaka bernama" sebelum pengiraan; pencegahan saman sia-sia (Kes 3, 4).
4. **Checklist bukti berstruktur (Templat A–F) pada hari pertama** — bukti hibah, bukti status agama, bukti keupayaan pewasiat, dokumen rayuan (semua kes).
5. **Pencegahan ex ante bagi wasiat** — flag penyedia=penerima manfaat; amaran wasiat ubah radikal; larangan ilmu "wasiat mengatasi penamaan" (Kes 2, 4).
6. **Kepastian awal kedudukan hak substantif** — termasuk berita buruk awal (tiada beneficial interest; KWSP bernama bukan pusaka) supaya tiada pembaziran pentadbiran (Kes 3, 4, 6).
7. **Kalkulator tarikh & penjejak tempoh automatik** — percabangan tarikh perintah s.29 (30 hari pasca-15.7.2024; tafsir lama pra-tarikh itu), peringatan berperingkat (Kes 7).
8. **Enjin pengiraan deterministik (A5)** — faraid, Akta 300, wasiat 1/3 — konsisten antara kes, hanya atas aset yang benar-benar pusaka (semua kes).
9. **Status kes tunggal merentasi agensi & dwi-laluan** — menggantikan sijil faraid fizikal dihantar antara agensi, dokumen berulang, dan "menunggu tanpa gambaran" (RP-06) (semua kes).
10. **Audit trail penuh** — setiap cadangan boleh dikesan ke norma/sumber; setiap pelanggaran WAJIB/DILARANG direkod; keputusan muktamad dicatat sebagai keputusan manusia/agensi (semua kes).

### C.2 Senarai KELEMAHAN proses klasik yang BOLEH DIPERDEBATKAN (konsolidat)

1. **Kebergantungan pengetahuan tersirat pegawai/peguam** — twin-track, rejim penama, asimetri pewarisan, laluan remedi: semuanya hanya wujud dalam penghakiman/pekeliling yang tidak sampai kepada waris awam (Kes 1, 4, 6, 7).
2. **Tiada status kes tunggal** — waris menunggu antara Mahkamah Syariah → PPKP → Pejabat Tanah → bank tanpa paparan kedudukan; sijil faraid fizikal dihantar antara agensi (RP-06) (Kes 1, 7).
3. **Dokumen sama dibawa berulang kali** antara agensi; permohonan separuh digital (MyLAND online tetapi Borang A bercetak ditandatangani di hadapan Majistret/Pesuruhjaya Sumpah) (Kes 7).
4. **Waris tidak faham dwi-jurisdiction** — punca saman forum salah (Latifah melalui 3 peringkat mahkamah), saman sia-sia KWSP, dan kejutan asimetri *Lim Ee Seng* (RP-03, KUAT) (Kes 1, 3, 6).
5. **Maklumat rasmi usang tidak ditarik** — risalah JBG "14 hari" terus beredar selepas pindaan 30 hari; tiada mekanisme semakan silang antara penerbitan agensi dengan teks akta (Kes 7).
6. **Forum ditentukan melalui litigasi bertingkat** — dan pihak tanpa forum (bukan Islam dalam isu status agama) terus tanpa remedy (Kes 1, 5).
7. **Geran/pentadbiran dikeluarkan sebelum hak substantif disemak** — SKM kepada keluarga yang tiada hak (*Lim Ee Seng*); pembahagian harta dipertikaikan sebelum penetapan syariah (*Latifah*) (Kes 1, 6).
8. **Kehilangan remedi secara senyap** — tiada peringatan tarikh akhir rayuan; keputusan MT muktamad; tiada statistik rayuan untuk menilai skala masalah (Kes 7).
9. **Ilmu penghakiman tidak mendidik** — kekeliruan sama berulang dekad demi dekad (*How Yew Hock* 1996 → *Krishnaveni* 2013 → *Divyyaa* 2024) kerana ilmu tidak dimoperasikan (Kes 3, 4).
10. **Prosesiding ex parte yang tidak mendengar pihak terkesan** dalam krisis status agama — dan tiada pengurusan harta sementara status dipertikaikan (Kes 5 — kelemahan struktur, bukan proses; reformasi undang-undang, bukan automasi, ialah jawapannya).

### C.3 Jadual guardrails ringkas (konsolidat — hanya item terverifikasi digunakan sebagai guardrail operasi)

| Modul agent | Asas statutori/undang-undang utama | Status |
|---|---|---|
| Klasifikasi laluan (A3) | Senarai Persekutuan 4(e)(i) & Senarai Negeri item 1 (Jadual Kesembilan); Perkara 121(1A); s.3, s.5(1) Akta 98 (bidang kuasa eksklusif MT atas probat); s.3(2) Akta 98 (had RM5 juta); s.17(1) Akta 532 (ARB ≤RM600,000) | ✅ terverifikasi |
| Norma pra-syarat (A8) | s.46(2)(b), s.50 Akta 505 (sijil faraid); s.5 Wills Act 1959 (formaliti); s.2 Akta 300 (pengecualian Islam); s.29 Akta 98 + A1643 s.23 (rayuan 30 hari) | ✅ terverifikasi |
| Nasihat penama (A1/A2) | s.54(1A) Akta KWSP 1991; reg. 7(1), 7(2), 9(2)(a)(i) EPFR 2001; Jadual 10 FSA 2013 (s.130); Fatwa MKI 1973/2000 (*Noridah*) | ✅ terverifikasi |
| Pengiraan (A5) | Skema faraid (12 ashab al-furud, 'aul/radd — sumber syariah dalam repo); Akta 300 s.6(1); had wasiat 1/3 (Enakmen Wasiat Selangor 1999 s.26; *Sabri*) | ✅ terverifikasi |
| Analitis kes (A4) | Preseden bercitation dalam `06-case-studies/` (Latifah, Savatery, How Yew Hock, Divyyaa, Lim Ee Seng, Wee Ku Wing, dll.) | ✅ terverifikasi (preseden; keputusan syariah perlu teks penuh sebelum "autoriti" — Gaps) |
| Dokumen (A7) | Borang Akta 98 (Borang A s.8; DDA; Borang E/F); PAA 1959 s.41, s.60, s.62 (inventori); NLC s.346 (pendaftaran wakil peribadi) | ✅ terverifikasi |
| Orkestrasi (A6) | s.346(5) NLC (tiada urusan sebelum pendaftaran); s.109 Companies Act 2016 (transmission syer ≤60 hari) | ✅ terverifikasi |
| Item DISEKAT (bukan guardrail) | Warta P.U.(B) 267/2024 (belum dibuka terus); "14 hari" Sessions Court (s.46 CJA 1964 belum disemak); teks penuh MR *Kaliammal*; teks penuh *Darius Hoindi*; enakmen wasiat negeri lain (nombor warta); IFSA 2013 seksyen nominasi; s.61(3) ARIE 2003 | ⚠️ PERLU SAHKAN — dipapar dengan flag; TIDAK digunakan sebagai guardrail |

**Prinsip penutup:** dalam kesemua 7 kes, coraknya sama — **agent memindahkan kerja dari mahkamah/pegawai kepada logik; mahkamah/pegawai mengekalkan kuasa muktamad**. Di mana isu bersifat kategori/deterministik (penamaan, tempoh, formaliti), agent jelas mengatasi klasik. Di mana isu bersifat penilaian fakta/diskresi/kredibiliti (suspicious circumstances, penetapan hibah, status agama dalam krisis), agent hanya menyediakan struktur — dan pada Kes 5 (Moorthy), kelemahan sebenar ialah perlembagaan itu sendiri, bukan proses; automasi bukan gantinya.

---

## Jurang maklumat (Gaps)

1. **Tempoh & kos sebenar kes klasik tidak direkodkan dalam repo** — Latifah (tempoh 3 peringkat), Savatery (kos peguam), Lim Ee Seng (tempoh prosiding), Moorthy (kos): semua tidak direkodkan; perbandingan kos klasik-vs-agent dalam fail ini bersifat kualitatif pada titik ini. Cadangan: kajian kos litigasi probat daripada rekod mahkamah/temubual peguam.
2. **Item PERLU SAHKAN yang diwarisi daripada fail sumber** — teks penuh MR *Kaliammal* (20.8.2010); citation *Ahmad bin Abd Majeed*; tahap mahkamah & citation *Mohamed Sulaiman bin Abdul Aziz*; teks penuh *Darius Hoindi* [2025] 11 MLJ 695 (hanya ringkasan Studocu); warta P.U.(B) 267/2024; nilai tepat "14 hari" (s.46 CJA 1964); Small Estates (Distribution) Rules (s.30). Semua ini TIDAK digunakan sebagai guardrail dalam analisis ini.
3. **Tiada kes rayuan s.29 dengan alasan penghakiman penuh** yang boleh diakses percuma — simulasi Kes 7 bergantung pada teks akta & ringkasan sekunder; alasan hakim tentang praktik rayuan tidak dikaji.
4. **Keputusan Mahkamah Syariah jarang diterbitkan terbuka** — analitis preseden A4 bagi isu hibah/sepencarian bergantung petikan jurnal akademik; teks penuh perlu esyariah.gov.my/repositori JKSM sebelum dipetik sebagai "autoriti" (Gaps syariah-cases butir 1).
5. **Statistik proses tidak wujud** — bilangan rayuan s.29 setahun, kadar kejayaan, tempoh median rayuan, kadar kes forum-salah yang dibatalkan: tiada satu pun diterbitkan; tanpa angka ini, dakwaan "agent lebih pantas" kekal kualitatif. Cadangan: rangka metrik baseline sebelum Fasa 3.
6. **Simulasi agent belum diuji secara empirik** — aliran A1–A8 dalam fail ini ialah simulasi atas kertas berasaskan jurnal §6.5; tiada prototype yang telah memproses kes sebenar; verdict YA/SEBAHAGIAN/TIDAK patut dinilai semula selepas ujian modul MVP (D-2).
7. **Had skop geografi** — analisis ini tertumpu Semenanjung; kedudukan Sabah/Sarawak (ANSEO Cap. 1, Cap. 109, Cap. 80, Native Courts) hanya disentuh melalui kes *Darius Hoindi*; cross-examination kes Sabah/Sarawak penuh belum dibuat (rujuk `gap-mission-undang-undang.md` Misi 4).
8. **Harta sepencarian & kes syariah lain** tidak diberikan cross-examination penuh dalam fail ini (fokus civil); cadangan fail susulan `klasik-vs-agent-syariah.md` bagi Templat C dan kes Noridah/Tengah/Wan Shahriman.
