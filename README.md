# Speech Generator 🗣️🔊

Welcome to **Speech Generator**, a simple yet powerful Streamlit application that converts lines of text from a `.txt` file into `.wav` audio files using text-to-speech (TTS) technology. 🎉

---

## Features ✨

- **Upload a `.txt` file** 📄: Easily upload a text file containing multiple lines of text.
- **Generate `.wav` files** 🎵: Each line of text is automatically converted into a separate `.wav` audio file.
- **Play audio files** ▶️: Listen to the generated audio files directly in the app.
- **Download as ZIP** 📦: Download all the audio files as a single ZIP archive for convenience.

---

## How to Use 🚀

1. **Run the App**:
   Install the required dependencies and start the Streamlit app:
   ```bash
   streamlit run text_to_wav.py
   ```

2. **Upload Your File**:
   - Click on the file uploader and select a `.txt` file.
   - Ensure each line in the file contains the text you want to convert to audio.

3. **Generate and Listen**:
   - The app will generate `.wav` files for each line in your file.
   - You can listen to the audio files directly in the app.

4. **Download Audio Files**:
   - Click the "Download all audio files as ZIP" button to save all files to your computer.

---

## Requirements 🛠️

- **Python 3.7+** 🐍
- **Dependencies**:
  - Streamlit
  - gTTS

Install the required Python libraries with:
```bash
pip install streamlit gtts
```

---

## Folder Structure 📂

```
Speech Generator/
├── speech.py              # Main application script
├── generated_audio/       # Folder where .wav files are saved
└── audio_files.zip        # ZIP archive of audio files (optional)
```

---

## Screenshots 📸


### Generated Audio Files

<img width="1432" alt="Screenshot 2025-01-05 at 11 07 07" src="https://github.com/user-attachments/assets/ee778976-769a-43ae-9462-aadd01ae80b5" />


---

## Contributing 🤝

Contributions are welcome! If you have ideas for improving the app or fixing bugs, feel free to open an issue or submit a pull request. 🛠️

---

## License 📜

This project is licensed under the MIT License. Feel free to use and modify it as you wish.

---

## Acknowledgments 🙌

- **[Streamlit](https://streamlit.io/)** for creating a great framework for building data apps.
- **[gTTS](https://pypi.org/project/gTTS/)** for providing easy text-to-speech conversion.

---

Enjoy using Speech Generator! 🗣️✨
