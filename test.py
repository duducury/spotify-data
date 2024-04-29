import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def show_page():
    st.title('Spotify Streaming Insights')
# 
# 
    # Load the dataset
    df = pd.read_csv('https://raw.githubusercontent.com/duducury/spotify-data/main/top5_artists_by_streams.csv')
# 
#Add "Global" option to select Region
    st.markdown('---')
    st.title('Spotify Top 5 Streamed Artists by Region and Globally')
    region_selection = ['Global'] + list(df['region'].unique())
    region = st.selectbox('Select Region or Global', region_selection, key='region_select')
    # Select Year
    year_artist = st.selectbox('Select Year', sorted(df['year'].unique()), key='year_artist')
     # Handle global aggregation for the selected year
    if region == 'Global':
        df_sorted = df[df['year'] == year_artist].groupby('artist', as_index=False)['streams'].sum().sort_values(by='streams', ascending=False).head(5)
        plot_title = 'Global Top 5 Streamed Artists'
        # Convert to billions for global plotting
        conversion_factor = 1e9
        x_label = 'Billions of Streams'
    else:
        # Filter data based on selections for a specific region
        df_sorted = df[(df['region'] == region) & (df['year'] == year_artist)].sort_values(by='streams', ascending=False)
        plot_title = f'Top Streamed Artists in {region}'
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




# 
# 
# Compare countries by streams
    st.markdown('---')
    st.title('Compare Countries by Streams')
     # Create selectors for country and year
    selected_country1 = st.selectbox('Select Country 1', df['region'].unique(), key='country1')
    selected_country2 = st.selectbox('Select Country 2', df['region'].unique(), key='country2')
    selected_year = st.selectbox('Select Year', df['year'].unique(), key='compare_year')
    # Filter DataFrame based on selected country and year
    filtered_df1 = df[(df['region'] == selected_country1) & (df['year'] == selected_year)]
    filtered_df2 = df[(df['region'] == selected_country2) & (df['year'] == selected_year)]
        # Calculate total streams for each country
    total_streams_country1 = filtered_df1['streams'].sum()
    total_streams_country2 = filtered_df2['streams'].sum()
    # Plot the bar graph
    fig, ax = plt.subplots()
    ax.bar([selected_country1, selected_country2], [total_streams_country1, total_streams_country2])
    ax.set_ylabel('Total Streams (Trillions)')
    ax.set_title(f'Total Streams Comparison for {selected_year}')
    st.pyplot(fig)

    st.write("The comparison of streaming numbers between countries reveals that more developed countries tend to have higher total stream numbers. This correlation can be attributed to various factors associated with development, such as access to high-speed internet, disposable income, and technological infrastructure.")
    st.write("In more developed countries, individuals are more likely to have access to streaming platforms and are often early adopters of new technologies. Additionally, higher disposable incomes enable people to subscribe to streaming services and access a wider range of content.")
    st.write("Furthermore, developed countries often have better internet infrastructure and connectivity, which facilitates smoother streaming experiences and encourages more frequent usage of streaming platforms.")
    st.write("While this correlation between development and streaming numbers is evident, it's important to note that cultural factors, government regulations, and the availability of local content can also influence streaming habits within each country.")




# 
# 
# Choropleth map section
    st.markdown('---')

    
    st.title('Choropleth Map of Spotify Streams by Region and Year')
    year_map = st.selectbox('Select Year for Map', df['year'].unique(), key='year_map')
    fig = choropleth_map(df, year_map)
    st.plotly_chart(fig)

    # Revenue trends section
    st.markdown('---')
    st.subheader('Highest and Lowest Number of Streams for Each Year')
    figure2 = streaming_revenue(df)
    st.plotly_chart(figure2)



def choropleth_map(df, year):
    filtered_df = df[df['year'] == year]
    aggregated_data = filtered_df.groupby('region', as_index=False).agg({'streams': 'sum'})
    blue_scale = ['rgba(173, 216, 230, 1)', 'rgba(0, 0, 255, 1)']

    fig = px.choropleth(aggregated_data, locations='region', locationmode='country names',
                        color='streams', hover_data=['region', 'streams'],
                        title=f'Number of Streams by Region in {year}',
                        color_continuous_scale= blue_scale, range_color=(0, 8e9))
    fig.update_layout(geo=dict(showframe=False, showcoastlines=True))
    return fig

def streaming_revenue(df):
    df_grouped = df.groupby('year')['streams'].agg(['max', 'min']).reset_index()
    df_grouped = df_grouped.rename(columns={'max': 'Highest Stream', 'min': 'Lowest Stream'})

    figure2 = px.bar(df_grouped, x='year', y=['Highest Stream', 'Lowest Stream'], barmode='group',
                     title='High and Low Number of Streams for Each Year')
    figure2.update_layout(
        xaxis_title='Year',
        yaxis_title='Streams',
        legend_title='Stream Count'
    )
    return figure2

if __name__ == "__main__":
    show_page()
