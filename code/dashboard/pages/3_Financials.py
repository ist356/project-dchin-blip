import os
import pandas as pd
import streamlit as st
if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from retrieve_financials import retrieve_fin_stmnts
else:
    from code.retrieve_financials import retrieve_fin_stmnts

TICKER_CACHE = "code/cache/ticker_cache/"
FIN_CACHE = "code/cache/fin_cache/"

st.title("Financials")

# the available tickers are accumulated from the sectors currently in the system; this ensures that they are compatible with the nasdaq website.
total = pd.DataFrame()
for file in os.listdir(TICKER_CACHE):
    df = pd.read_csv(TICKER_CACHE + file)
    total = pd.concat([total, df], ignore_index = True)
ticker_retrieval_selection = st.selectbox("Tickers:", total["Symbol"].to_list())

if st.button("Retrieve Financials"):
    retrieve_fin_stmnts(ticker_retrieval_selection)

available_tickers = []