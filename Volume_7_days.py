
# New challenge: 

# 1) Create a code to pull data (Volume from the last 7 days) from an API (Application Programming Interface)
# 2) Plot the chart 

# Solution:

import requests
import matplotlib.pyplot as plt


# 1) Provide the URL and the parameters.

url = 'https://alphavantage.co/query'

params = {'function' : 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol' : 'TSLA',
        'outputsize' : 'full',
        'apikey' : 'TE1E1KD330UYLRHQ'}

# 2) Pull the data and convert to json format.

response = requests.get(url, params=params)
data = response.json()

# 3) Create 2 lists containing the date and the volume from the last 7 days.

list_7_days = []

for i in range(7):

    day = list(data['Time Series (Daily)'].keys())[i]
    list_7_days.append(day)
    i += i + 1

volume_7_days = []

for date in list_7_days:

    daily_volume = data['Time Series (Daily)'][date]['6. volume']
    volume_7_days.append(float(daily_volume))

# print(type(list_7_days))
# print(type(volume_7_days))

# 4) Plot the chart

plt.title('TSLA Volume of the last 7 days')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.bar(list_7_days, volume_7_days)
plt.show()
