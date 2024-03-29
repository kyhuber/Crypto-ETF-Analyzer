import os
from sqlite3 import Date
import pandas as pd
import requests
import streamlit as st
from dotenv import load_dotenv
from datetime import datetime
from MCForecastTools import MCSimulation
import matplotlib.pyplot as plt
import yfinance as yf
from mc import mcstreamlit

# Set Webpage Name
st.set_page_config(page_title="Crypto ETF Analysis", layout="centered")
st.header('Crypto and Stock Comparison Tool')

# Get initial investment
initial_investment = st.sidebar.number_input(
    "What is your initial investment?",min_value=1,step=100)
initial_investment = int(initial_investment)

#Crypto Define Input
crypto_choice = st.sidebar.selectbox(
    "Which cryptocurrency would you like to compare?",
    ("BTC","ETH","LTC","XRP"))
cryptoData = yf.Ticker(f"{crypto_choice}-USD")
cryptoDf = cryptoData.history(period="id", start="2020-10-18",index_col="Date", parse_dates=["Date"])

weight1 = st.sidebar.number_input(
    "What percent to your crypto investment?",max_value=100,step=1,value=50)
weight1 = int(weight1)

#Ticker Define Input
ticker_choice = st.sidebar.text_input(
    "Which stock would you like to compare? Please enter the stock's ticker.",value="SPY")
tickerData = yf.Ticker(ticker_choice)
tickerDf = tickerData.history(period="id", start="2020-10-18",index_col="Date", parse_dates=["Date"])

#Gather other inputs
weight2 = st.sidebar.number_input(
    "What percent to your stock investment?",max_value=100,step=1,value=50)
weight2 = int(weight2)
years = st.sidebar.number_input(
    "How many years do you want to simulate",step=1)
years = int(years)

st.write(mcstreamlit(initial_investment,ticker_choice,crypto_choice,weight1,weight2,years))

#Crypto Cumulative Returns
cryptoDf["Daily Return"] = cryptoDf.Close.pct_change()
crypto_cumulative_returns = (1 + cryptoDf["Daily Return"]).cumprod()

#Ticker Cumulative Returns
tickerDf["Daily Return"] = tickerDf.Close.pct_change()
ticker_cumulative_returns = (1 + tickerDf["Daily Return"]).cumprod()

#Plot Both Cumulative Returns
st.write(f"{crypto_choice} vs {ticker_choice} Cumulative Returns")
ax = ticker_cumulative_returns.plot()
bx = crypto_cumulative_returns.plot(ax=ax)
Combined_Plot = pd.concat([crypto_cumulative_returns,ticker_cumulative_returns], join="inner", axis=1)
Combined_Plot.columns = [f"{crypto_choice} Returns",f"{ticker_choice} Returns"]
st.line_chart(Combined_Plot)

#Plot Crypto Close
st.write(f"{crypto_choice} Price History")
st.line_chart(cryptoDf.Close)

#Plot Ticker Close
st.write(f"{ticker_choice} Price History")
st.line_chart(tickerDf.Close)