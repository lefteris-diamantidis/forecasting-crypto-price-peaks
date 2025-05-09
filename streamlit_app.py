import streamlit as st
import pandas as pd

st.title("Forecasting TUNH App")
st.info("This is an app that Forecasts Cryptos TUNH")

with st.expander("Data"):
  st.write("Raw Data")
  df_btc = pd.read_csv("final_data_btc.csv")
  df.head()
