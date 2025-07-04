"""
News search utility functions for the YourNews application.
"""

import os
import sys
import tempfile
from datetime import datetime
from pathlib import Path
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

# Import CrewAI components
from crewai import Agent, Crew, Process, Task
from crewai_tools import SerperDevTool
from utils.wnews.crew import Wnews

def search_news(subject):
    """
    Search for news articles based on the provided subject using CrewAI.
    
    Args:
        subject (str): The subject to search for news about
        
    Returns:
        str: Markdown formatted string containing news articles
    """
    if not subject:
        return "Please enter a subject to search for news."
    
    # Check if API keys are set
    serper_api_key = os.environ.get('SERPER_API_KEY')
    openai_api_key = os.environ.get('OPENAI_API_KEY')
    
    # Log API key status
    missing_keys = []
    if serper_api_key and openai_api_key:
        print("Info: Both SERPER_API_KEY and OPENAI_API_KEY are set.")
    else:
        if not serper_api_key:
            missing_keys.append('SERPER_API_KEY')
        if not openai_api_key:
            missing_keys.append('OPENAI_API_KEY')
        print(f"Info: Missing API keys: {', '.join(missing_keys)}")
        return _mock_search_news(subject, missing_keys)
    
    # Use CrewAI implementation
    try:
        # Create a temporary file to store the output
        with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.md') as temp_file:
            output_path = temp_file.name
        
        # Import necessary components directly
        from crewai import Agent, Task, Crew
        from crewai_tools import SerperDevTool
        
        # Create a search tool
        search_tool = SerperDevTool()
        
        # Create agents directly with ASCII-only text to avoid encoding issues
        researcher = Agent(
            role="AI News Researcher",
            goal=f"Find the most relevant and recent information about {subject}",
            backstory="You are an expert at finding and analyzing news and information from various sources.",
            verbose=True,
            tools=[search_tool]
        )
        
        writer = Agent(
            role="AI Content Writer",
            goal=f"Write engaging and informative content about {subject}",
            backstory="You are a skilled writer who can transform research into compelling narratives.",
            verbose=True
        )
        
        editor = Agent(
            role="Newsletter Editor",
            goal="Create a polished final newsletter with proper formatting and structure",
            backstory="You ensure all content is accurate, well-organized, and ready for distribution.",
            verbose=True
        )
        
        # Create tasks with ASCII-only text
        research_task = Task(
            description=f"Research the latest news and developments about {subject}. Find at least 5 relevant sources.",
            expected_output="A detailed research report with links to sources and key findings.",
            agent=researcher
        )
        
        writing_task = Task(
            description=f"Based on the research, write an informative article about {subject}. Include analysis of trends and impacts.",
            expected_output="A well-written article with sections covering different aspects of the subject.",
            agent=writer,
            context=[research_task]
        )
        
        editing_task = Task(
            description="Review and edit the article into a newsletter format. Ensure proper structure, formatting, and clarity.",
            expected_output="A polished newsletter ready for distribution.",
            agent=editor,
            context=[writing_task],
            output_file=output_path
        )
        
        # Create the crew
        crew = Crew(
            agents=[researcher, writer, editor],
            tasks=[research_task, writing_task, editing_task],
            verbose=True
        )
        
        # Run the crew
        result = crew.kickoff()
        
        # Read the output file
        if os.path.exists(output_path):
            with open(output_path, 'r') as f:
                content = f.read()
            
            # Clean up temporary file
            os.unlink(output_path)
            return content
        else:
            return result
            
    except Exception as e:
        print(f"Error using CrewAI: {str(e)}")
        return _mock_search_news(subject, [f"CrewAI error: {str(e)}"])


def _mock_search_news(subject, missing_keys=None):
    """
    Provides mock news results when CrewAI is not available.
    
    Args:
        subject (str): The subject to search for news about
        missing_keys (list, optional): List of missing API keys
        
    Returns:
        str: Markdown formatted string containing mock news articles
    """
    current_date = datetime.now()
    date_str = current_date.strftime("%B %d, %Y")
    yesterday = current_date.replace(day=current_date.day-1)
    yesterday_str = yesterday.strftime("%B %d, %Y")
    two_days_ago = current_date.replace(day=current_date.day-2)
    two_days_ago_str = two_days_ago.strftime("%B %d, %Y")
    
    mock_news = f"""
# News Results for: {subject}

## Top Headlines

### {subject} Makes Waves in Technology Sector
*{date_str}* - Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nullam euismod, nisl eget aliquam ultricies, nunc nisl aliquet nunc, quis
aliquam nisl nunc eu nisl. Nullam euismod, nisl eget aliquam ultricies.

### New Developments in {subject} Research
*{yesterday_str}* - Praesent euismod, nisl eget aliquam ultricies, nunc nisl
aliquet nunc, quis aliquam nisl nunc eu nisl. Nullam euismod, nisl eget
aliquam ultricies, nunc nisl aliquet nunc.

### {subject} Industry Sees Record Growth
*{two_days_ago_str}* - Vestibulum ante ipsum primis in faucibus orci luctus et
ultrices posuere cubilia curae; Nullam euismod, nisl eget aliquam ultricies,
nunc nisl aliquet nunc, quis aliquam nisl nunc eu nisl.

## Related Stories

- **Expert Analysis**: What {subject} Means for the Future
- **Opinion**: Why {subject} Matters in Today's World
- **Market Impact**: How {subject} is Changing Industries

## Trending Topics Related to {subject}

1. {subject} Innovation
2. {subject} Technology
3. {subject} Market Trends
4. Future of {subject}

---

"""    
    # Add note about missing API keys if applicable
    if missing_keys:
        mock_news += f"*Note: This is a mock response because the following API keys are missing: {', '.join(missing_keys)}. "
        mock_news += "Please ensure these keys are set in your .env file to enable real news search.*"
    else:
        mock_news += "*Note: This is a mock response. Real news search functionality is not available at this time.*"
        
    return mock_news
