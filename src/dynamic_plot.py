import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from pandas_datareader import data
from pandas_datareader._utils import RemoteDataError

asset = input("Enter the ticker: ")
START_DATE = input("Enter the start date (YYYY_MM_DD): ")
END_DATE = str(datetime.now().strftime('%Y-%m-%d'))


def get_stats(asset):
    return {
        'last': np.mean(asset.tail(1)),
        'short mean': np.mean(asset.tail(50)),
        'short rolling': asset.rolling(window=20).mean(),
        'long rolling': asset.rolling(window=200).mean()
    }

def clean_data(asset, col):
    weekdays = pd.date_range(start=START_DATE, end=END_DATE)
    clean_data = asset[col].reindex(weekdays)
    return clean_data.fillna(method="ffill")

def create_plot(asset, ticker):
    stats = get_stats(asset)
    plt.style.use('seaborn')
    plt.subplots(figsize=(12,8))
    plt.plot(stats['short rolling'], label='20 days rolling mean')
    plt.xlabel('Date')
    plt.ylabel('Adjusted Close Price')
    plt.legend()
    plt.title("Rolling 20 - " + str(ticker))
    plt.tight_layout()
    plt.show()

def get_data(ticker):
    try:
        asset = data.DataReader(ticker,
                                     'yahoo',
                                     START_DATE,
                                     END_DATE)
        adj_close = clean_data(asset, 'Adj Close')
        
        create_plot(adj_close, ticker)
    
    except RemoteDataError:
        print('No data fount for {t}'.format(t=ticker))

get_data(asset)