# YourNews Streamlit Application

A Streamlit application for displaying and interacting with news content.

## Project Structure

```
/project-root
│
├── .streamlit/
│   └── secrets.toml
├── assets/
├── example/
├── utils/
├── .dockerignore
├── .env
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
└── streamlit_app.py
```

## Setup

### Local Development

1. Create a virtual environment:
   ```
   python -m venv venv
   ```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Update the values in `.env` with your configuration

5. Run the application:
   ```
   streamlit run streamlit_app.py
   ```

### Docker

1. Build the Docker image:
   ```
   docker build -t yournews-app .
   ```

2. Run the Docker container:
   ```
   docker run -p 8501:8501 yournews-app
   ```

3. Access the application at `http://localhost:8501`

## Configuration

- Environment variables are stored in the `.env` file
- Secrets are stored in `.streamlit/secrets.toml`

## License

[Your License Information]
