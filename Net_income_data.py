
# New chalenge
# 1) Create a code that conect pull earnings data from the Alpha Vantage capital
# 2) Give the user the choice of chosing teh ticker. and the period of earnings requested
# 3) Plot the chart 

# Path shortcut: /Users/mateussfeir/Desktop/Python/GPT\ Project\ stock\ market
# File name: Earnings_chart.py

'''Solution:'''

# 1) Crate a function to push the data from the API (Aplication Programming Interface)

import requests

def get_API():
    url = 'https://www.alphavantage.co/query'
    params = {'function': 'INCOME_STATEMENT',
            'symbol': 'TSLA',
            'apikey': 'TE1E1KD330UYLRHQ'}
    response = requests.get(url, params=params)
    return response

# url = 'https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol=IBM&apikey=TE1E1KD330UYLRHQ'

# 2) Call the function and convert the data to JSON format

response = get_API()
data = response.json()

# 3) Create a list to acumulate just the net income informations

earnings_list = []

for earnings in data['quarterlyReports']:

    net_income = float(earnings['netIncome'])
    fiscal_date = earnings['fiscalDateEnding']
    earnings_list.append((fiscal_date, net_income))

print(earnings_list)

