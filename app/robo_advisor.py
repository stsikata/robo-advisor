# this is the "app/robo_advisor.py" file

import requests
import json

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#
# INFORMATION INPUTS
#

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"
#lets us get a specific URL
response = requests.get(request_url)
# print(type(response))
# print(response.status_code) # the part of http response that lets us know how successful
# print(response.text) # actual body of the response

parsed_response = json.loads(response.text) # to parse the response string into a dictionary

last_refreshed = parsed_response["Meta Data"]["3. Last Refreshed"]
last_close = parsed_response["Time Series (Daily)"]["2021-08-03"]["4. close"]

#symbol = input("Please enter a ticker symbol:")

#breakpoint()


 
print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print(f"LATEST DAY: {last_refreshed}")
print(f"LATEST CLOSE: {to_usd(float(last_close))}")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


## The system should prompt the user to input one stock or cryptocurrency symbol (e.g. "MSFT", "AAPL", etc.).
##It may optionally allow the user to specify multiple symbols, either one-by-one or all at the same time (e.g. "MSFT, AAPL, GOOG, AMZN").
##It may also optionally prompt the user to specify additional inputs such as risk tolerance and/or other trading preferences, as desired and applicable.