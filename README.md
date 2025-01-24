# Text-to-Speech Voice Generator

A Streamlit application for generating text-to-speech audio using multiple AI voices with voice combination capabilities.

## Requirements
- Python 3.8+
- Streamlit
- OpenAI Python client
- [Kokoro FastAPI](https://github.com/remsky/Kokoro-FastAPI) running locally or on a server

## Installation
```bash
# Install Python dependencies
pip install streamlit openai

# Clone and setup Kokoro FastAPI
git clone https://github.com/remsky/Kokoro-FastAPI.git
cd Kokoro-FastAPI
pip install -r requirements.txt

# Run Kokoro FastAPI server (in a separate terminal)
python main.py
```

## Usage
1. Start Kokoro FastAPI server
2. Run the Streamlit app:
```bash
streamlit run app.py
```

## Features
- Text-to-speech conversion with multiple voice options
- Voice combination support (mix two or more voices)
- Real-time audio playback
- MP3 download option
- Generation time tracking
- Interactive voice selection interface

## Available Voices
- af (Default 50-50 mix of Bella & Sarah)
- af_bella
- af_sarah
- am_adam
- am_michael
- bf_emma
- bf_isabella
- bm_george
- bm_lewis
- af_nicole
- af_sky

## API Configuration
The app uses Kokoro FastAPI endpoint. Update the `base_url` in the code to match your endpoint:
```python
base_url="http://localhost:8880/v1"
```