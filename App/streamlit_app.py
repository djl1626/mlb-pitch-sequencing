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


df = pd.read_csv("../Data/BrayanBello2023Data.csv")

with st.sidebar.form(key="Filters"):
    st.subheader("Data Filters:")
    balls = st.number_input("Balls", min_value=0, max_value=3, step=1, value=None)
    strikes = st.number_input("Strikes", min_value=0, max_value=2, step=1, value=None)
    st.form_submit_button("Apply")

plotData(df, balls, strikes)
