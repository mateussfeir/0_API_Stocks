import requests

# Shortcut pathway: python winning_portfolios.py
url = 'https://www.alphavantage.co/query'
params = {
    'function' : 'TOURNAMENT_PORTFOLIO',
    'season' : '2021-09',
    'apikey' : 'TE1E1KD330UYLRHQ'
}

response = requests.get(url, params=params)
data = response.json()
# print(data)

# data sample: 2022-04', 'ranking': [{'rank': '1', 'portfolio': [{'symbol': 'BRQS', 'shares': '1'}],
#  'measurement_start': '2022-04-15', 'start_value_usd': '0.21', 'measurement_end': '2022-04-29',
#  'end_value_usd': '0.34', 'percent_gain': '61.90476'}, {'rank': '2', 'portfolio': [{'symbol': 'UVIX', 'shares': '1'}],
#  'measurement_start': '2022-04-15', 'start_value_usd': '16.13', 'measurement_end': '2022-04-29', 'end_value_usd': '24.37',
#  'percent_gain': '51.08493'},

''' I'll try to print the top 10 portfolios showing the rank position, % earned and stock held.'''

# Remember that we are using a dictionary data format (JSON) so we have keys and values:
# {'rank': '2', 'portfolio': [{'symbol': 'HOG', 'shares': '1'}, {'symbol': 'BBBY', 'shares': '1'} {...} 'measurement_end': '2021-09-24', 'end_value_usd': '150.94', 'percent_gain': '4.87042'}

for i in range(10):
    rank = data['ranking'][i]
    print('\nRank', rank['rank'] +':\n')
    percentage = float(rank['percent_gain'])
    print('Percentage: {:.2f}%'.format(percentage))
        
    for symbol_shares in rank['portfolio']:
        print('Stock:', symbol_shares['symbol'],', Shares:', symbol_shares['shares'])
