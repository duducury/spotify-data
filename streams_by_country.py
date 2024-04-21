# streams_by_country.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_page():
    st.title('Compare Countries by Streams')
    df = pd.read_csv('https://raw.githubusercontent.com/duducury/spotify-data/main/top5_artists_by_streams.csv')

    # Create selectors for country and year
    selected_country1 = st.selectbox('Select Country 1', df['region'].unique())
    selected_country2 = st.selectbox('Select Country 2', df['region'].unique())
    selected_year = st.selectbox('Select Year', df['year'].unique())

    # Filter DataFrame based on selected country and year
    filtered_df1 = df[(df['region'] == selected_country1) & (df['year'] == selected_year)]
    filtered_df2 = df[(df['region'] == selected_country2) & (df['year'] == selected_year)]

    # Calculate total streams for each country
    total_streams_country1 = filtered_df1['streams'].sum()
    total_streams_country2 = filtered_df2['streams'].sum()

    # Plot the bar graph
    fig, ax = plt.subplots()
    ax.bar([selected_country1, selected_country2], [total_streams_country1, total_streams_country2])
    ax.set_ylabel('Total Streams(Trillion)')
    ax.set_title(f'Total Streams Comparison for {selected_year}')
    st.pyplot(fig)
