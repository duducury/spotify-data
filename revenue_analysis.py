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
    I_dict = {
        'Music Streaming' : 84,
        'Other' : 16
    }
    D_dict = {
        'Royalties,Etc' : 70,
        'Other' : 30
    }
    Revenue = pd.Series(R_dict)
    Gross_profit = pd.Series(Gross_dict)
    
    Debt = pd.Series(D_dict)

    Industy = pd.Series(I_dict)

    Rev = pd.DataFrame({'Revenue': Revenue, 'Gross Profit':Gross_profit})
    Ind = pd.DataFrame({'Music Industy': Industy,})
    Debt1 = pd.DataFrame({'Fees': Debt,})

    def Revenue1():
        fig1 = px.pie(Rev, values='Revenue', names=Rev.index)
        return fig1
    fig1 = Revenue1()
    
    def Gross():
        fig2 = px.pie(Rev, values='Gross Profit', names=Rev.index)
        return fig2
    fig2 = Gross()

    def Music_Ind():
        fig3 = px.pie(Ind, values='Music Industy', names=Ind.index)
        return fig3
    fig3 = Music_Ind()

    def Royalty_Ind():
        fig3 = px.pie(Debt1, values='Fees', names=Debt1.index)
        return fig3
    fig4 = Royalty_Ind()

    
    st.title('Revenue Analysis')
    st.write("""Spotify(SPOT) is a Swedish audio streaming and media service provider that was founded on April 23, 2006 by Daniel Ek and Martin Lorentzon.
             The Company went public in 2018 with its initial stock shares being traded for \$165.90 a share thus requiring Spotify to disclose all financial information.
             Spotify offers its services globally with Spotify being available in 184 countries and territories and has roughly around 602 million monthly active users
              and 236 million Premium Subscribers as of December 31, 2023. It was also reported that in the year 2023 that Spotify made $4.05 billion US dollars""")
    st.subheader('Spotify Revenue Based on 2021')
    st.plotly_chart(fig1)
    st.subheader('Spotify Gross Profit Based on 2021')
    st.plotly_chart(fig2)
    st.write("""Spotify Despite its pure massive amounts of streams and possible ad revenue from said streams, majority of the money made from its platform is generated from its premium monthly or yearly subscriptions.
              Premium Subscribers of spotify are able to enjoy unlimited online and offline access to their entire catalog of music and podcasts without having to listen to any commercials.""")
    st.subheader('Spotify Subscription Cost:')
    st.markdown("""
- Premium Individual: \$10.99 per month.
- Premium Duo: \$14.99 per month. Like the Individual plan, the Duo option provides all the same Premium features, but with the option for two accounts
- Premium Family: \$16.99 per month. The Family plan includes all of the features of the Individual plan but is meant for up to 6 people
- Premium Student: \$5.99 per month. Student plan comes with the same features as the Individual option and can be used for up to four years but need to use a school email.
                """)

    st.write("""Fortunately members of Spotify who do not pay for a premium subscription are able to access Spotify's Ad-Supported Services but
              such users have limited on-demand online access to the company's music catalog and unlimited online access to its catalog of podcasts""")
    st.plotly_chart(fig4)
    st.write("""Spotify however is just a streaming service so it has been paying back nearly 70% of every dollar generated from music as royalties to rights holders who represent artists and songwriters. 
             These organizations, which include independent distributors, publishers, performance rights organizations,
              record labels, and collecting societies, then pay the artists and songwriters based on their agreed terms. These terms to can vary drastically mostly depending on well the artist tends to perform""")
    
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.subheader('Music Streaming Industry')
    st.plotly_chart(fig3)
    st.write(""" The Music streaming makes up 84% of music industry revenue with the streaming industry experience year after year growth with just last year being 10%.
              According to analysis the music streaming global revenue is sitting at 17.5 billion dollars and paid streaming makes up 23% of it. Nearly 4/5 people currently use a 
             streaming service such as spotify to listen to music now and only growing. With over 600 million people actively paying a subscription the market is only to grow and spotify is sure to keep its place is large and growing market """)


if __name__ == "__main__":
    show_page()
