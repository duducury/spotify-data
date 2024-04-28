import streamlit as st
import pandas as pd
import plotly.express as px

# intro
def show_page():
    st.title('The Progress of Music Streaming Services')
    st.markdown('''
        Here, we'll analyze the impressive growth of streaming 
        subscribers and compare the major players in this new era of streaming.
    ''')


   #  Music Consumption 
    st.markdown('---')
    st.title(' Music Consumption Comparison (2010 - 2019) ')
    st.markdown('''
        The way we listen to music has changed!
        Let's take a look at the music consumption difference between 2010 and 2019.
    ''')

# Data for comparison between 2010 and 2019
# reference: https://www.clickondetroit.com/news/local/2019/12/31/heres-how-the-way-we-listen-to-music-has-changed-since-the-start-of-the-decade/
    data = {
        'Year': [2010, 2019],
        'Physical (CDs)': [52, 9],
        'Digital Downloads': [38, 9],
        'Syncing (TV)': [3, 2],
        'Streaming Services': [7, 80]
    }
    df_music_consumption = pd.DataFrame(data)
    df_music_consumption_melted = df_music_consumption.melt(id_vars='Year', 
                                                            var_name='Method', 
                                                            value_name='Percentage')

# Year dropdown
    year_choice = st.selectbox('Select a Year to Compare:', df_music_consumption['Year'].unique())

# Filter data by year
    data_pie = df_music_consumption_melted[df_music_consumption_melted['Year'] == year_choice]
    fig_pie = px.pie(data_pie, values='Percentage', names='Method',
                    title=f'Music Consumption in {year_choice}',
                    color='Method', 
                    hover_data=['Percentage'],  
                    labels={'Method':'Method: '} 
                    )
    # Update the pie template
    fig_pie.update_traces(
        hoverinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>Percentage: %{percent}',
        textposition='outside', textinfo='percent+label'
    )
    st.plotly_chart(fig_pie)




    # Subscriber Growth Over the Years
    st.markdown('---')
    st.markdown('''
        ## Subscriber Growth Over the Years
        As we can see from the bar chart below, the number of music streaming services subscribers
        over the last seven yeas has grown wilsly, being able to change the way we listen to music.
    ''')
    url_total_subs = 'https://raw.githubusercontent.com/duducury/spotify-data/main/totalMusicStreamSubs2015-2022.csv'
    df_total_subs = pd.read_csv(url_total_subs)
    df_total_subs['Year'] = pd.to_datetime(df_total_subs['Year'], format='%Y')

    #  display the bar plot 
    fig_total_subs = px.bar(df_total_subs, x='Year', y='Total Streaming Subscribers', title='Streaming subscribers',
                            labels={'Total Streaming Subscribers': 'Total Subscribers',
                                     'Year': 'Year'})
    st.plotly_chart(fig_total_subs)



    # Streaming Platforms Comparison 
    st.markdown('---')
    st.title('Streaming Platforms Comparison (2016-2022)')
    st.markdown('''
        The number of streaming Subscrivers was been growing and 
        the competition between the main platforms becomes more intense. 
    ''')

    url = 'https://raw.githubusercontent.com/duducury/spotify-data/main/2016-2022streamsByPlatforms.csv'
    df = pd.read_csv(url)
    
    # Replace 'NAN' with 0 
    df = df.replace('NAN', 0)
    df['year'] = pd.to_datetime(df['year'], format='%Y')


    # user selectbox
    year_choice = st.selectbox('Select a Year from the Pie Chart:', df['year'].dt.year.unique())

    # Filter data 
    data_pie = df[df['year'].dt.year == year_choice]
    platform_data = data_pie.iloc[0, 1:].reset_index()
    platform_data.columns = ['Platform', 'Streams']

    # Create a pie chart
    fig_pie = px.pie(platform_data, values='Streams', names='Platform', title=f'Streams by Platform in {year_choice}',
                     color='Platform', 
                     hover_data=['Streams'],  
                     labels={'Platform':'Platform: '} 
                    )
    fig_pie.update_traces(textposition='outside', textinfo='label+percent')
    st.plotly_chart(fig_pie)



    # Music Streaming Subscribers by Different Apps
    st.markdown('---')
    st.title('Music Streaming Subscribers by Different Apps')   
    st.markdown('''
        This line chart plots the number of music streaming subscriber from 2016 to 2022 from diferent streaming platforms
    ''')
    #line plot
    long_df = df.melt(id_vars=['year'], var_name='Platform', value_name='Subscribers')
    long_df['year'] = long_df['year'].dt.year  # Convert datetime to int year for plotting

    fig_line = px.line(long_df, x='year', y='Subscribers', color='Platform', title='Data collected from 2016 to 2022',
                       markers=True, labels={'Subscribers': 'Number of Subscribers', 'year': 'Year'})
    st.plotly_chart(fig_line)



    # Platforms Comparison Table
    st.markdown('---')
    st.title('Platforms Comparison Table')
    url_platforms_comparison = 'https://raw.githubusercontent.com/duducury/spotify-data/main/ComparePlatforms.csv'
    df_platforms_comparison = pd.read_csv(url_platforms_comparison)

    # set 'Streaming Service' as the index 
    df_platforms_comparison.set_index('Streaming Service', inplace=True)
    st.dataframe(df_platforms_comparison)



    st.markdown('---')
    st.title('What contributes to Spotify success?')
    st.markdown("""
    - **Pioneering**: One of the first companies to enter into the music streaming market.
    - **User Experience (UX)**: Spotify offers a clean, intuitive, and user-friendly interface.
    - **Freemium Model**: Allows free access with the option to upgrade for additional benefits.
    - **Strategic Partnerships**: With record labels, artists, and telecom companies.
    - **Extensive Music Library**: Provides access to a vast library of songs and podcasts.
    - **Offline Downloading**: Enables users to download music and listen without an internet connection.
    - **Global Presence**: Available in numerous countries, catering to a global market.
    - **Personalization**: Delivers personalized playlists and recommendations.
    - **Platform Integration**: Service integration with various devices and platforms.
    - **Continuous Innovation**: Regular updates with new features and improvements.
""")



    st.markdown('---')
    st.title('Conclusion: The Future of Music Consumption')
    st.markdown('''
        In conclusion, The Music Consumption market was changed drastically from physical CDs all way to streaming services.
        As we look to the future, streaming services will likely continue to innovate 
        and evolve, with new features, business models, AI Integration, and partnerships reshaping even further. 
        One thing is clear: streaming has changed the music industry forever, and spotify has been of the greatest contributors for this transformation.
    ''')


if __name__ == "__main__":
    show_page()
