import os
from gtts import gTTS
import streamlit as st

def save_text_to_speech(text, output_path, line_num):
    """
    Convert text to speech and save as .wav file.

    Args:
        text (str): Text to convert to speech.
        output_path (str): Directory to save the .wav file.
        line_num (int): Line number for naming the file.
    """
    tts = gTTS(text, lang='en')
    output_file = os.path.join(output_path, f"line_{line_num}.wav")
    tts.save(output_file)

def process_uploaded_file(uploaded_file):
    """
    Process the uploaded .txt file and create .wav files for each line.

    Args:
        uploaded_file (UploadedFile): The uploaded text file.

    Returns:
        output_dir (str): Directory containing the generated .wav files.
    """
    # Read the file content
    lines = uploaded_file.read().decode('utf-8').splitlines()

    # Create output directory
    output_dir = "generated_audio"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each line and save as .wav file
    for idx, line in enumerate(lines, start=1):
        if line.strip():  # Skip empty lines
            save_text_to_speech(line.strip(), output_dir, idx)

    return output_dir

# Streamlit app
st.title("Text-to-Speech File Generator")
st.write("Upload a .txt file, and this app will generate .wav files for each line of text.")

uploaded_file = st.file_uploader("Choose a .txt file", type=["txt"])

if uploaded_file is not None:
    # Process the uploaded file
    st.write("Processing the uploaded file...")
    output_directory = process_uploaded_file(uploaded_file)

    # Display results
    st.success("Audio files generated successfully!")
    st.write(f"All .wav files are saved in the '{output_directory}' folder.")

    # List generated files
    audio_files = os.listdir(output_directory)
    for audio_file in audio_files:
        audio_path = os.path.join(output_directory, audio_file)
        st.audio(audio_path, format="audio/wav")

    # Option to download files as a zip
    import shutil
    zip_file = "audio_files.zip"
    shutil.make_archive("audio_files", 'zip', output_directory)
    with open(zip_file, "rb") as fp:
        st.download_button(
            label="Download all audio files as ZIP",
            data=fp,
            file_name="audio_files.zip",
            mime="application/zip"
        )
