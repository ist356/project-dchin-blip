import os
import asyncio
from code.retrieve_prices import retrieve_prices
from code.retrieve_financials import retrieve_fin_stmnts

def test_should_pass():
    print("\nAlways True!")
    assert True

tickers = ["AAPL", "CVS", "MU", "NVDA", "WBA"]

def test_prices():
    for ticker in tickers:
        asyncio.run(retrieve_prices(ticker))
        assert os.path.exists(f"code/cache/prices_cache/{ticker.lower()}.csv")

def test_fins():
    for ticker in tickers:
        retrieve_fin_stmnts(ticker)
        assert os.path.exists(f"code/cache/fin_cache/{ticker.lower()}.csv")