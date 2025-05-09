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

  st.write("AAVE Data")
  df_aave = pd.read_csv("https://raw.githubusercontent.com/lefteris-diamantidis/forecasting-crypto-price-peaks/refs/heads/main/data/final_data_aave.csv")
  df_aave

  st.write("SOL Data")
  df_sol = pd.read_csv("https://raw.githubusercontent.com/lefteris-diamantidis/forecasting-crypto-price-peaks/refs/heads/main/data/final_data_sol.csv")
  df_sol

  st.write("LTC Data")
  df_ltc = pd.read_csv("https://raw.githubusercontent.com/lefteris-diamantidis/forecasting-crypto-price-peaks/refs/heads/main/data/final_data_ltc.csv")
  df_ltc 
  
  st.write("XRP Data")
  df_xrp = pd.read_csv("https://raw.githubusercontent.com/lefteris-diamantidis/forecasting-crypto-price-peaks/refs/heads/main/data/final_data_xrp.csv")
  df_xrp

  st.write("ADA Data")
  df_ada = pd.read_csv("https://raw.githubusercontent.com/lefteris-diamantidis/forecasting-crypto-price-peaks/refs/heads/main/data/final_data_ada.csv")
  df_ada

with st.expander('Data visualization'):
  st.scatter_chart(data=df_btc, x='Date', y='tunh', color='species')
