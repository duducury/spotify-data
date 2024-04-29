# app.py

import streamlit as st
import pandas as pd
import revenue_analysis
import revcomp# Import the new module
import stremingPlatforms
import how_covid_impacts_streaming
import spotifyStreaming

# Define the function for the Home Page
def home_page():
    st.title('Welcome to the Spotify Data Analysis Dashboard!')
   
    # spotify logo 
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/168px-Spotify_logo_without_text.svg.png?20160123212544', width=200)
 # Introduction text 
    st.markdown('---') 
    st.markdown("""                
This interactive platform is designed to analyze data from one of the leading streaming music platforms: Spotify. 
Our dashboard offers a comprehensive analysis of data including:

- **The Progress of Music**: Track the evolution of music consumption from physical mediums to digital streaming.

- **Spotify Streaming Insights**: Discover music streaming trends, artist popularity, and global streaming dynamics.

- **How COVID Impacted Streaming**: Discover the impact of the COVID-19 pandemic on music streaming trends and artist popularity.

- **Royalties Comparison**: Compare the royalties generated across different platforms and what this means for artists.

- **Revenue Analysis**: Gain insights into how revenues are generated and distributed among artists and stakeholders within the Spotify ecosystem.


    """)



# Update the pages dictionary to include the new page
pages = {
    "Home": home_page,
    "The Progress of Music":stremingPlatforms.show_page,# Add the new page 
    "Spotify Streaming Insights":spotifyStreaming.show_page,
    "How Covid Impacted Streaming": how_covid_impacts_streaming.show_page,
    "Royalities Comparsion":revcomp.show_page,# Add the new page 
    "Revenue Analysis": revenue_analysis.show_page,
   
 }   
   

# Navigation menu
st.sidebar.title('Navigation')
default_page_index = list(pages.keys()).index("Home")
option = st.sidebar.radio('Go to', list(pages.keys()), index=default_page_index)

# Call the function associated with the chosen option
if option in pages:
    pages[option]()
else:
    st.write("Something went wrong. Page not found.")
