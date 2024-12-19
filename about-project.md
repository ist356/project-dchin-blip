# About My Project

Student Name:  Dexter Chin
Student Email:  dpchin@syr.edu

### What it does
During the summer, I got interested in investing in the stock market. Over the semester, prior to the project, I used some of the things taught in class to make a program that used the yfinance library and Pandas. It's primary purpose was to keep track of daily stock close prices. This project is an upgrade/extension of that first program that uses the things I learned from making and running it. Like the first program, I make heavy use of the Nasdaq website as it includes information from the other major stock exchanges (NYSE, AMEX, Global Markets) and make data easy available through downloadable .csv files.

Page 1, or the home page is primarily concerned with scraping the available tickers from the Nasdaq website. I've made use of the website's filter option to divide the tickers by sector as I personally only look at one or two. The user selects the sectors they want the stocks of and they have to save it. I chose not to save and retrieve in one go to create an extra barrier of safety. The Retrieve Tickers button then uses retrieve_nasdaq_tickers.py to retrieve the tickeres and store them in the cache folder. When it does so, the cache is overwritten; I did this because I found that the tickers and stocks available change frequently (the first program had a static ticker database and would run into errors weekly when some were removed). As such, it was better to just overwrite everything and not have to worry about old tickers remaining.

Page 2, Prices, is the exciting part and gets the closing prices of stocks. From the ticker collections downloaded with Page 1, a list is created that shows all of the tickers compatible with the Nasdaq website. I can then go to the history page of each ticker and scrape a log of all of the prices with retrieve_prices.py. The information of each stock has to be downloaded individually because I only need a few of them; just like how I'm only interested in a few sectors, I'm only interested in a few stocks. Once the price information has been downloaded, it can be displayed as a chart. I chose the line and box plots as they are the most useful to me. Like any investing tool, having a time-series of price information is important for knowing the general direction of a stock. The box plot is important for knowing where the prices are concentrated which is helpful for knowing when to buy/sell. There is also a slider to control how many days in the past the plots should show.

Page 3, Financials, appears very similar in structure to Page 2. Instead of web scraping, the financial statements of each ticker are obtained with the Polygon.io API, a specialized API for stocks. I had to sign up and get a key. All of the API calls involve get requests and the results are returned as dictionaries of dictionaries in the .json format. Each financial statement is parsed to get the important parts (to me) like the timeframe, revenue, and profit. For the most accuracy, the quarterly reports are used. Like everything else, the information is stored in the cache with each ticker getting its own dedicated file.

### How you run my project
1_Home.py should be run through Streamlit. It connects to every other page through a sidebar on the left and each page is connected to all of the necessary functions and external files.

### Other things you need to know
I made heavy use of ChatGPT and forums to solve errors and any other problems I had. For ChatGPT, some of the questions I asked were:
- Error readouts.
- Clarifications like how to make a comment block in VSC, the naming convention for test files to be recognized by pytest, or how exactly to use apply() to apply a function to all values in a dataframe column.
- How to do small things and things that were specific to my scenario like decrease the text size of a Seaborn plot or if it was possible to have pylot plot underneath everything else on a streamlit page.

Because of the limit on the free version of Polygon.io, the tests may fail if ran too quickly.