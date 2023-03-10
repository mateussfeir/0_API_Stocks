import requests

# Short cut pathway: python news_sentiment.py

user_input = input('Choose the company you want to know how the news are affecting the sentiment of market: ')
url = 'https://www.alphavantage.co/query'
params = {'function' : 'NEWS_SENTIMENT',
        #   'topics' : 'technology',
           'tickers' : user_input,
          'apikey' : 'TE1E1KD330UYLRHQ'
            }

response = requests.get(url, params=params)
data = response.json()
# print(data)

for i in data:
    feed = data['feed']
    for j in feed:
        news = j
        print('\n')
        for k, v in news.items():
            print(k + ':', v)
    
