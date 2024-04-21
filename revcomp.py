import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
def show_page():

    st.title('Compare Spotify Royalities to its Streaming Competitors')
    df = pd.read_csv('https://raw.githubusercontent.com/duducury/spotify-data/main/top5_artists_by_streams.csv')
    df['Spotify'] = (df['streams'] / 100000) * 400
    df['Apple Music'] = (df['streams'] / 100000) * 800
    df['Tidal'] = (df['streams'] / 100000) * 1500
    df['YouTube Music'] = (df['streams'] / 100000) * 200
    df['Amazon Music'] = (df['streams'] / 100000) * 550
    df['Deezer'] = (df['streams'] / 100000) * 400

    def Streaming_rev():
        #Sidebar selection
        year = st.selectbox('Select Year', df['year'].unique())
        artist = st.selectbox('Select Artist', df['artist'].unique())

        # Filter data based on selection
        filtered_df = df[(df['year'] == year) & (df['artist'] == artist)]

        if st.checkbox('Show raw data'):
            st.subheader('Raw data')
            st.write(filtered_df)

        # Plot the revenue data
    
        platforms = ['YouTube Music', 'Spotify', 'Deezer', 'Amazon Music', 'Apple Music', 'Tidal']
        revenue_data = filtered_df[platforms].values[0]

        fig, ax = plt.subplots()
        ax.barh(platforms, revenue_data)
        plt.xlabel('Streaming Platform')
        plt.ylabel('Revenue')
        plt.title('Streaming Revenue for {} in {}'.format(artist, year))

        plt.xticks(rotation=45, ha='right')
        
    fig = Streaming_rev()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    
    st.pyplot(fig)

    st.markdown("""Spotify, despite being one of the most well-known streaming services with a large volume of daily streams, doesn't pay its artists the most when it comes to royalties.
Spotify only pays about \$0.003-\$0.005 per stream, which amounts to roughly \$400 for every 100,000 streams. On the other hand, a less popular streaming service named Tidal pays approximately
\$1,250 to \$1,500 for every 100,000 streams on their platform. 

The chart provides a breakdown of each artist's earnings on Spotify by year and compares the same number of streams across multiple platforms.

Caution: Will have an error for some selections due to missing data""")
    st.markdown("""Streaming royalties paid by popular platforms:
- Spotify: \$0.003-\$0.005 per stream. Artists can expect around \$400 for every 100,000 streams.
- Apple Music: \$0.006-\$0.008 per stream. Artists can expect \$600 to \$800 for every 100,000 streams.
- Tidal: \$0.0125-\$0.015 per stream. Artists can expect \$1,250 to \$1,500 for every 100,000 streams on this platform.
- YouTube Music: \$0.001-\$0.003 per stream. Artists can expect \$100 to \$300 for every 100,000 streams.
- Amazon Music: \$0.004-\$0.007 per stream. Artists can expect \$400 to \$700 for every 100,000 streams.
- Deezer: \$0.005-\$0.007 per stream. Artists can expect \$500 to \$700 for every 100,000 streams.""")
if __name__ == "__main__":
    show_page()
