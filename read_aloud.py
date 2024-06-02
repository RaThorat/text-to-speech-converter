from gtts import gTTS
from playsound import playsound
import os

# Path to the text file
text_file_path = 'Strijd_tegen _witteboorden­criminaliteit_hapert.txt'

# Read the text from the file
with open(text_file_path, 'r', encoding='utf-8') as file:
    document_text = file.read()

# Convert text to speech with adjustments for Dutch language and slower speed
tts = gTTS(text=document_text, lang='nl', slow=False)
audio_file = 'document_audio.mp3'
tts.save(audio_file)

# Play the audio file
playsound(audio_file)

# Optionally, remove the audio file after playing
os.remove(audio_file)

