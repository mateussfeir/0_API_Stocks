
# New chalenge
# 1) Create a code that conect pull earnings data from the Alpha Vantage capital
# 2) Give the user the choice of chosing teh ticker. and the period of earnings requested
# 3) Plot the chart 

# Path shortcut: /Users/mateussfeir/Desktop/Python/GPT\ Project\ stock\ market
# File name: Earnings_chart.py

'''Solution:'''

# 1) Crate a function to push the data from the API (Aplication Programming Interface)

import requests
import matplotlib.pyplot as plt

chosen_stock = input('Which company do you want to get data? ').upper()


period = input('Do you want to see annual or quarterly report? (a/q) ').lower()
if period == 'a' or period == 'annual':
    period = 'annual'
elif period == 'q' or period == 'quarterly':
    period = 'quarterly'

def get_API():
    url = 'https://www.alphavantage.co/query'
    params = {'function': 'INCOME_STATEMENT',
            'symbol': chosen_stock,
            'apikey': 'TE1E1KD330UYLRHQ'}
    response = requests.get(url, params=params)
    return response

# url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=TE1E1KD330UYLRHQ'

# 2) Call the function and convert the data to JSON format

response = get_API()
data = response.json()

# 3) Create a list to storage the date and the net income data.

earnings_list = []

for earnings in data[f'{period}Reports']:

    net_income = float(earnings['netIncome'])
    fiscal_date = earnings['fiscalDateEnding']
    earnings_list.append((fiscal_date, net_income))

# 3.1) Separate the informations in the list 

earnings_list.reverse()
dates = [inf[0] for inf in earnings_list]
net_income = [inf[1] for inf in earnings_list]

dates = dates
net_income = net_income

# 4) Plot the chart

plt.style.use('dark_background')
plt.bar(dates, net_income)
plt.xlabel('Date')
plt.ylabel('Earnings')
plt.title(f"{chosen_stock}'s Net Income")
plt.show()






