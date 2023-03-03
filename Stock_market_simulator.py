'''Create a investment return simulator.

1) Get data from the user such as: ticker, date of investment and amount invested.

2) Calculate how much it would be worth if the user had held untill today.

3) Output the loss/profit in value and in percentage.

'''
import requests
import pandas as pd

def calculate_purchase_power (investment, stock_value):
    amount_of_shares = (investment/stock_value)
    return amount_of_shares


def get_data():
    chosen_ticker = input('Which company do you want to simulate the investment? ').upper()
    investment_input = float(input('How much did you invest (USD)? '))
    date_input = str(input('When did you invest? (yyyy-mm-dd) '))

    # 1) Specify API endpoint and parameters
    url = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': chosen_ticker,
        'outputsize': 'full',
        'apikey': 'TE1E1KD330UYLRHQ'
    }

    # 2) Make API request and retrieve data
    response = requests.get(url, params=params)
    data = response.json()

    # 3) Convert data to Pandas DataFrame
    df = pd.DataFrame.from_dict(data['Time Series (Daily)'], orient='index')
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)

    # 4) Get the stock price for a specific date
    old_price = df.loc[date_input]['5. adjusted close']
    # print(updated_date)
    new_price = df.iloc[0]['4. close']
    print(f'\nThe price of {chosen_ticker} at {date_input} was {old_price:.2f} USD per share.')
    amount_of_shares = calculate_purchase_power(investment_input, old_price)
    print(f'Investing {investment_input}$ you would buy {amount_of_shares:.2f} shares of {chosen_ticker}.')
    print(f'The current price of {chosen_ticker} is {new_price}USD per share.')
    new_value = amount_of_shares*new_price
    print(f'If you had held until today. It would be worth {new_value:.2f} USD now.')
    usd_profit_loss = new_value - investment_input
    percentage_profit_loss = (usd_profit_loss/investment_input)*100
    if usd_profit_loss > 0:
        print(f'It represents a profit of {usd_profit_loss:.2f} USD or {percentage_profit_loss:.2f}%.')
    else:
        print(f'It represents a loss of {usd_profit_loss:.2f} USD or {percentage_profit_loss:.2f}%.')
    # Short cut to open this project on terminal: cd /Users/mateussfeir/Desktop/Phyton/GPT\ Project\ stock\ market/

running = True

get_data()


while running:

    run_again = input('Would you like to simulate again?\n(y/n)').lower()
    if run_again == 'y':
        get_data()
    elif run_again =='n':
        running = False
        print('User quit.')
        break
    else:
        print('Choose one of the options: (y/n)')
