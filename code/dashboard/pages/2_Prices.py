import asyncio
import matplotlib.pyplot as plt
import os
import pandas as pd
import seaborn as sns
import streamlit as st
if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from retrieve_prices import retrieve_prices
else:
    from code.retrieve_prices import retrieve_prices

PRICES_CACHE = "code/cache/prices_cache/"
TICKER_CACHE = "code/cache/ticker_cache/"
MAXIMUM = 30 # this number is arbitrary but small enough to fit within the plot.

def clean_price(price): # function taken from assignment seven.
    return float(price.replace("$", "").replace(",", ""))

# this function displays the charts associated with the stock prices.
def display():

    if ticker_display_selection:
        c1, c2 = st.columns(2)
        df = pd.read_csv(PRICES_CACHE + available_tickers_dict[ticker_display_selection])

        # since these are initially strings, they have to be converted in order to work with seaborn correctly.
        df["date_datetime"] = pd.to_datetime(df["Date"], format="%m/%d/%Y")
        df["close_price_formatted"] = df["Close/Last"].apply(clean_price)

        # section off a portion of the data; displaying the entire dataset causes the plot to double up on itself as it is too small.
        data = df.tail(num_days)
        
        # column one shows a line plot to help visualize the time-series.
        with c1:
            fig1, ax1 = plt.subplots()
            ax1.tick_params(axis = "x", labelrotation = 90, labelsize = 5)
            sns.lineplot(data = data, x = "Date", y = "close_price_formatted", errorbar = None, ax = ax1)
            st.pyplot(fig1)
        
        # column two shows a box plot to help determine a good buy/sell price.
        with c2:
            fig2, _ = plt.subplots()
            sns.boxplot(data = data,y = "close_price_formatted")
            st.pyplot(fig2)

st.title("Prices")

# the available tickers are accumulated from the sectors currently in the system; this ensures that they are compatible with the nasdaq website.
total = pd.DataFrame()
for file in os.listdir(TICKER_CACHE):
    df = pd.read_csv(TICKER_CACHE + file)
    total = pd.concat([total, df], ignore_index = True)
ticker_retrieval_selection = st.selectbox("Tickers:", total["Symbol"].to_list())

# the prices are scraped asynchronously from the nasdaq website.
if st.button("Retrieve Prices"):
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)
    title = loop.run_until_complete(retrieve_prices(ticker_retrieval_selection))
    print(title)

available_tickers = []
available_tickers_dict = {} # a dictionary is created to make finding the file based on the ticker easier.
for file in os.listdir(PRICES_CACHE):
    available_tickers.append(file.split(".")[0].upper())
    available_tickers_dict[file.split(".")[0].upper()] = file
st.write("Downloaded Ticker Prices:", available_tickers)
ticker_display_selection = st.selectbox("Select a ticker to display:", available_tickers)
num_days = st.select_slider("Select how many days to display:", options = range(MAXIMUM + 1), value = MAXIMUM - 1)
st.button("Display", on_click = display)

