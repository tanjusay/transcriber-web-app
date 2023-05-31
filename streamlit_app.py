import streamlit as st
import whisper

model = whisper.load_model("base")

st.title("Whisper Transcription App")
st.header("Transcribe Audio to Text")

audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav", "ogg"])

if st.button("Transcribe"):
    if audio_file is not None:
        audio_data = audio_file.read()

        result = model.transcribe(audio_data)

        transcribed_text = result["text"]

        st.subheader("Transcribed Text:")
        st.write(transcribed_text)

        with open("transcription.txt","w")as f:
            f.write(transcribed_text)

        st.success("Transcription complete and saved to 'transcription.txt'")

    else:

        st.warning("Please upload an audio file to transcribe")


            
