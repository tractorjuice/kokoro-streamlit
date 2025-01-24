# Text-to-Speech Voice Generator

A Streamlit application for generating text-to-speech audio using multiple AI voices with voice combination capabilities.

## Features
- Text-to-speech conversion with multiple voice options
- Voice combination support (mix two or more voices)
- Real-time audio playback
- MP3 download option
- Generation time tracking
- Interactive voice selection interface

## Installation
```bash
pip install streamlit openai
```

## Usage
1. Run the app:
```bash
streamlit run app.py
```

2. Enter text in the input area
3. Select one or more voices using the toggle buttons
4. Click "Generate Speech" to create audio
5. Use the audio player or download button to access the generated speech

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
The app uses a custom OpenAI-compatible API endpoint. Update the `base_url` in the code to match your API endpoint:
```python
base_url="http://api.mcc.uk/v1"
```