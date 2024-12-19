import pandas as pd
from playwright.async_api import async_playwright

PRICES_CACHE = "code/cache/prices_cache/"

'''
this function also uses the playwright boiler plate with added asynchronous commands as mentioned in the comments of
1_Home.py; the prices of each stock are conveniently stored in a .csv file for public use by nasdaq.
'''
async def retrieve_prices(ticker):
    async with async_playwright() as playwright:
        browser = await playwright.firefox.launch(headless = True)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(f"https://www.nasdaq.com/market-activity/stocks/{ticker.lower()}/historical")
        await page.get_by_role("button", name = "Max").click()
        async with page.expect_download() as download_info:
            await page.get_by_role("button", name = "Download historical data").click()
        download = await download_info.value
        file_name = f"{ticker}.csv"
        await download.save_as(PRICES_CACHE + file_name.lower())
    
    # the .csv is provided most recent date first, so flip them so the oldest date is first.
    df = pd.read_csv(PRICES_CACHE + file_name.lower())
    df_flipped = df[::-1]
    df_flipped.to_csv(PRICES_CACHE + file_name.lower(), index = False)