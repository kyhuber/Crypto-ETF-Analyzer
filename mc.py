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

def mcstreamlit(initial_investment,ticker_choice,crypto_choice,weight1,weight2,years):
    tickerData = yf.Ticker(ticker_choice)
    tickerDf = tickerData.history(period="id", start="2020-10-18",index_col="Date", parse_dates=["Date"])
    tickerDf.drop(["Dividends","Stock Splits"],axis=1,inplace=True)
    tickerDf.columns = ["open","high","low","close","volume"]
    cryptoData = yf.Ticker(f"{crypto_choice}-USD")
    cryptoDf = cryptoData.history(period="id", start="2020-10-18",index_col="Date", parse_dates=["Date"])
    cryptoDf.drop(["Dividends","Stock Splits"],axis=1,inplace=True)
    cryptoDf.columns = ["open","high","low","close","volume"]
    to_merge_dict = {f"{ticker_choice}": tickerDf , f"{crypto_choice}": cryptoDf}

    df = pd.concat(to_merge_dict.values(), axis=1, keys=to_merge_dict.keys())
    
    MC_df = MCSimulation(
        portfolio_data = df.dropna(),
        weights = [weight1,weight2],
        num_simulation = 500,
        num_trading_days = 252*years)
    
    x = MC_df.calc_cumulative_return()

    output_summary = MC_df.summarize_cumulative_return()
    percent_change = (output_summary["mean"])
    final_investment = initial_investment*percent_change 
    return f"If you invest {initial_investment} dollars in {crypto_choice} and {ticker_choice} with a {weight1}% - {weight2}% allocation, you will have ${final_investment:.2f} in {years} years."