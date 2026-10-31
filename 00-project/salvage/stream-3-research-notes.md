---
title: "Salvage — Stream 3 (Institusi + Peta Proses): nota research agent yang gagal HTTP 402"
category: 00-project/salvage
updated: 2026-10-31
status: bahan mentah — URL perlu di-fetch semula & fail sebenar perlu ditulis
---

# Salvage Stream 3 — Nota Research (Recovery 402)

Agent stream 3 gagal dengan HTTP 402 (kredit inference habis) **sebelum** menulis mana-mana fail target: `02-institutions/amanahraya-berhad.md`, `02-institutions/courts-and-offices.md`, `03-processes/process-maps.md`.

Transkrip log mengandungi hasil carian yang telah dilakukannya (~17 minit kerja). Nota ini menyimpan semula: (a) narasi agent, (b) petikan hasil carian, (c) senarai lengkap URL yang disentuh — supaya fail sebenar boleh dibina tanpa ulang carian dari kosong. **Petikan di bawah dipendekkan oleh log — fetch semula URL untuk kandungan penuh sebelum menulis fail akhir.**

## 1. Narasi agent (ikut kronologi)

- Repositori hanya mengandungi README.md — Saya akan buat fail baharu. Domain ARB
- Repositori hanya mengandungi README.md — Saya akan buat fail baharu. Domain ARB kini adalah `amanahraya.my` (akan disahkan berbanding `arb.com.my`). Sekarang, saya sedang mengekstrak laman web rasmi ARB dan mencari butiran yang tidak lengkap (Akta 682, yuran, statistik).
- `web_extract` returned None for one batch. Re-running defensively, one URL at a
- `web_extract` returned None for one batch. Re-running defensively, one URL at a time with retries:
- Laman ARB mengesahkan: 1921 → corporatized 1995, dimiliki sepenuhnya oleh keraja
- Laman ARB mengesahkan: 1921 → corporatized 1995, dimiliki sepenuhnya oleh kerajaan, tertakluk kepada "Public Trust Corporation Act 1995" (perlu untuk mengesahkan nombor akta sebenar — Act 682?). Sekarang: (1) ekstrak penuh bagi halaman terperinci anak syarikat/pentadbiran, (2) pengesahan akta, (3) sumber yuran, (4) memulakan kajian institusi.
- `Public Trust Corporation Act 1995` adalah **Akta 532** — jadi premis "Akta 682
- `Public Trust Corporation Act 1995` adalah **Akta 532** — jadi premis "Akta 682 2001" memerlukan pemeriksaan. Skala yuran rasmi ARB (5%/4%/3%/2%/1%, deposit RM50, tempoh 4–6 bulan) diperoleh. Kini mengesahkan identiti sebenar bagi Akta 682, mengekstrak teks PTCA, dan memulakan kelompok institusi.
- Act 682 = **University of Malaya Act 1961** — the premise is wrong; ARB's statut
- Act 682 = **University of Malaya Act 1961** — the premise is wrong; ARB's statute is PTCA 1995 [Act 532], in force 1 Aug 1995. Now extracting the institution batch (JKPTG, JKSM, MdI, ANM, SSM, banks, High Court process sources):
- Data utama telah diperoleh. JKPTG FAQ menyatakan RM5 juta sebagai had semasa (me
- Data utama telah diperoleh. JKPTG FAQ menyatakan RM5 juta sebagai had semasa (menarik — Conventuslaw masih menyatakan RM2m; perlu diselesaikan melalui teks Akta 98/pindaan 2021). JKSM memberikan butiran sijil faraid + fi. Kini: cetakan kedalaman penuh untuk halaman yang disimpan dan gelombang ekstrak seterusnya:
- Pemetaan trofi yang baik (sila rujuk pindaan RM2j→RM5j, Act 370/360/532 pengesah
- Pemetaan trofi yang baik (sila rujuk pindaan RM2j→RM5j, Act 370/360/532 pengesahan, s.122 Akta Insolvensi, butiran proses faraid). Gelombang ekstraksi akhir — sumber peta proses (ascolaw, KWSP, eGUMIS, Bursa, JKPTG piagam, MyGOV PPKP steps):
- Hampir lengkap. Pusingan terakhir: cetakan bahagian STORE kekal (PTCA s.17/s.33,
- Hampir lengkap. Pusingan terakhir: cetakan bahagian STORE kekal (PTCA s.17/s.33, perbandingan kos ARB vs peguam ascolaw, dokumen waris eGUMIS, senarai dokumen Bursa) + beberapa ekstrak bertanda (Family Care Trust, Pending Fund Management, SSM trust company PDF, iProperty/Bar wasiat artikel, Etiqa) + verifikasi akta:
- Bahan hampir lengkap. Gelombang pengesahan terakhir (kos ascolaw, statistik ARB
- Bahan hampir lengkap. Gelombang pengesahan terakhir (kos ascolaw, statistik ARB dari media, FSA 2013 penamaan insurans, nombor akta) kemudian saya menulis fail:
- Satu siri verifikasi terakhir (nombor akta Trust Companies Act, artikel The Star
- Satu siri verifikasi terakhir (nombor akta Trust Companies Act, artikel The Star mengenai pembangunan semula undang-undang amanah), kemudian saya akan menulis ketiga-tiga fail tersebut:

## 2. Alatan & intensiti carian

Jumlah tool calls: 12 (execute_code(B, execute_code(def, execute_code(from, execute_code(import, search_files(*.md))

## 3. Petikan hasil carian (truncated oleh log)

### Petikan [1]

```
search_files ok 0.2s: {"total_count": 2, "files": ["/opt/data/profiles/estateadministration-project/estate-admin-malaysia/README.md", "/opt/data/profiles/estateadministration-project/estate-admin-malaysia/.git"]}
```

### Petikan [2]

```
execute_code ok 15.9s: {"status": "success", "output": "## arb1\n 0: https://www.amanahraya.my/about/about-us/\n About Us\n 1: https://en.wikipedia.org/wiki/Amanah_Raya_Berhad\n Amanah Raya Berhad - Wikipedia\n 2: https://theedgemalaysia.com/content/advertise/amanahraya-syariah-income-fund-crossed-rm200-million-mark\n AmanahRaya Syariah Income Fund Crossed RM200 Million Mark\n 3: https://contactout.com/company/Amanah-Ra …(+14770 chars)
```

### Petikan [3]

```
execute_code ERROR 81.2s: {"status": "error", "output": "\n--- stderr ---\nTraceback (most recent call last):\n File \"/opt/data/cache/scratch/hermes_kernel_33z_326t/hermes_kernel_runner.py\", line 118, in run_cell\n exec(compile(request[\"code\"], \"<cell>\", \"exec\"), GLOBALS)\n ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n File \"<cell>\", line 54, in <module>\n File \"<cell>\", line 28, in dig\nTypeError …(+713 chars)
```

### Petikan [4]

```
execute_code ok 7.4s: {"status": "success", "output": "=== https://www.amanahraya.my/about/about-us/\n[Skip to content](https://www.amanahraya.my/about/about-us/#main)\nAmanah Raya Berhad is Malaysia’s premier trustee company wholly owned by the Government of Malaysia.\n![](https://www.amanahraya.my/wp-content/uploads/2023/08/amout-1024x1024.jpg)\nEstablished in 1921 as the Department of Public Trustee and Official Adm …(+24961 chars)
```

### Petikan [5]

```
execute_code ok 51.0s: {"status": "success", "output": "=== TAIL https://www.amanahraya.my/ms/anak-syarikat/\ns:**\n\n7th & 8th Floor, Wisma AmanahRaya\n\n2 Jalan Ampang,\n\n50508 Kuala Lumpur\n\n**Contact Numbers:**\n\nTel: 603-2687 5200\n\nFax: 603-2687 5300\n\nReal Estate Management\n\n![](https://www.amanahraya.my/wp-content/uploads/2023/08/blogo-arkenedix.png)\n\n## AmanahRaya-Kenedix REIT Manager Sdn. Bhd.\n\n[Vis …(+13709 chars)
```

### Petikan [6]

```
execute_code ok 29.7s: {"status": "success", "output": "=== HOME services section:\n (not found) \n\n=== SUBSIDIARIES tail:\n ttps://www.amanahraya.my/subsidiaries/#back-to-top)\n\n## [Back To Top](https://www.amanahraya.my/subsidiaries/\\#back-to-top)\n\n[Scroll to the top of the page](https://www.amanahraya.my/subsidiaries/#)\n\nOMNI \n\n=== https://simrahman.com/wp-content/uploads/2025/07/Public-Trust-Corporation-Act …(+13055 chars)
```

### Petikan [7]

```
execute_code ok 91.3s: {"status": "success", "output": "=== https://www.jkptg.gov.my/my/soalan-lazim-3/47-faq/pusaka-kecil/1084-pusaka-kecil\n[![soalan lazim2](https://www.jkptg.gov.my/images/photos/icon_mampu/FAQ-BM.png)](https://www.jkptg.gov.my/my/soalan-lazim-3) \\| [![hubungi kami2](https://www.jkptg.gov.my/images/photos/icon_mampu/CONTACT-BM.png)](https://www.jkptg.gov.my/my/hubungi-kami/ibu-pejabat) \\| [![aduan2 …(+38493 chars)
```

### Petikan [8]

```
execute_code ok 40.3s: {"status": "success", "output": "=== SECTION https://www.jkptg.gov.my/my/soalan-lazim-3/47-faq/pusaka-kecil/1084-pusaka-kecil\nApakah yang dimaksudkan dengan Harta Pusaka Kecil?\n\n\nHarta Pusaka Kecil merupakan harta peninggalan si mati yang mempunyai ciri-ciri berikut:\n\n a) Harta si mati terdiri daripada:\n\n i- Harta Alih sahaja atau;\n\n ii- Harta Tak Alih Sahaja atau;\n\n iii- Harta Alih be …(+37767 chars)
```

### Petikan [9]

```
execute_code ok 55.6s: {"status": "success", "output": "=== SEC https://www.anm.gov.my/awam/wang-tak-dituntut\n3. Wang dalam kredit sesuatu akaun dagangan yang telah tidak dikendalikan melalui apa-apa urusniaga dalam satu tempoh masa tidak kurang dari dua (2) tahun.\n\n\n\n **Contoh dibawah kategori ini ialah :**\n - akaun pemiutang dagangan;\n - akaun penghutang dagangan berbaki kredit.\n\n- [Siapa Wajib Mematuhi Akta  …(+41083 chars)
```

### Petikan [10]

```
execute_code ok 49.1s: {"status": "success", "output": "=== SEC https://simrahman.com/wp-content/uploads/2025/07/Public-Trust-\ngrantee to extract letters \nof administration\n\n16. Corporation may take possession of property\n\n17. Summary administration of movable property\n\n18. Administration of estates of small value\n\n19. Payment of minor’s maintenance\n\n20. Undistributed funds\n\n21. Corporation may represent m …(+28513 chars)
```

### Petikan [11]

```
execute_code ok 25.8s: {"status": "success", "output": "=== SEC https://ascolaw.co/blog/cara-mohon-geran-probet-malaysia\n pertikaian atau isu wasi.\n\n\nJika anda sudah mempunyai set ini dan mahu mengetahui skop kerja serta kos yang sesuai, lihat [Peguam Probet Malaysia: Skop, Dokumen, Kos dan Cara Dapatkan Quotation](https://ascolaw.co/blog/peguam-probet-malaysia).\n\n## Soalan Lazim\n\n### Berapa lama proses permohon …(+13086 chars)
```

### Petikan [12]

```
execute_code ok 9.5s: {"status": "success", "output": "## tcanum\n https://www.ssm.com.my/Pages/Legal_Framework/Trust-Companies-Act.aspx\n Trust Companies Act | # ​​ ​​​​​​​Trust Companies Act​\n**Legislation**\n|​​Bil​|Legislation|​Format|\n|--|--|--|\n|1.​|Trust Companies \n https://lawplayer.com/my/act/act-100\n Trust Companies Act 1949 — Malaysia Act | LawPlayer MY | Trust Companies Act 1949 [Act 100] — Laws of Mal …(+4525 chars)
```

## 4. Senarai URL dalam transkrip (32 unik)

- https://www.amanahraya.my/about/about-us/\n
- https://en.wikipedia.org/wiki/Amanah_Raya_Berhad\n
- https://theedgemalaysia.com/content/advertise/amanahraya-syariah-income-fund-crossed-rm200-million-mark\n
- https://contactout.com/company/Amanah-Ra
- https://www.amanahraya.my/about/about-us/\n[Skip
- https://www.amanahraya.my/about/about-us/#main
- https://www.amanahraya.my/wp-content/uploads/2023/08/amout-1024x1024.jpg
- https://www.am
- https://www.amanahraya.my/ms/anak-syarikat/\ns:**\n\n7th
- https://www.amanahraya.my/wp-content/uploads/2023/08/blogo-arkenedix.png
- https://www.amanahraya.my/ms/
- https://www.amanahraya.my/subsidiaries/\\#back-to-top
- https://www.amanahraya.my/subsidiaries/#
- https://simrahman.com/wp-content/uploads/2025/07/Public-Trust-Corporation-Act
- https://www.jkptg.gov.my/my/soalan-lazim-3/47-faq/pusaka-kecil/1084-pusaka-kecil
- https://www.jkptg.gov.my/en/pembahagian-pusaka-kecil
- https://www.jkptg.gov.my/en/panduan/senarai-undang-undan
- https://www.jkptg.gov.my/my/soalan-lazim-3/47-faq/pusaka-kecil/1084-pusaka-kecil\n[![soalan
- https://www.jkptg.gov.my/images/photos/icon_mampu/FAQ-BM.png
- https://www.jkptg.gov.my/my/soalan-lazim-3
- https://www.jkptg.gov.my/images/photos/icon_mampu/CONTACT-BM.png
- https://www.jkptg.gov.my/my/hubungi-kami/ibu-pejabat
- https://www.jkptg.gov.my/my/soalan-lazim-3/47-faq/pusaka-kecil/1084-pusaka-kecil\nApakah
- https://www.anm.gov.my/awam
- https://www.anm.gov.my/awam/wang-tak-dituntut\n3
- https://simrahman.com/wp-
- https://simrahman.com/wp-content/uploads/2025/07/Public-Trust-\ngrantee
- https://ascolaw.co/blog/c
- https://ascolaw.co/blog/cara-mohon-geran-probet-malaysia\n
- https://ascolaw.co/blog/peguam-probet-malaysia
- https://www.ssm.com.my/Pages/Legal_Framework/Trust-Companies-Act.aspx\n
- https://lawplayer.com/my/act/act-100\n

---
*Diselamatkan secara automatik oleh Zizi pada 2026-10-31 selepas kegagalan kredit stream 3.*
