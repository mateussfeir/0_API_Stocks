
# New challenge: 

# 1) Upadte the code in way that the user can choose the stock and how many passed days of data.

# Solution:

import requests
import matplotlib.pyplot as plt


# 1) Provide the URL, the parameters, ask the user how long and which stock he wants to analyse.

url = 'https://alphavantage.co/query'

chosen_stock = input('Choose the stock you want to analyse: ').upper()
duration = int(input('How many days of data do you want to see the volume chart? '))

params = {'function' : 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol' : chosen_stock,
        'outputsize' : 'full',
        'apikey' : 'TE1E1KD330UYLRHQ'}

# 2) Pull the data and convert to json format.

response = requests.get(url, params=params)
data = response.json()

# 3) Create 2 lists containing the date and the volume from the period requested.

list_of_days = []

for i in range(duration):

    day = list(data['Time Series (Daily)'].keys())[i]
    list_of_days.append(day)
    i += i + 1

volume_of_the_days = []

for date in list_of_days:

    daily_volume = data['Time Series (Daily)'][date]['6. volume']
    volume_of_the_days.append(float(daily_volume))


# 4) Plot the chart

plt.title(f'{chosen_stock} Volume of the last {duration} days')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.bar(list_of_days, volume_of_the_days)
plt.show()
