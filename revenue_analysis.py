# revenue_analysis.py
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
def show_page():
    R_dict = {
        'Premium Services' : 88,
        'Ad-Supported Services' : 12
    }
    Gross_dict = {
        'Premium Services' : 95,
        'Ad-Supported Services' : 5
    }
    Revenue = pd.Series(R_dict)
    Gross_profit = pd.Series(Gross_dict)
    Rev = pd.DataFrame({'Revenue': Revenue, 'Gross Profit':Gross_profit})

    def Revenue1():
        fig1 = px.pie(Rev, values='Revenue', names=Rev.index)
        return fig1
    fig1 = Revenue1()
    
    def Gross():
        fig2 = px.pie(Rev, values='Gross Profit', names=Rev.index)
        return fig2
    fig2 = Gross()

    
    st.title('Revenue Analysis')
    st.write("""Spotify(SPOT) is a Swedish audio streaming and media service provider that was founded on April 23, 2006 by Daniel Ek and Martin Lorentzon.
             The Company went public in 2018 with its initial stock shares being traded for \$165.90 a share thus requiring Spotify to disclose all financial information.
             Spotify offers its services globally with Spotify being available in 184 countries and territories and has roughly around 602 million monthly active users
              and 236 million Premium Subscribers as of December 31, 2023.""")
    st.subheader('Spotify Revenue Based on 2021')
    st.plotly_chart(fig1)
    st.subheader('Spotify Gross Profit Based on 2021')
    st.plotly_chart(fig2)
    st.write("""Spotify despite its pure massive amounts of streams and possible add revenue from said streams, majority of the money made from its platform is generated from its premium monthly or yearly subscriptions. 
              Premium Subscribers of spotify are able to enjoy unlimited online and offline access to their entire catalog of music and podcasts without having to listen to any commercials.""")
    st.subheader('Spotify Subscription Cost:')
    st.markdown("""
- Premium Individual: \$10.99 per month.
- Premium Duo: \$14.99 per month. Like the Individual plan, the Duo option provides all the same Premium features, but with the option for two accounts
- Premium Family: \$16.99 per month. The Family plan includes all of the features of the Individual plan but is meant for up to 6 people
- Premium Student: \$5.99 per month. Student plan comes with the same features as the Individual option and can be used for up to four years but need to use a school email.
                """)

    st.write(""" """)
    st.set_option('deprecation.showPyplotGlobalUse', False)
if __name__ == "__main__":
    show_page()
