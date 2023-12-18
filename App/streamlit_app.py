import streamlit as st
import pandas as pd
import plotly.express as px
from Functions import PitcherStatistics
from Functions import StatcastSlicer


def plotData(data, balls, strikes):
    data_filtered = StatcastSlicer.applyFilters(data=data, balls=balls, strikes=strikes)
    fig = px.line_polar(PitcherStatistics.getPitchUsage(data_filtered), r='percentage_pitch_thrown', theta='pitch_type',
                        line_close=True, range_r=[0, 75])
    st.plotly_chart(fig)
    st.dataframe(data_filtered)


@st.cache_data
def loadData():
    df = pd.read_csv("../Data/BrayanBello2023Data.csv")
    names = df.drop_duplicates(['pitcher', 'player_name'])
    names = dict(zip(names['pitcher'], names['player_name']))
    return df, names


df, names = loadData()

with st.sidebar.form(key="Filters"):
    st.subheader("Data Filters:")
    player = st.multiselect("Player", options=pd.unique(df['pitcher']), format_func=lambda pitcher: names[pitcher], default=None)
    balls = st.number_input("Balls", min_value=0, max_value=3, step=1, value=None)
    strikes = st.number_input("Strikes", min_value=0, max_value=2, step=1, value=None)
    st.form_submit_button("Apply")

if len(player) != 0:
    plotData(df, balls, strikes)
