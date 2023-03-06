import requests

# 1) Provide the link from where you want to conect the API (Application programming interface)

url = 'https://www.alphavantage.co/query'

# 2) Create a dictionary and define the parameters (function, symbol, outputsize and API key)

# Obs: The TIME_SERIES_DAILY_ADJUSTED function returns daily historical time series of adjusted
# price data for the stock, which includes the open, high, low, close, and volume data.

params = {'function' : 'TIME_SERIES_DAILY_ADJUSTED',
         'symbol' : 'TSLA',
         'outputsize' : 'full',
        'apikey' : 'TE1E1KD330UYLRHQ'
}

# 3) Make the API requested and convert the data to json format.

response = requests.get(url, params=params)
data = response.json()

# Obs: Now the data is organized in this format:

'''
2010-09-18... 2010-09-17': {'1. open': '21.02', '2. high': '21.32', '3. low': '19.8', '4. close': '20.23',
# '5. adjusted close': '1.34866666666667', '6. volume': '1198500', '7. dividend amount': '0.0000',
# '8. split coefficient': '1.0'}, 2010-09-16...
'''
# 4) Call the function to get the volume data

latest_date = list(data['Time Series (Daily)'].keys())[0]

# Obs: to get the information wanted, select the list (Time Series (Daily), choose the date and the especific inf)

daily_volume = data['Time Series (Daily)'][latest_date]['6. volume']

print(f'{daily_volume}$')
