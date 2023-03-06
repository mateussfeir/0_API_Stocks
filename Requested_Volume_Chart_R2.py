import requests
import matplotlib.pyplot as plt

# Getting the inputs from the user

chosen_stock = input('Choose the stock you want to analyse: ').upper()
duration = int(input('How many days of data do you want to see the volume chart? '))

# Defining the function to plot the chart 

def plot_chart(dates, volume):
    plt.style.use('dark_background')
    plt.title(f"{chosen_stock}'s stock volume of negociation of the last {duration} trading days")
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.bar(dates, volume)
    plt.show()

# Defining the function to conect the API and return the data

def API_get_stock_data(chosen_stock):
    url = 'https://alphavantage.co/query'
    params = {'function' : 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol' : chosen_stock,
        'outputsize' : 'full',
        'apikey' : 'TE1E1KD330UYLRHQ'}
    response = requests.get(url, params=params)
    return response

# Calling the API function and passing the parameter

response = API_get_stock_data(chosen_stock)

# Converting the data to JSON format

data = response.json()

# Defining an If statement to give a user feedback if the chosen ticker is not available.

if 'Error Message' in data:

    print('Sorry, this ticker does not exists or we do not have in our database')

else:

# Creating a variable list to storage the dates variating in function of the user choice

    list_of_days = []

# Bulding a loop to fill our list with the data in the chosen duration.

    for i in range(duration):

        day = list(data['Time Series (Daily)'].keys())[i]
        list_of_days.append(day)
        i += i + 1

    volume_of_the_days = []

# Running another loop to push the volume data from the specific dates

    for date in list_of_days:

        daily_volume = data['Time Series (Daily)'][date]['6. volume']
        volume_of_the_days.append(float(daily_volume))

# Calling the plot chart function

    plot_chart(list_of_days, volume_of_the_days)


