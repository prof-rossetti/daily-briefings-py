# app/stocks_service.py

import os
import json

import requests
from dotenv import load_dotenv

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="abc123")
MY_STOCKS = os.getenv("MY_STOCKS", default="MSFT,GOOG,TSLA")

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"  #> $12,000.71

symbols = MY_STOCKS.split(",") #> ["MSFT", "GOOG", "TSLA"]

for symbol in symbols:
    print("---------------------")
    print("SYMBOL:", symbol)
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
    if "Time Series (Daily)" in parsed_response.keys():
        tsd = parsed_response["Time Series (Daily)"]
        latest_date, latest_prices = list(tsd.items())[0]
        latest_close = latest_prices["4. close"]
        print("LATEST DAY:", latest_date)
        print("LATEST CLOSE:", to_usd(float(latest_close)))
    else:
        print(parsed_response)
