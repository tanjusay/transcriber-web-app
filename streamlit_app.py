import streamlit as st

import asyncio

import websockets

import numpy as np

import sounddevice as sd



st.title("Whisper Transcriber")

# Constants for audio recording

duration = 10  # Recording duration in seconds

sample_rate = 16000  # Audio sample rate



async def transcribe_audio(audio_frames):

    async with websockets.connect('wss://whisper-asr.api.cloud.openai.com/speech-to-text/v1/whisper/asr/streaming') as websocket:

        for frame in audio_frames:

            await websocket.send(frame.tobytes())

            result = await websocket.recv()

            # Process and display the result as needed

            st.write(result)

# Streamlit app content

with st.beta_container():

    recording = st.empty()

    if st.button("Start/Stop Recording"):

        if recording.button_value:

            recording.button_value = False

            recording.empty()

        else:

            recording.button_value = True

            recording_text = st.empty()

            audio_frames = []

            def callback(indata, frames, time, status):

                audio_frames.append(indata.copy())

            with sd.InputStream(callback=callback, channels=1, samplerate=sample_rate):

                st.write("Recording started. Click 'Start/Stop Recording' to stop.")

                while recording.button_value:

                    pass

            st.write("Recording stopped. Transcribing audio...")

            audio_data = np.concatenate(audio_frames)

            loop = asyncio.get_event_loop()

            loop.run_until_complete(transcribe_audio(audio_data))

