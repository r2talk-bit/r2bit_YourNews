"""
News search utility functions for the YourNews application.
"""

import os
import tempfile
import dotenv

# Load environment variables from .env file
dotenv.load_dotenv()

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
            
        # Run the crew
        result = Wnews().crew().kickoff(inputs={'topic': subject})
        
        return result
    except Exception as e:
        return f"CrewAI error: {str(e)}"
