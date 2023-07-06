import os
from glob import iglob
from google.cloud import texttospeech

sentence_filenames = []

for filename in iglob('1/*.txt'):
    i = filename.rsplit('/', 1)[-1].removesuffix('.txt')

    with open(filename, encoding='utf-8') as f:
        for j, line in enumerate(f):
            translation, original, filename = line.rstrip('\n').split('\t')
            sentence_filenames.append((translation, filename))

client = texttospeech.TextToSpeechClient()

for sentence, filename in sentence_filenames:
    filename = f'2/{filename}'
    if os.path.exists(filename):
        continue

    synthesis_input = texttospeech.SynthesisInput(text=sentence)
    voice = texttospeech.VoiceSelectionParams(language_code='en-GB', ssml_gender=texttospeech.SsmlVoiceGender.FEMALE)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
    response = client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)

    with open(filename, 'wb') as f:
        f.write(response.audio_content)
        print(f'{filename} done!')
