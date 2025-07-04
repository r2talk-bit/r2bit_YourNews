import os
import streamlit as st
from dotenv import load_dotenv

# Import the search_news function from utils
from utils.searchnews import search_news

# Load environment variables
load_dotenv()

# Access environment variables
app_name = os.getenv("APP_NAME", "YourNews App")

# Page configuration
st.set_page_config(
    page_title=app_name,
    page_icon="📰",
    layout="wide"
)

# Title and description
st.title("News Search")

# Create a two-column layout
left_col, right_col = st.columns([1, 2])

with left_col:
    # Input for news subject
    subject = st.text_input("Enter a subject to search for news about:")
    
    # Search button
    search_button = st.button("Search for News")
    
    # Store the search results in session state to persist between reruns
    if "news_results" not in st.session_state:
        st.session_state.news_results = ""
    
    # Call the search_news function when the button is clicked
    if search_button and subject:
        with st.spinner(f"Searching for news about {subject}..."):
            st.session_state.news_results = search_news(subject)

with right_col:
    # Display instructions initially and then search results when available
    if not st.session_state.news_results:
        st.info("### Instructions\n\nEnter a subject in the text box on the left and click 'Search for News' to see the latest news about your topic.\n\nThe results will appear here.")
        
        # Empty container for results
        st.container()
        st.markdown("### Results will appear here")
        st.markdown("---")
        st.markdown("*Waiting for your search query...*")
    else:
        # Display the search results as markdown
        st.markdown(st.session_state.news_results)

# Footer
st.markdown("---")
st.markdown("© 2025 YourNews App | Created with Streamlit")
