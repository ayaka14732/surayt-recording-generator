from bs4 import BeautifulSoup
import os
import requests

urls = [
    *(f'https://textbook.surayt.com/en/Level%20A/{i}.1' for i in range(3, 16+1)),
    *(f'https://textbook.surayt.com/en/Online%20Course/2.{i}.1' for i in range(1, 8+1)),
]

for i, url in enumerate(urls, 3):
    filename = f'1/{i}.txt'
    if os.path.exists(filename):
        continue

    with open(filename, 'w', encoding='utf-8') as f:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.select('article section table:not(.no_header_row) tr:not(:first-child), article section table.no_header_row tr')

        for row in rows:
            cols = row.find_all('td')
            if len(cols) != 2:
                continue
            l, r = cols

            original = l.find('a').text.strip()
            translation = r.text.strip()
            filename = l.find('a').get('href').rsplit('/', 1)[1]

            assert '\t' not in translation
            assert '\t' not in original
            assert '\t' not in filename

            print(translation, original, filename, sep='\t', file=f)

    print(f'Course {i} done')
