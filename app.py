# app.py

import streamlit as st
import pandas as pd
import top_streams_artist
import global_trends
import revenue_analysis
import streams_by_country
import revcomp# Import the new module
import stremingPlatforms
import how_covid_impacts_streaming


# Define the function for the Home Page
def home_page():
    st.title('Welcome to the Spotify Data Analysis Dashboard!')
    st.markdown('---') 

     col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image('https://upload.wikimedia.org/wikipedia/commons/thumb/1/19/Spotify_logo_without_text.svg/168px-Spotify_logo_without_text.svg.png?20160123212544', width=200)
 # Introduction text
    st.markdown("""                
This interactive platform is designed to analyze data from one of the leading streaming music platforms: Spotify. 
Our dashboard offers a comprehensive analysis of data including:

- **Top 5 Streamed Artists**: Discover the most popular artists on Spotify, From Global to Region .

- **Global Trends**: Explore a beutiful Choropleth Map.

- **Revenue Analysis**: Gain insights into how revenues are generated and distributed among artists and stakeholders within the Spotify ecosystem.

- **Compera Streams by Country**: Compare two regions according to the number of streamers per year.

- **Royalties Comparison**: Compare the royalties generated across different platforms and what this means for artists.

- **The Progress of Music**: Track the evolution of music consumption from physical mediums to digital streaming.

- **How COVID Impacted Streaming**: Discover the impact of the COVID-19 pandemic on music streaming trends and artist popularity.
    
    """)



# Update the pages dictionary to include the new page
pages = {
    "Home": home_page,
    "Top 5 Streamed Artist": top_streams_artist.show_top_artists,
    "Global Trends": global_trends.show_page,
    "Revenue Analysis": revenue_analysis.show_page,
    "Streams by Country": streams_by_country.show_page,
    "Royalities Comparsion":revcomp.show_page,# Add the new page
    "The Progress of Music":stremingPlatforms.show_page,# Add the new page
    "How Covid Impacted Streaming": how_covid_impacts_streaming.show_page,
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
