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

#Crypto Define Input
crypto_choice = st.sidebar.selectbox(
    "Which cryptocurrency would you like to compare?",
    ("BTC-USD","ETH-USD","LTC-USD","XRP-USD"))
cryptoData = yf.Ticker(crypto_choice)
cryptoDf = cryptoData.history(period="id", start="2020-10-18",index_col="Date", parse_dates=["Date"])

#Crypto Cumulative Returns
cryptoDf["Daily Return"] = cryptoDf.Close.pct_change()
crypto_cumulative_returns = (1 + cryptoDf["Daily Return"]).cumprod()

#Ticker Define Input
ticker_choice = st.sidebar.text_input(
    "Which stock would you like to compare?")
tickerData = yf.Ticker(ticker_choice)
tickerDf = tickerData.history(period="id", start="2020-10-18",index_col="Date", parse_dates=["Date"])

#Ticker Cumulative Returns
tickerDf["Daily Return"] = tickerDf.Close.pct_change()
ticker_cumulative_returns = (1 + tickerDf["Daily Return"]).cumprod()

#Gather other inputs
initial_investment = st.sidebar.number_input(
    "What is your initial investment?")
weight1 = st.sidebar.number_input(
    "What percent to your crypto investment?")
weight2 = st.sidebar.number_input(
    "What percent to your stock investment?")
years = st.sidebar.number_input(
    "How many years do you want to simulate")

st.write(mcstreamlit(initial_investment,ticker_choice,crypto_choice,weight1,weight2,years))

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