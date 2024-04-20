import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_top_artists():
    st.title('Spotify Top 5 Streams Artists by Region and Globally')

    # Load the dataset
    df = pd.read_csv('https://raw.githubusercontent.com/duducury/spotify-data/main/top5_artists_by_streams.csv')

    st.markdown('---')

    #Add "Global" option to select Region
    region_selection = ['Global'] + list(df['region'].unique())
    region = st.selectbox('Select Region or Global', region_selection)

    # Select Year
    year = st.selectbox('Select Year', sorted(df['year'].unique()))

    if region == 'Global':
        # Handle global aggregation for the selected year
        df_sorted = df[df['year'] == year].groupby('artist', as_index=False)['streams'].sum().sort_values(by='streams', ascending=False).head(5)
        plot_title = f'Global Top 5 Streamed Artists in {year}'
        # Convert to billions for global plotting
        conversion_factor = 1e9
        x_label = 'Billions of Streams'
    else:
        # Filter data based on selections for a specific region
        df_sorted = df[(df['region'] == region) & (df['year'] == year)].sort_values(by='streams', ascending=False)
        plot_title = f'Top Streamed Artists in {region}, {year}'
        # Convert to millions for regional plotting
        conversion_factor = 1e6
        x_label = 'Millions of Streams'

    # Plotting
    fig, ax = plt.subplots()
    ax.barh(df_sorted['artist'].iloc[::-1], df_sorted['streams'].iloc[::-1] / conversion_factor)
    ax.set_xlabel(x_label)
    ax.set_ylabel('Artist Name')
    ax.set_title(plot_title)
    st.pyplot(fig)

    # display raw data
    if st.checkbox('Show raw data!'):
        st.subheader('Raw data')
        st.write(df_sorted)

show_top_artists()
