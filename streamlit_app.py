import streamlit as st
import os, time
from openai import OpenAI
from tempfile import NamedTemporaryFile

@st.cache_resource
def get_client():
    return OpenAI(base_url="http:localhost:8880/v1", api_key="not-needed")

def toggle_voice(voice):
    if voice not in st.session_state.selected_voices:
        st.session_state.selected_voices.append(voice)
    else:
        st.session_state.selected_voices.remove(voice)

st.title("Text to Speech Generator")
text_input = st.text_area("Enter text to convert to speech:", "Hello world!")

base_voices = ['af', 'af_bella', 'af_sarah', 'am_adam', 'am_michael',
          'bf_emma', 'bf_isabella', 'bm_george', 'bm_lewis',
          'af_nicole', 'af_sky']

if 'selected_voices' not in st.session_state:
    st.session_state.selected_voices = []

st.write("Select voices to combine:")
cols = st.columns(3)
for idx, voice in enumerate(base_voices):
    with cols[idx % 3]:
        st.button(
            voice,
            key=f"btn_{voice}",
            type="primary" if voice in st.session_state.selected_voices else "secondary",
            on_click=toggle_voice,
            args=(voice,)
        )

selected_voice = '+'.join(st.session_state.selected_voices) if st.session_state.selected_voices else 'af'
st.write(f"Current voice combination: {selected_voice}")

if st.button("Generate Speech"):
    try:
        client = get_client()
        with st.spinner('Generating audio...'):
            start_time = time.time()
            with NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
                with client.audio.speech.with_streaming_response.create(
                    model="kokoro",
                    voice=selected_voice,
                    input=text_input,
                    response_format="mp3"
                ) as response:
                    response.stream_to_file(temp_file.name)

                with open(temp_file.name, "rb") as audio_file:
                    audio_bytes = audio_file.read()
                    end_time = time.time()
                    st.success(f'Generated in {(end_time - start_time):.2f} seconds')
                    st.audio(audio_bytes, format="audio/mp3")
                    st.download_button("Download MP3", audio_bytes,
                                     "generated_speech.mp3", "audio/mp3")
                os.unlink(temp_file.name)
    except Exception as e:
        st.error(f"Error generating speech: {str(e)}")