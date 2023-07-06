import os
from glob import iglob

silence = os.path.abspath('silence.mp3')

for filename in iglob('1/*.txt'):
    i = filename.rsplit('/', 1)[-1].removesuffix('.txt')

    mp3_files = []

    with open(filename, encoding='utf-8') as f:
        for j, line in enumerate(f):
            translation, original, filename = line.rstrip('\n').split('\t')
            mp3_files.append(f'2/{filename}')
            mp3_files.append(f'4/{filename}')

    with open(f'5/{i}.txt', 'w') as f:
        for mp3_file in mp3_files:
            f.write(f"file '{os.path.abspath(mp3_file)}'\n")
            f.write(f"file '{silence}'\n")
