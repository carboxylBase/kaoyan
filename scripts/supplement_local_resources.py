"""Import selected local exam sources, preserving existing solution editions.

Run with Python 3, pypdf and beautifulsoup4:
  python scripts/supplement_local_resources.py --source E:/kaoyan --apply
Without --apply, print the proposed destinations only. Never downloads files.
"""
import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

from bs4 import BeautifulSoup
from pypdf import PdfReader

REPO = Path(__file__).resolve().parents[1]
RES = REPO / 'resources'
MANIFEST = RES / 'local_sources_manifest.json'
UPSTREAM = 'https://github.com/youngflysky/KaoYanZhenTi-PDF'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, default=Path('E:/kaoyan'))
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--image-source', type=Path, help='Optional existing local images directory (no downloads)')
    args = parser.parse_args()
    base = args.source.resolve()
    records = json.loads(MANIFEST.read_text(encoding='utf-8')) if MANIFEST.exists() else []
    entries = {r['destination']: r for r in records}
    count = 0
    planned_removed = set()

    def add(source, relative, kind, reason, upstream=UPSTREAM, relocate=False):
        nonlocal count
        dest = (REPO / relative).resolve()
        assert dest.is_relative_to(RES.resolve()), dest
        key = dest.relative_to(REPO).as_posix()
        # Relocations are already complete on a subsequent run.
        if relocate and key in entries and dest.exists():
            assert digest(dest) == entries[key]['sha256'], f'Changed destination: {dest}'
            return
        source = source.resolve()
        if relocate:
            assert source.is_relative_to(RES.resolve()), source
        assert source.is_file(), source
        sha = digest(source)
        if dest.exists() and dest not in planned_removed and digest(dest) != sha:
            # Only the eight tracked HTTP 404 downloads may be overwritten.
            header = dest.read_bytes()[:500]
            assert dest.suffix == '.pdf' and b'HTTP Status 404' in header and not header.startswith(b'%PDF-'), f'Refusing to overwrite {dest}'
        info = {'destination': key, 'source_local': str(source), 'upstream': upstream,
                'kind': kind, 'selection_reason': reason, 'sha256': sha,
                'bytes': source.stat().st_size, 'import_date': '2026-10-09'}
        if source.suffix.lower() == '.pdf':
            assert source.read_bytes()[:5] == b'%PDF-', source
            reader = PdfReader(source)
            info['pages'] = len(reader.pages)
            assert info['pages'] > 0
            info['validation'] = 'PDF header and page tree readable; selected editions visually sampled; not every question proofread'
        elif source.suffix.lower() == '.html':
            soup = BeautifulSoup(source.read_text(encoding='utf-8'), 'html.parser')
            box = soup.select_one('.td-content')
            assert box and len(box.select('h5')) > 0, source
            info['title'] = soup.title.get_text() if soup.title else ''
            info['question_heading_count'] = len(box.select('h5'))
            info['question_image_sources'] = sorted({i.get('src', '') for i in box.select('img[src]')})
            info['validation'] = 'Article and question headings present; transcription, not official scan; external assets may be missing'
        if not args.apply:
            print(('MOVE ' if relocate else 'COPY ') + key)
            if relocate:
                planned_removed.add(source)
            return
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists() or digest(dest) != sha:
            shutil.copy2(source, dest)
        assert digest(dest) == sha
        if relocate and source != dest:
            source.unlink()
        # Preserve original provenance for repeated invocations.
        entries.setdefault(key, info)
        if entries[key]['sha256'] != sha:
            raise RuntimeError(f'Manifest mismatch: {key}')
        MANIFEST.write_text(json.dumps(sorted(entries.values(),key=lambda x:x['destination']),ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
        count += 1

    # Existing editions that were mislabeled as question papers.
    for year in range(2014, 2023):
        add(RES/f'raw_papers/math1/{year}_math1.pdf', f'resources/solutions/math1/{year}_math1.pdf',
            'solutions', 'Preserve existing solution edition; canonical paper replaced with local question-only edition',
            'https://github.com/TsekaLuk/Kaoyan-Math1-Papers', relocate=True)
    add(RES/'raw_papers/english1/2024_english1.pdf', 'resources/solutions/english1/2022_english1.pdf',
        'solutions', 'Printed title is 2022 answers and explanations; original filename incorrectly said 2024',
        'https://github.com/TsekaLuk/Kaoyan-English1-Papers', relocate=True)
    add(RES/'raw_papers/english1/2021_english1.pdf', 'resources/solutions/english1/2021_english1.pdf',
        'questions-and-solutions', 'Preserve 22-page explanatory edition while adding a question-only paper',
        'https://github.com/TsekaLuk/Kaoyan-English1-Papers', relocate=True)

    english = base/'02_英语一/来源_GitHub_KaoYanZhenTi-PDF'
    for year in range(2002, 2023):
        add(english/f'{year}.pdf', f'resources/raw_papers/english1/{year}_english1.pdf',
            'questions-and-solutions' if year == 2022 else 'question-paper',
            'Fill missing year or replace HTTP 404/solution-only edition; 2002-2009 are pre-split English papers')
    math = base/'03_数学一/来源_GitHub_KaoYanZhenTi-PDF'
    for year in range(2010, 2023):
        add(math/f'01.1987-2020数一真题标准版（直接打印）/{year}.pdf', f'resources/raw_papers/math1/{year}_math1.pdf',
            'question-paper', 'Question-only printable edition; complements separate solutions')
    for year in range(2010, 2014):
        add(math/f'03.2005-2020年数一真题详解（步骤解析）/{year}解析.pdf',f'resources/solutions/math1/{year}_math1.pdf',
            'solutions', 'Add corresponding solutions for newly added papers')
    add(math/'01.1987-2020数一真题标准版（直接打印）/0.1987-2009考研数学一真题【 72页 】（直接打印）.pdf',
        'resources/raw_papers/math1/1987-2009_math1_collection.pdf', 'question-collection',
        'One historical question collection; omit overlapping 1987-2022 and 2010-2022 collections')
    for year in range(2009, 2014):
        add(base/f'04_408/来源_GitHub_KaoYanZhenTi-PDF/{year}年408真题.pdf',f'resources/raw_papers/408/{year}_408.pdf',
            'questions-and-solutions','Fill missing older years; retain existing 2014-2025 editions')

    for folder, subject, urlpart in [('01_政治','politics','politics'),('02_英语一','english1','english/english-one'),
                                    ('03_数学一','math1','math/math-one'),('04_408','408','cs')]:
        for source in sorted((base/folder/'网页离线版').glob('*.html')):
            if re.fullmatch(r'20\d{2}', source.stem):
                add(source,f'resources/archived_pages/{subject}/{source.stem}.html',
                    'transcription-with-explanations','Searchable supplementary text; PDFs take precedence for wording and diagrams',
                    'https://www.csgraduates.com (local archive; exact page URL not independently reverified)')
    if args.image_source:
        for source in sorted(args.image_source.rglob('*')):
            if source.is_file() and source.suffix.lower() in {'.png', '.jpg', '.jpeg', '.svg'}:
                add(source, 'resources/archived_pages/assets/images/' + source.relative_to(args.image_source).as_posix(),
                    'transcription-image', 'Existing locally cached image; raw HTML source paths are recorded in the manifest',
                    'https://www.csgraduates.com/images/')
    if args.apply:
        MANIFEST.write_text(json.dumps(sorted(entries.values(),key=lambda x:x['destination']),ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
        print(f'Processed {count} files; manifest contains {len(entries)} entries.')


if __name__ == '__main__':
    main()
