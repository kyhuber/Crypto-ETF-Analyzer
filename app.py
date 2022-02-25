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

# Set Werbpage Name
st.set_page_config(page_title="Crypto ETF Analysis")

st.markdown('---')

# Define Inputs

cryptochoice = st.selectbox(
    "Which cryptocurrency would you like to compare?",
    ("BTC","ETH","LTC","XRP"))

st.write("You selected:", cryptochoice)

ticker = st.text_input(
    "Which ticker would you like to compare?")

Alpha_API_Key = os.getenv("Alpha_API_Key")
twenty_years_history = pd.read_csv(f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={ticker}&apikey={Alpha_API_Key}&datatype=csv')

twenty_years_history.plot()

