import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_page():
    # Load the data from the provided CSV URL
    url = "https://raw.githubusercontent.com/duducury/spotify-data/main/top5_artists_by_streams.csv"
    data = pd.read_csv(url)

    # Grouping the data by year and summing the streams
    streaming_data = data.groupby('year')['streams'].sum().reset_index()

    st.title("How Covid Impacted Streaming")

    # Plotting with Matplotlib
    plt.figure(figsize=(10, 6))
    plt.plot(streaming_data['year'], streaming_data['streams'], marker='o')
    plt.title('How Covid Impacted Streaming Numbers')
    plt.xlabel('Year')
    plt.ylabel('Total Streams (Billions)')
    plt.grid(True)
    st.pyplot(plt)

    # Analysis
    st.write("## Analysis:")
    st.write("The data reveals interesting patterns in streaming numbers surrounding the COVID-19 pandemic. Prior to the onset of COVID-19, there was a gradual decline in streaming numbers, indicating a possible trend of saturation or shifting consumer preferences. However, this trend abruptly changed with the emergence of the pandemic.")
    st.write("Once COVID-19 started spreading globally and governments implemented lockdown measures, there was a notable spike in total streams. This surge can be attributed to several factors. Firstly, with people spending more time at home due to lockdowns and social distancing measures, there was an increased demand for entertainment options.")
    st.write("Additionally, the closure of cinemas, theaters, and other entertainment venues likely led individuals to seek alternative forms of entertainment, such as streaming music and movies. Moreover, with remote work and online learning becoming the norm, individuals may have turned to streaming platforms to help alleviate stress and create a sense of normalcy during uncertain times.")
    st.write("Furthermore, the availability of diverse content on streaming platforms, coupled with advancements in technology and streaming services' aggressive marketing strategies, also contributed to the surge in streaming numbers.")
    st.write("In summary, the spike in streaming numbers during the COVID-19 pandemic underscores the resilience and adaptability of the streaming industry. It also highlights the crucial role that digital entertainment platforms play in providing accessible and engaging content, particularly during times of crisis.")
    st.write("As we move forward, it will be interesting to observe whether the streaming habits formed during the pandemic will persist or if there will be shifts in consumer behavior as societal norms evolve.")
