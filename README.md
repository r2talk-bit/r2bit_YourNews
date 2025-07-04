# YourNews Streamlit Application

A Streamlit application for displaying and interacting with news content, powered by CrewAI for intelligent news search and analysis.

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
- Required API keys:
  - `SERPER_API_KEY`: API key for the SerperDev search tool
  - `OPENAI_API_KEY`: API key for OpenAI services used by CrewAI

## Features

### CrewAI Integration

YourNews uses CrewAI to create intelligent agent-based workflows for news search and analysis:

- **News Search**: Search for news articles on any subject using the SerperDev search tool
- **Content Analysis**: AI agents analyze and summarize news content
- **Newsletter Generation**: Automatically generate well-formatted newsletters based on search results

### Agent Roles

The application uses a team of specialized AI agents:

1. **Researcher**: Finds and collects relevant news articles
2. **Writer**: Transforms research into engaging content
3. **Editor**: Formats and polishes the final output

### Usage

You can use the CrewAI functionality in two ways:

1. **Through the Streamlit interface**: Simply enter a search term in the search box
2. **Programmatically**: Use the `search_news()` function from the `utils.searchnews` module

```python
from utils.searchnews import search_news

# Search for news on a specific subject
results = search_news("artificial intelligence")
print(results)
```

### Advanced Usage

For advanced usage and customization, you can use the Wnews crew directly:

```python
from utils.wnews.crew import Wnews

# Initialize the crew
news_crew = Wnews()

# Run the crew
result = news_crew.crew().kickoff()
print(result)
```

## License

[Your License Information]
