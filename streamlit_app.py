import whisper
import streamlit as st


def main():
    st.set_page_config(page_title="AI Transcriber App")
    st.header("🪶 AI Transcriber App")
    
    model = whisper.load_model("base")
    
    file = st.file_uploader("Upload a video file", type=["mp4"])
    
    if file is not None:
        # Transcribe the video
        result = model.transcribe(file)
        
        # Save the transcription to a text file
        with open("transcription.txt", "w") as f:
            f.write(result["text"])
        
        st.success("Transcription completed and saved to transcription.txt")
    else:
        st.info("Please upload a video file (.mp4)")
        

if __name__ == "__main__":
    main()
