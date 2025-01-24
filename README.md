# Text-to-Speech Voice Generator

A Streamlit application for generating text-to-speech audio using Kokoro-82M, a state-of-the-art TTS model that outperforms much larger models while using only 82 million parameters.

## About Kokoro TTS
Kokoro-82M is a highly efficient text-to-speech model that achieves exceptional quality with only 82M parameters, outperforming models 14x larger. The model supports:
- Multiple voice generation
- Voice mixing/combination
- High-quality speech synthesis

### Important Links
- **Try it out**: [Kokoro TTS Demo](https://huggingface.co/spaces/hexgrad/Kokoro-TTS)
- **Model**: [Kokoro-82M on Hugging Face](https://huggingface.co/hexgrad/Kokoro-82M)
- **Development**:
  - [Kokoro Inference Library](https://github.com/hexgrad/kokoro)
  - [Kokoro FastAPI](https://github.com/remsky/Kokoro-FastAPI)
- **Community**: [Discord Server](https://discord.gg/QuGxSWBfQy) (access to videos, example projects, etc.)

## Requirements
- Python 3.8+
- Streamlit
- OpenAI Python client
- Docker
- Kokoro FastAPI Docker container

## Installation

### 1. Setup Streamlit App
```bash
pip install streamlit openai
```

### 2. Start Kokoro FastAPI Server
```bash
# Pull and run the Docker container
docker pull remsky/kokoro-fastapi:latest
docker run -p 8880:8880 remsky/kokoro-fastapi:latest
```

### 3. Run the App
```bash
streamlit run streamlit_app.py
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
base_url="http://localhost:8880/v1"  # Default local Docker endpoint would be http://localhost:8880/v1
```