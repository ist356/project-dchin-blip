import os
import pickle
import shutil
from playwright.async_api import async_playwright

STREAMLIT_CACHE = "code/cache/streamlit_cache/"
TICKER_CACHE = "code/cache/ticker_cache/"

'''
this function uses the playwright boiler plate with added asynchronous commands as mentioned in the comments of
1_Home.py; the sectors have to be scraped because the tickers supported by nasdaq change and are delisted/added frequently.
'''
async def retrieve_nasdaq_tickers():
    async with async_playwright() as playwright:
        try:
            with open(STREAMLIT_CACHE + "sector_selection", "rb") as file:
                sector_selection = pickle.load(file)
                if os.path.exists(TICKER_CACHE):
                    shutil.rmtree(TICKER_CACHE)
                browser = await playwright.firefox.launch(headless = True)
                context = await browser.new_context()
                page = await context.new_page()
                for sector in sector_selection:
                    await page.goto("https://www.nasdaq.com/market-activity/stocks/screener")
                    await page.get_by_label(sector, exact = True).check()
                    await page.get_by_role("button", name = "Apply").click()
                    async with page.expect_download() as download_info:
                        await page.get_by_role("button", name = "Download CSV").click()
                    download = await download_info.value
                    file_name = f"{sector}.csv"
                    await download.save_as(TICKER_CACHE + file_name.lower().replace(" ", "_"))
            
                # ---------------------
                await context.close()
                await browser.close()
        except:
            pass
