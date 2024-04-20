import streamlit as st
import pandas as pd

# Import modules for different pages
import top_streams_artist
import global_trends
import revenue_analysis



#Paga content
def home_page(): 
    st.title('Welcome to the Spotify Data Analysis Dashboard!')
    st.markdown('---') 
 # Introduction text
    st.markdown("""
        Our main motivation for this project is to analyze data from one of the leading streaming music platforms: Spotify. 
        We aim to uncover insights into artist earnings, track the popular artists across different regions, and explore how these dynamics influence music trends and preferences worldwide.
    """)
    


    df = pd.read_csv('https://raw.githubusercontent.com/duducury/spotify-data/main/top5_artists_by_streams.csv')
    
    # raw data Checkbox
    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(df)


# Nav Menu / mapping each paga to their functions
pages = {
    "Home": home_page,  
    "Top 5 Streamed Artist": top_streams_artist.show_top_artists,
    "Global Trends": global_trends.show_page,
    "Revenue Analysis": revenue_analysis.show_page,
}

# Navigation
st.sidebar.title('Navigation')
# default  "Home" 
default_page_index = list(pages.keys()).index("Home") 

# Use the default_page_index to set the default for the radio button
option = st.sidebar.radio('Go to', list(pages.keys()), index=default_page_index)

# Call the function associated with the chosen option
if option in pages:
    pages[option]()
else:
    st.write("Something went wrong. Page not found.")
