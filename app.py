import os
import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv
import alpaca_trade_api as tradeapi
from datetime import datetime
from dateutil.relativedelta import relativedelta
from MCForecastTools import MCSimulation
from PIL import Image
from alpaca_trade_api.rest import TimeFrame
import yfinance as yf

# Set Werbpage Name
st.set_page_config(page_title="Crypto ETF Analysis")

st.markdown('---')

# Define Inputs

cryptochoice = st.sidebar.selectbox(
    "Which cryptocurrency would you like to compare?",
    ("BTC","ETH","LTC","XRP"))

st.write("You selected:", cryptochoice)

#tickerSymbol = st.sidebar.text_input(
 #   "Which ticker would you like to compare?")

tickerSymbol = "BITW"
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period="id", start="2020-10-18", end="2021-2-18")

st.line_chart(tickerDF.Close)

