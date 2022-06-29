# Hello World Project
# python3
# خواندن اطلاعات بازاربا Alpaca API در پایتون
# حال به نحوه خواندن داده‌های بازار با استفاده از Alpaca API در پایتون می‌پردازیم:

from matplotlib.pyplot import spy
import alpaca_trade_api as tradeapi
import numpy as np
import time

SEC_KEY ='bcO995J1nB2W7iWbzIkXv4foX0GKaQJAYT8pX1fN'
BASE_URL = 'https://paper-api.alpaca.markets'
api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL)

symb ="spy"
symb ="spy"

print("")
print("Checking price")

market_data= api.get_barset(symb,'minute',limit=5) #  Get one bar object for each of the past 5 minutes

close_list =[] # This array will store all the closing prices from the last 5 minutes
for bar in market_data[symb]:

    close_list.append(bar.c) #  bar.c is the closing price of that bar’s time interval

    close_list = np.array(close_list,dtype=np.float64) #  Convert to numpy array
    ma = np.mean(close_list)
    last_price = close_list[4] # Most recent closing price

    print("Moving Average:"+str(ma))
    print ("Last Price"+ str(last_price))
    
    time.sleep(60)#  Wait one minute before retreiving more market data

    # اگر به دنبال اطلاعات عمیق‌تر برای ساختن استراتژی خود هستید، اسناد Alpaca را از آدرس زیر بررسی کنید:
    # https://alpaca.markets/docs/api-documentation/api-v2/market-data/alpaca-data-api-v2/
    

