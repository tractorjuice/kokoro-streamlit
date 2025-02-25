# Kokoro Streamlit App Guide

## Run Commands
- Start app: `streamlit run streamlit_app.py`
- Start Kokoro API: `docker pull remsky/kokoro-fastapi:latest && docker run -p 8880:8880 remsky/kokoro-fastapi:latest`
- Install dependencies: `pip install -r requirements.txt`

## Code Style
- **Imports**: Group standard library imports first, then third-party packages, then local modules
- **Formatting**: Use 4-space indentation
- **Error Handling**: Use try/except blocks with specific error messages
- **Types**: No explicit type annotations but consider adding for clarity
- **Functions**: Use descriptive function names in snake_case
- **Comments**: Add comments for complex logic or non-obvious functionality
- **Caching**: Use `@st.cache_resource` for API client and resource-intensive operations
- **UI Components**: Group related UI elements with clear labels and instructions
- **State Management**: Use Streamlit session_state for persistent data between reruns