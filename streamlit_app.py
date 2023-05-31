import streamlit as st

import whisper

# Load the Whisper model

model = whisper.load_model("base")

# Streamlit app title and header

st.title("Whisper Transcription App")

st.header("Transcribe Audio to Text")

# File uploader for audio input

audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "ogg"])

# Button to transcribe audio

if st.button("Transcribe"):

    if audio_file is not None:

        # Load the audio file

        audio_data = audio_file.read()

        

        # Perform transcription

        result = model.transcribe(audio_data)

        

        # Get the transcribed text

        transcribed_text = result["text"]

        

        # Display the transcribed text

        st.subheader("Transcribed Text:")

        st.write(transcribed_text)

        

        # Save transcribed text to file

        with open("transcription.txt", "w") as f:

            f.write(transcribed_text)

            

        st.success("Transcription complete and saved to 'transcription.txt'")

    else:

        st.warning("Please upload an audio file to transcribe")


            
