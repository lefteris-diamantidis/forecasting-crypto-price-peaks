import streamlit as st
import pandas as pd

st.title("Forecasting TUNH App")
st.info("This is an app that Forecasts Cryptos TUNH")

with st.expander("Data"):
  st.write("BTC Data")
  df_btc = pd.read_csv("https://raw.githubusercontent.com/lefteris-diamantidis/forecasting-crypto-price-peaks/refs/heads/main/data/final_data_btc.csv")
  df_btc
  
  st.write("PAXG Data")
  df_paxg = pd.read_csv("https://raw.githubusercontent.com/lefteris-diamantidis/forecasting-crypto-price-peaks/refs/heads/main/data/final_data_paxg.csv")
  df_paxg
  
  st.write("ETH Data")
  df_eth = pd.read_csv("https://raw.githubusercontent.com/lefteris-diamantidis/forecasting-crypto-price-peaks/refs/heads/main/data/final_data_eth.csv")
  df_eth
  
  st.write("BNB Data")
  df_bnb = pd.read_csv("https://raw.githubusercontent.com/lefteris-diamantidis/forecasting-crypto-price-peaks/refs/heads/main/data/final_data_bnb.csv")
  df_bnb
