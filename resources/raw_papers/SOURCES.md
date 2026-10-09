# 11408 raw paper sources

## Current status after local supplementation (2026-10-09)

The sections below this update are historical collection notes, not an accurate description of the current file layout. See [the current resource index](../README.md) and [the per-file provenance manifest](../local_sources_manifest.json).

- Local supplementary source: `E:\kaoyan`; selected PDF copies originate from https://github.com/youngflysky/KaoYanZhenTi-PDF. Files are copied byte-for-byte.
- English 2014-2020 and 2022 previously contained HTTP 404 HTML under PDF filenames; all eight were replaced. The former `2024_english1.pdf` actually contains **2022 answers/explanations** and is now `../solutions/english1/2022_english1.pdf`. No verified 2024 English PDF is currently available locally; use the archived transcription with caution.
- Math 2014-2022 former solution editions are now in `../solutions/math1/`, with question-only local editions at the original paper paths. Math 2023-2025 still include answers/explanations alongside questions.
- English 2021's explanatory edition is preserved in `../solutions/english1/`; its paper path now contains a question-only edition.
- Added older 408 papers (2009-2013), English papers (2002-2013), Math papers (2010-2013), Math solutions (2010-2013), and one 1987-2009 Math collection. Pre-2010 English is the pre-split national English examination.
- Added local HTML transcriptions from 计算机考研杂货铺 (`https://www.csgraduates.com`) under `../archived_pages/`: politics 2010-2026, English 2010-2026, Math 2008-2026, 408 2009-2026. These are searchable secondary sources, not official scans. Their external resources are not all bundled.
- Politics now has local HTML questions/explanations, but still has no PDF paper. The historical PDF links below remain candidates; this import made no network requests.
- Validation: PDF signature and page-tree checks; sampled first/last-page rendering for replacement editions and suspected mislabels; SHA-256 equality for copied files. Not a complete per-question or per-page correctness audit.

## Historical collection notes (before supplementation)

This directory stores publicly accessible exam paper PDFs collected for 11408 preparation.

## Current files

- `english1/2014_english1.pdf` through `english1/2024_english1.pdf`
  - Source repository: https://github.com/TsekaLuk/Kaoyan-English1-Papers
  - Source path: `papers/english1_YYYY.pdf`
- `math1/2014_math1.pdf` through `math1/2024_math1.pdf`
  - Source repository: https://github.com/TsekaLuk/Kaoyan-Math1-Papers
  - Source path: `solutions/YYYY年解析/*_origin.pdf`
- `408/2014_408.pdf` through `408/2024_408.pdf`
  - Source repository: https://github.com/kxmzyc/cs408-exam-analysis
  - Source path: top-level `YYYY年计算机408...pdf` files

## 2025 additions

- `english1/2025_english1.pdf`
  - Source repository: https://github.com/Gatsby666-jay/Kaoyan-English-2a
  - Source path: `2025考研英语真题和答案/2025考研英语一真题及答案/2025考研英语一真题.pdf`
  - Verified as a complete 21-page question paper. It is a third-party typeset copy with a Wanxue Haiwen watermark, not an official scan.
- `math1/2025_math1.pdf`
  - Source repository: https://github.com/fjw345/mathonline
  - Source path: `resource/考研数学/考研数学 (一) 真题及答案解析（1987-2026）/2025考研数学（一）真题试卷及解析详细版.pdf`
  - Verified as a complete 16-page question-and-solution edition. Answers and explanations are interleaved with the questions, so this is not a clean question-only paper.
- `408/2025_408.pdf`
  - Source repository: https://github.com/SyHang-hash/408-----
  - Source path: `历年真题pdf/2025年408计算机考研真题.pdf`
  - Verified as a complete 12-page paper; the printed footer identifies 11 numbered test pages after the cover.

## Politics source candidates

The Zhengzhou Technology and Business University Marxism School page lists 2014-2024 politics PDFs directly:

- Page: https://szb.ztbu.edu.cn/2025_05/08_17/content-63733.html
- 2014: https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/80fce00922d3521e.pdf
- 2015: https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/fd8d31fce1370441.pdf
- 2016: https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/52bc1b34ce1420ac.pdf
- 2017: https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/ef7e656229b14ffe.pdf
- 2018: https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/aa722ead55dc4dbc.pdf
- 2019: https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/fe440afcb892077f.pdf
- 2020: https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/fb8a3633a8df34d0.pdf
- 2021: https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/12a2177b1eec778a.pdf
- 2022: https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/dba47a0f0e542aa0.pdf
- 2023: https://szb.ztbu.edu.cn/attachment/sites/item/2025_06/03_17/148ebcad6cdfd251.pdf
- 2024: link is shown on the source page as `2024考研政治真题(完整).pdf`.

At collection time, the local shell environment timed out during TLS handshakes to `szb.ztbu.edu.cn`, so the politics PDFs are recorded as source links but not yet stored locally.

### 2025 politics sources

The following public sources were checked and contain the complete 2025 politics questions:

- Original-layout 12-page paper preview: https://www.scribd.com/document/976680139/2025考研政治真题
- Xi'an International University, 16-page complete paper: https://edu.xaiu.edu.cn/__local/F/70/01/50746677F11FF187B5D43B0E760_18751FEC_70206.pdf
- Juying complete paper: https://m.juyingonline.com/upload/202412/23/202412231025028712.pdf
- GitHub Markdown transcription (not a PDF): https://github.com/xyzxyq/kaoyanzhengzhi

The PDF hosts above time out from the current local network route. No 2025 politics PDF has been placed in `politics/`; this is intentionally left incomplete rather than substituting a recalled or partial paper.
