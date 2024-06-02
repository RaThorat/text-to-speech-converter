# Text-to-Speech Converter

This project provides a simple Python script to convert text to speech using the Google Text-to-Speech (`gTTS`) library and play the resulting audio file. The text to be converted is stored in a separate text file, making it easy to change the content without modifying the script.

## Features

- Converts text from a file to speech.
- Supports Dutch (`nl`) language.
- Uses `gTTS` for text-to-speech conversion.
- Plays the audio file using `playsound`.
- Optionally deletes the audio file after playing.

## Prerequisites

- Python 3.x
- `gTTS` library
- `playsound` library

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/text-to-speech-converter.git
    cd text-to-speech-converter
    ```

2. **Install the required libraries**:
    ```sh
    pip install gtts playsound
    ```

## Usage

1. **Prepare the text file**:
    - Create a text file named `document_text.txt` in the project directory.
    - Add the text you want to convert to speech in this file.

    Example `document_text.txt`:
    ```
    Hoe rechercheurs vastlopen in stuwmeer van fraudezaken
    Bart Mos, Nika Buijs, Johan Leupen
    14-18 minuten
    In het kort

    Ondanks een verhoging van budgetten met bijna een derde sinds 2013, slaagt justitie er minder goed in witteboordencriminelen veroordeeld te krijgen, blijkt uit FD-onderzoek.
    Het aantal verdachten dat wegkwam zonder straf of boete omdat het fraudeparket van strafvervolging afzag, steeg in dezelfde periode van 1000 naar bijna 2000 gevallen per jaar.
    Betrokkenen klagen over het grote aantal oude zaken, personeelstekorten en moeizame samenwerking tussen rechercheurs en officieren van justitie.

    Het is 2020 als Flip Schreurs als curator aanloopt tegen de bestuurder van een failliet beleggingsbedrijf. De man in kwestie blijkt enkele honderden Nederlanders en Belgen te hebben opgelicht. In plaats van het spaargeld van zijn klanten in cryptovaluta’s te hebben gestoken, heeft de bestuurder er auto’s, dure horloges en reizen voor zichzelf van gekocht. In januari 2021 doet Schreurs daarom aangifte van fraude tegen de man.

    (de rest van de artikel)
    ```

2. **Run the script**:
    ```sh
    python read_aloud.py
    ```

3. **Listen to the audio**:
    - The script will convert the text in `document_text.txt` to speech and play the audio.

4. **Optional**:
    - The script will delete the audio file after playing. You can modify the script if you want to keep the audio file.

