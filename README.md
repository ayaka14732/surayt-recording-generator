# Surayt Recording Generator

## The Results

The results are saved in `6/`.

## Run

Save your Google application credentials to `xxx-xxxx-xxxxxx.json`, then run:

```sh
python -m venv venv
. venv/bin/activate
pip install -U pip
pip install -U wheel
pip install -r requirements.txt
mkdir -p 1 2 3 4 5 6
python 1_get_courses.py
GOOGLE_APPLICATION_CREDENTIALS='xxx-xxxx-xxxxxx.json' python 2_synthesis.py
python 3_download_files.py
for file in 3/*.mp3; do base=$(basename "$file"); if [ ! -f "4/$base" ]; then ffmpeg -nostats -loglevel error -i "$file" -filter:a "volume=1.75" "4/$base"; fi; done
python 4_merge.py
ffmpeg -f lavfi -i anullsrc=channel_layout=stereo:sample_rate=16000 -t 0.25 silence.mp3
for filepath in 5/*.txt; do filename=$(basename "$filepath"); if [ ! -f 6/"Šlomo Surayt ${filename%.*}".mp3 ]; then ffmpeg -nostats -loglevel error -f concat -safe 0 -i $filepath -vn -ar 16000 -ac 2 -b:a 128k 6/"Šlomo Surayt ${filename%.*}".mp3; fi; done
```
