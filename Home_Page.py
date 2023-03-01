import streamlit as st
import pandas as pd
import datetime
import altair as alt
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Home Page",
                page_icon = ":pig_nose:",
                layout="wide",
                initial_sidebar_state='expanded')


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title(":bar_chart: CIMB & F88 Forecasting for March")
st.markdown("##")

cimb = pd.read_excel("EDA/cimb_t3.xlsx")
f88 = pd.read_excel("EDA/f88_t3.xlsx")
    # match = pd.read_parquet("EDA/match.parquet", engine = 'fastparquet')
    # data_loc = pd.read_parquet("EDA/a.parquet",engine = 'fastparquet')
    # data_loc_1 = pd.read_parquet("EDA/c.parquet",engine = 'fastparquet')


# cimb.drop("DU_THU_F88", axis = 1, inplace = True)
# cimb.rename(columns = {'DU_THU_CIMB': 'THUC_THU'}, inplace = True)
cimb.dropna(inplace = True)

fig = go.Figure()
fig.add_trace(go.Scatter(x=cimb['Date'][-31:], y=cimb['THUC_THU'][-31:],
                    mode='lines',
                    name='CIMB'))
fig.add_trace(go.Scatter(x=f88['Date'][-31:], y=f88['THUC_THU'][-31:],
                    mode='lines+markers',
                    name='F88'))
fig.update_layout(
    xaxis_tickformat = '%d %B (%a)'
)
# fig.update_layout(
#       margin=dict(l=0, r=0, t=35, b=0),
# )
fig.update_xaxes(tickangle=90,tickmode='linear')

st.plotly_chart(fig, use_container_width=True)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
