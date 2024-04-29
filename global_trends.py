import streamlit as st
import pandas as pd
import plotly.express as px

def show_page():
    df = pd.read_csv('https://raw.githubusercontent.com/duducury/spotify-data/main/top5_artists_by_streams.csv')

    #choropleth map
    def choropleth_map(year):
        filtered_df = df[df['year'] == year]
        aggregated_data = filtered_df.groupby('region', as_index=False).agg({'streams': 'sum'})
        blue_scale = ['rgba(173, 216, 230, 1)', 'rgba(0, 0, 255, 1)']

        fig = px.choropleth(aggregated_data, locations='region', locationmode='country names',
                            color='streams', hover_data=['region', 'streams'],
                            title=f'Number of Streams by Region in {year}',
                            color_continuous_scale= blue_scale, range_color=(0, 8e9))
        fig.update_layout(geo=dict(showframe=False, showcoastlines=True))
        return fig

    st.title('Global trends')
    st.subheader('Choropleth Map of Spotify Streams by Region and Year')


    year = st.selectbox('Select Year', df['year'].unique())

    # Display the choropleth map
    fig = choropleth_map(year)
    st.plotly_chart(fig)


    selected_region = st.selectbox('Select a region to display the number of streams', df['region'].unique())
    selected_data = df[(df['year'] == year) & (df['region'] == selected_region)]
    aggregated_data = selected_data.groupby('region', as_index=False).agg({'streams': 'sum'})
    if not selected_data.empty:
        selected_streams = aggregated_data['streams'].values[0]
        st.write(f"Region: {selected_region}")
        st.write(f"Number of Streams: {selected_streams}")
    else:
        st.write("No data available for the selected region and year.")
    st.markdown('---')
    st.subheader('Highest and Lowest Number of Streams for Each Year')
    def streaming_revenue():
        df_grouped = df.groupby('year')['streams'].agg(['max', 'min']).reset_index()
        df_grouped = df_grouped.rename(columns={'max': 'Highest Stream', 'min': 'Lowest Stream'})

        figure2 = px.bar(df_grouped, x='year', y=['Highest Stream', 'Lowest Stream'], barmode='group', title='High and Low Number of Streams for Each Year')

        figure2.update_layout(
            xaxis_title='Year',
            yaxis_title='Streams',
            legend_title='Revenue'
        )

        return figure2

    figure2 = streaming_revenue()
    st.plotly_chart(figure2)

if __name__ == "__main__":
    show_page()
