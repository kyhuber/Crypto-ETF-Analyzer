import os
from sqlite3 import Date
import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from datetime import datetime
from MCForecastTools import MCSimulation
import matplotlib.pyplot as plt
from PIL import Image
from alpaca_trade_api.rest import TimeFrame
import yfinance as yf
import plotly.figure_factory as ff
import plotly.graph_objects as go

# Set Werbpage Name
st.set_page_config(page_title="Crypto ETF Analysis", layout="centered")
st.header('Crypto and Stock Comparison Tool')

# Define Inputs

crypto_choice = st.sidebar.selectbox(
    "Which cryptocurrency would you like to compare?",
    ("BTC-USD","ETH-USD","LTC-USD","XRP-USD"))

st.write(f"{crypto_choice} Price History")

cryptoData = yf.Ticker(crypto_choice)
cryptoDf = cryptoData.history(period="id", start="2020-10-18",end="2021-2-18",index_col="Date", parse_dates=["Date"])

st.line_chart(cryptoDf.Close)

st.write(f"{crypto_choice} Cumulative Returns")

cryptoDf["Daily Return"] = (cryptoDf.Close - cryptoDf.Close.shift(1))/cryptoDf.Close.shift(1)
crypto_cumulative_returns = (1 + cryptoDf["Daily Return"]).cumprod()

st.line_chart(crypto_cumulative_returns)

ticker_choice = st.sidebar.text_input(
    "Which stock would you like to compare?")

tickerData = yf.Ticker(ticker_choice)
tickerDf = tickerData.history(period="id", start="2020-10-18", end="2021-2-18",index_col="Date", parse_dates=["Date"])

st.write(f"{ticker_choice} Price History")

st.line_chart(tickerDf.Close)

tickerDf["Daily Return"] = (tickerDf.Close - tickerDf.Close.shift(1))/tickerDf.Close.shift(1)
ticker_cumulative_returns = (1 + tickerDf["Daily Return"]).cumprod()
st.write(f"{ticker_choice} Cumulative Returns")

st.line_chart(ticker_cumulative_returns)

fig = go.Figure()
fig.add_trace(go.Scatter(x=Date, y=crypto_cumulative_returns,
                    mode="lines",
                    name="lines"))
fig.add_trace(go.Scatter(x=Date, y=ticker_cumulative_returns,
                    mode="lines",
                    name="lines"))

fig.show()

#fig = px.line(x=fruits, y=[1,3,2], color=px.Constant("This year"),
#labels=dict(x="Fruit", y="Amount", color="Time Period"))
#fig.add_bar(x=fruits, y=[2,1,3], name="Last year")
#fig.show()