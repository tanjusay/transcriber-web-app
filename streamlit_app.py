import whisper
import streamlit as st


def main():
    st.set_page_config(page_title="AI Transcriber App")
    st.header("🪶 AI Transcriber App")

    model = whisper.load_model("base")

    file = st.file_uploader("Upload an MP4 file", type=["mp4"])

    if file is not None:
        result = model.transcribe(file)

        with open("transcription.txt", "w") as f:
            f.write(result["text"])

        st.subheader("Transcribed Text:")
        with open("transcription.txt", "r") as f:
            transcribed_text = f.read()
            st.write(transcribed_text)


if __name__ == "__main__":
    main()
