import asyncio
import os
import pandas as pd
import pickle
import streamlit as st
if __name__ == "__main__":
    import sys
    sys.path.append('code')
    from retrieve_nasdaq_tickers import retrieve_nasdaq_tickers
else:
    from code.retrieve_nasdaq_tickers import retrieve_nasdaq_tickers

SECTORS = ["Technology", "Telecommunications", "Consumer Discretionary", "Consumer Staples", "Energy"] # sectors are form the nasdaq stock screener.
STREAMLIT_CACHE = "code/cache/streamlit_cache/"
TICKER_CACHE = "code/cache/ticker_cache/"

# this function saves the selection to a pickle file so that the session state is saved though multiple streamlit sessions.
def save_sector_selection():
    if sector_selection:
        with open(STREAMLIT_CACHE + "sector_selection", "wb") as file:
            pickle.dump(sorted(sector_selection), file)
        st.success("Sector selection saved.")
    else: # nothing well happen if nothing is selected.
        st.error("Sector selection is empty.")

# this function shows the sectors currently in the system.
def view_sector_selection():
    try:
        with open(STREAMLIT_CACHE + "sector_selection", "rb") as file:
            sector_selection = pickle.load(file)
            st.write("Current Selection:")
            st.write(sector_selection)
    except: # if no sector selection pickle file exists, nothing happens.
        pass
    
st.title("Home")
view_sector_selection()
sector_selection = st.multiselect("Sectors:", SECTORS)
st.button("Save Selection", on_click = save_sector_selection)
if st.button("Retrieve Tickers"):
    
    # as with the other streamlit pages, a special loop and asynchronous setup is required to integrate playwright with streamlit.
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)
    title = loop.run_until_complete(retrieve_nasdaq_tickers())
    print(title)

# all of the tickers of the sectors currently in the system are displayed.
for file in os.listdir(TICKER_CACHE):
    st.write(file)
    st.dataframe(pd.read_csv(TICKER_CACHE + file)[["Symbol", "Name", "Country", "Industry"]])