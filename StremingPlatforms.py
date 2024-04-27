import streamlit as st
import pandas as pd
import plotly.express as px

# intro
def show_page():
    st.title('The Progress of Music Streaming Services (2015-2022)')
    st.markdown('''
        Here, we'll analyze the impressive growth of streaming 
        subscribers and compare the major players in this new era of streaming.
    ''')

    st.markdown('---')


    # Global Music Consumption 
    st.title('Global Music Consumption ')
    st.markdown('''
        Let's take a look at the 2022 different music consumption.
    ''')\
    # CSV dataset
    url_global_music = 'https://raw.githubusercontent.com/duducury/spotify-data/main/GlobalMusicConsumption.csv'
    df_global_music = pd.read_csv(url_global_music)

    # Convert the 'SHARE' column to a numeric type after removing the '%' sign
    df_global_music['SHARE'] = df_global_music['SHARE'].str.replace('%', '').astype(float)

    # horizontal bar plot for global music consumption
    fig_global_music = px.bar(df_global_music, x='SHARE', y='SERVICE', orientation='h',
                            labels={'SHARE': 'Share in (%)', 
                                    'SERVICE': 'Service'},
                            text='SHARE')  
    # sort the bars 
    fig_global_music.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig_global_music)


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
    st.markdown('''
   
    ''')



    st.markdown('---')
    st.title('Conclusion: The Future of Music is Streaming')

if __name__ == "__main__":
    show_page()
