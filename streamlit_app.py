"""
Kokoro TTS Streamlit Application
--------------------------------
A Streamlit app that provides a user interface for the Kokoro-82M text-to-speech model.
Allows users to generate and download synthesized speech with various voice options.
"""

import streamlit as st
import os, time
from openai import OpenAI
from tempfile import NamedTemporaryFile

@st.cache_resource
def get_client():
    """
    Creates and caches an OpenAI client configured for the Kokoro API.
    
    Returns:
        OpenAI: A configured OpenAI client pointing to the local Kokoro API endpoint.
    """
    return OpenAI(base_url="http://localhost:8880/v1", api_key="not-needed")

@st.cache_resource
def check_kokoro_api():
    """
    Tests connection to the Kokoro API by generating a short audio sample.
    
    Returns:
        tuple: (success_status, result)
            - success_status (bool): True if API is available, False otherwise
            - result: Audio bytes if successful, error message string if failed
    """
    try:
        client = get_client()
        with NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
            # Generate a test audio file to verify API connection
            with client.audio.speech.with_streaming_response.create(
                model="kokoro",
                voice="af",
                input="API Connected Successfully",
                response_format="mp3"
            ) as response:
                response.stream_to_file(temp_file.name)
            # Read the generated audio file
            with open(temp_file.name, "rb") as audio_file:
                audio_bytes = audio_file.read()
            # Clean up the temporary file
            os.unlink(temp_file.name)
            return True, audio_bytes
    except Exception as e:
        return False, str(e)

def toggle_voice(voice):
    """
    Toggles selection status of a voice in the session state.
    
    Args:
        voice (str): The voice ID to toggle in the selected_voices list
    """
    if voice not in st.session_state.selected_voices:
        st.session_state.selected_voices.append(voice)
    else:
        st.session_state.selected_voices.remove(voice)

# Test Kokoro API connection at startup
with st.spinner('Checking Kokoro API availability...'):
    api_available, result = check_kokoro_api()
    if not api_available:
        st.error(f"""Cannot connect to Kokoro FastAPI server. Please ensure:
        1. Docker is running
        2. Kokoro FastAPI container is running:
           ```
           docker pull remsky/kokoro-fastapi:latest
           docker run -p 8880:8880 remsky/kokoro-fastapi:latest
           ```
        Error: {result}""")
        st.stop()
    else:
        st.success('Kokoro API is available!')
        st.audio(result, format="audio/mp3", autoplay=True)

# Main app interface
st.title("Text to Speech Generator")
text_input = st.text_area("Enter text to convert to speech:", "Hello world!")

# Available voice options
base_voices = ['af', 'af_bella', 'af_sarah', 'am_adam', 'am_michael',
          'bf_emma', 'bf_isabella', 'bm_george', 'bm_lewis',
          'af_nicole', 'af_sky']

# Initialize selected voices in session state if not present
if 'selected_voices' not in st.session_state:
    st.session_state.selected_voices = []

# Voice selection interface
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

# Combine selected voices or use default
selected_voice = '+'.join(st.session_state.selected_voices) if st.session_state.selected_voices else 'af'
st.write(f"Current voice combination: {selected_voice}")

# Speech generation button and process
if st.button("Generate Speech"):
    try:
        # Get a new client instance for this generation
        client = get_client()
        with st.spinner('Generating audio...'):
            # Track generation time
            start_time = time.time()
            
            # Create temporary file for audio output
            with NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
                # Make API call to generate speech
                with client.audio.speech.with_streaming_response.create(
                    model="kokoro",
                    voice=selected_voice,
                    input=text_input,
                    response_format="mp3"
                ) as response:
                    response.stream_to_file(temp_file.name)

                # Calculate and display generation time
                end_time = time.time()
                st.success(f'Generated in {(end_time - start_time):.2f} seconds')

                # Display audio player and download button
                with open(temp_file.name, "rb") as audio_file:
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes, format="audio/mp3")
                    st.download_button("Download MP3", audio_bytes,
                                     "generated_speech.mp3", "audio/mp3")
                
                # Clean up temporary file
                os.unlink(temp_file.name)
    except Exception as e:
        st.error(f"Error generating speech. Please ensure Kokoro FastAPI is running properly: {str(e)}")