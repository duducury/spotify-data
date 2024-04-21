# streams_by_country.py

import streamlit as st
import pandas as pd

def show_page():
    st.title('Streams by Country')
    df = pd.read_csv('https://raw.githubusercontent.com/ShaneKanterman04/School/main/streams_by_country_2023.csv')

    # Allow user to select countries for comparison
    country1 = st.selectbox('Select Country 1', df['country'].unique())
    country2 = st.selectbox('Select Country 2', df['country'].unique())

    # Filter data for the selected countries
    df_country1 = df[df['country'] == country1]
    df_country2 = df[df['country'] == country2]

    # Merge data for both countries
    df_combined = pd.concat([df_country1.set_index('country'), df_country2.set_index('country')], axis=1)

    # Bar chart to compare streams between the two selected countries
    st.subheader('Streams Comparison')
    st.bar_chart(df_combined)
