# YourNews Streamlit Application

A Streamlit application for displaying and interacting with news content, powered by CrewAI for intelligent news search and analysis. This application helps you find, analyze, and present news on any topic using AI agents working together.

## What is YourNews?

YourNews is a beginner-friendly application that uses artificial intelligence to search for news articles, analyze their content, and create well-formatted newsletters. It's perfect for:

- Students learning about current events
- Professionals who need to stay updated on industry news
- Anyone interested in getting summarized news on specific topics

## How It Works

YourNews uses a team of AI agents (called a "crew") that work together like a real news team:

1. **News Researcher**: Searches the internet for the latest news on your topic
2. **News Curator/Analyst**: Selects the most important stories and writes detailed analyses
3. **Newsletter Editor**: Formats everything into a professional newsletter

## Project Structure

```
/project-root
│
├── .streamlit/        # Streamlit configuration files
│   └── secrets.toml   # Secret keys and configuration
├── assets/            # Images and other static assets
├── example/           # Example files and templates
├── utils/             # Helper functions and modules
│   └── wnews/         # News crew implementation
│       ├── config/    # Configuration files for agents and tasks
│       └── crew.py    # Main crew implementation
├── .dockerignore      # Files to exclude from Docker builds
├── .env               # Environment variables
├── .env.example       # Example environment file
├── .gitignore         # Files to exclude from git
├── Dockerfile         # Instructions for building Docker container
├── README.md          # This documentation file
├── requirements.txt   # Python dependencies
└── streamlit_app.py   # Main application file
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

### Agent Roles and Objectives

The application uses a team of specialized AI agents, each with specific roles:

1. **News Researcher**: 
   - **Objective**: Search the internet for detailed and relevant news about your topic
   - **What it does**: Identifies main news stories, filters for relevance, and prioritizes the most important ones
   - **Output**: Collects at least 30 significant news items with links and relevance comments

2. **News Curator/Analyst**: 
   - **Objective**: Transform research into meaningful analysis
   - **What it does**: Selects the 10 most impactful stories and writes detailed analyses (300-400 words each)
   - **Output**: Clear explanations of each news item's importance and potential impact

3. **Newsletter Editor**: 
   - **Objective**: Create a polished, professional newsletter
   - **What it does**: Reviews and edits all content for accuracy, clarity, and grammar
   - **Output**: A well-structured newsletter with an engaging title, introduction, detailed analyses, and additional resource links

## How to Use YourNews (For Beginners)

### Using the Streamlit Interface (Easiest Method)

1. **Start the application** (see Setup instructions below)
2. **Enter a search term** in the search box (like "climate change" or "artificial intelligence")
3. **Click the search button** and wait for the AI agents to work
4. **View your results** - a complete newsletter will be generated for you!

### Using Python Code (For Learning Programmers)

If you're learning programming, you can use YourNews in your Python code:

```python
# Basic usage - just import and call the search function
from utils.searchnews import search_news

# Search for news on a specific subject
results = search_news("artificial intelligence")
print(results)
```

### Advanced Usage (As You Learn More)

As you become more comfortable with programming, you can customize how the crew works:

```python
from utils.wnews.crew import Wnews

# Initialize the crew
news_crew = Wnews()

# Run the crew with your topic
result = news_crew.crew().kickoff(inputs={"topic": "artificial intelligence"})
print(result)
```

### Understanding the Process

When you run YourNews, here's what happens behind the scenes:

1. The **News Researcher** agent searches for at least 30 recent news items about your topic
2. The **News Curator/Analyst** agent selects the 10 most important stories and writes detailed analyses
3. The **Newsletter Editor** agent formats everything into a professional newsletter

All of this happens automatically - you just provide the topic!

## Customizing YourNews (As You Learn More)

As you become more comfortable with programming, you can customize YourNews by:

1. **Modifying agent behaviors**: Edit the YAML files in `utils/wnews/config/` to change how agents work
   - `agents.yaml`: Change agent roles, goals, and backstories
   - `tasks.yaml`: Modify what each agent does and how they do it

2. **Adding new tools**: In `crew.py`, you can add more tools to agents:
   ```python
   @agent
   def news_researcher(self) -> Agent:
       return Agent(
           config=self.agents_config['news_researcher'],
           tools=[SerperDevTool(), ScrapeWebsiteTool(), YourNewTool()],  # Add new tools here
           verbose=True
       )
   ```

3. **Creating new agents**: Add new agent definitions to `agents.yaml` and then create methods for them in `crew.py`

4. **Changing the workflow**: Modify the task dependencies in `crew.py` to change how information flows between agents

## Common Issues for Beginners

- **API Key Errors**: Make sure you've set up your API keys in the `.env` file
- **Import Errors**: Check that you've installed all requirements with `pip install -r requirements.txt`
- **No Results**: Ensure your search term is specific enough and that your internet connection is working
- **Slow Performance**: The AI agents take time to work - be patient!

## License

[Your License Information]
