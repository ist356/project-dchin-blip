import json
import pandas as pd
import requests
with open("code/meta.json", "r") as file:
    key = json.load(file).get("KEY")

FIN_CACHE = "code/cache/fin_cache/"

# this function checks to make sure the ticker is compatible with polygon.io as polygon.io mostly tracks US-based markets.
def check_ticker(ticker):
    url = "https://api.polygon.io/v3/reference/tickers"
    params = {
        "ticker" : ticker,
        "apiKey" : key,
    }
    response = requests.get(url, params = params).json()
    return True if len(response["results"]) > 0 else False # true means the ticker is recognized by polygon.io.

# this function calls the polygon.io api to request all stored financial statements.
def request_fin_stmnts(ticker):
    url = "https://api.polygon.io/vX/reference/financials"
    params = {
        "ticker" : ticker,
        "limit" : 100,
        "timeframe" : "quarterly",
        "order" : "asc",
        "apiKey" : key,
    }
    response = requests.get(url, params = params).json()
    if "next_url" in response.keys(): # regardless of the limit, polygon.io has a maximum page size and will spread the json response over multiple pages if needed; while theoretically possible, no single company currently requires more than one page (at limit = 100) to display all of its quarterly financial statements.
        raise Exception("Response returned more than one page.")
    return response["results"]

# this function writes the information from each financial statement to the ticker's dedicated .csv file.
def write_fin_stmnts_csv(ticker, period, oldest_date, newest_date, shares, profits, revenues, append):
    
    # import streamlit as st
    # st.write(profits)
    # st.write(shares)

    eps = [0] if shares == 0 else [profits / shares]
    sps = [0] if shares == 0 else [revenues / shares]
    
    fin_stmnts_values = {
        "ticker" : [ticker],
        "period" : [period],
        "oldest_date" : [oldest_date],
        "newest_date" : [newest_date],
        "shares" : [shares],
        "eps" : eps,
        "sps" : sps,
    }
    fin_stmnts_values_df = pd.DataFrame(fin_stmnts_values)
    fin_stmnts_ticker_path = FIN_CACHE + f"{ticker}.csv".lower()
    if append:
        fin_stmnts_values_df.to_csv(fin_stmnts_ticker_path, mode = "a", header = False, index = False)
    else:
        fin_stmnts_values_df.to_csv(fin_stmnts_ticker_path, index = False)

def retrieve_fin_stmnts(ticker):

    # first, emsure the ticker is recognzied by polygon.io.
    if check_ticker(ticker):
        
        # request all available financial statements.
        response = request_fin_stmnts(ticker)

        # store the information from each financial statement.
        first_period = True
        for period in response:
            shares = 0
            try:
                shares = period["financials"]["income_statement"]["basic_average_shares"]["value"]
            except:
                pass

            if first_period:
                write_fin_stmnts_csv(ticker, 
                                    period["fiscal_period"] + " " + period["fiscal_year"],
                                    period["start_date"],
                                    period["end_date"],
                                    shares,
                                    period["financials"]["income_statement"]["net_income_loss_available_to_common_stockholders_basic"]["value"],
                                    period["financials"]["income_statement"]["revenues"]["value"],
                                    append = False
                                    )
                first_period = False
            else:
                write_fin_stmnts_csv(ticker, 
                                    period["fiscal_period"] + " " + period["fiscal_year"],
                                    period["start_date"],
                                    period["end_date"],
                                    shares,
                                    period["financials"]["income_statement"]["net_income_loss_available_to_common_stockholders_basic"]["value"],
                                    period["financials"]["income_statement"]["revenues"]["value"],
                                    append = True
                                    )
    else:
        raise Exception("Ticker not recognized by Polygon.io.")