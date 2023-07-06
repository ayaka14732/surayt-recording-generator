from glob import iglob
import os
import requests
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
}

def download_url(url: str) -> None:
    while True:
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f'Error occurred: {e}, retrying...')
            time.sleep(0.5)

d = {}

for filename in iglob('1/*.txt'):
    i = filename.rsplit('/', 1)[-1].removesuffix('.txt')

    with open(filename, encoding='utf-8') as f:
        for j, line in enumerate(f):
            translation, original, filename = line.rstrip('\n').split('\t')
            d[filename] = None

for filename in d:
    filename_ = f'3/{filename}'
    if os.path.exists(filename_):
        continue

    content = download_url(f'https://textbook.surayt.com/files/{filename}')

    with open(filename_, 'wb') as f:
        f.write(content)

    print(f'{filename_} done!')
