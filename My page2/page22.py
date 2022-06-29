# Hello World Project
# python3
# اجرای استراتژی معاملاتی با alpaca trade api در پایتون
# برای الگوریتم معاملاتی کامل خود همه موارد را کنار هم قرار می‌دهیم:
# واین هم ربات معاملاتی که بازبان پایتون نوشته شده

from email.mime import base
from fileinput import close
import secrets
from symtable import Symbol
from matplotlib.markers import MarkerStyle

from numpy import busday_count
import alpaca_trade_api as tradeapi


SEC_KEY = "" # Enter Your Secret Key Here
PUB_KEY = "" # Enter Your Public Key Her
BASE_URL = "https://paper-api.alpaca.markets" #  This is the base URL for paper trading

api = tradeapi.REST(key_id= PUB_KEY,secret_Key=SEC_KEY,base_url=BASE_URL) # For real trading, don’t enter a base_url


# Buy a stock
api.submit_order(
    Symbol='SPY' # Replace with the ticker of the stock you want to buy'
    ,qty=1
    ,side='buy'
    ,type='market'
    ,time_in_force='gtc' # Good ’til cancelled
    )


#  Sell a stock(Just change side to ‘sell’)
api.submit_order(
    symbol='SPY'  
     ,qty=1
     ,side='sell'
     ,type='Market'
     ,time_in_force='gtc'
    )    

import alpaca_trade_api as tradeapi
import numpy as np
import time

SEC_KEY= "bcO995J1nB2W7iWbzIkXv4foX0GKaQJAYT8pX1fN"
PUB_KEY= "PKRQE96HW8BM6TO9V13V"
BASE_URL= "https://paper-api.alpaca.markets"

api = tradeapi.REST(Key_id=PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL)

symb= "SPY"

symb= "SPY"

print("")
print("Checking Price")

market_data=api.get_barset(symb, 'minute', limit=5) # Get one bar object for each of the past 5 minutes
close_list = [] # This array will store all the closing prices from the last 5 minutes
for bar in market_data[symb]:

    close_list.append(bar.c) # bar.c is the closing price of that bar’s time interval
    close_list=np.array(close_list,dtype=np.float64) #  Convert to numpy array
    ma = np.mean(close_list)
    last_price= close_list[4] # Most recent closing price


print("Moving Average:"+ str(ma))
print("Last Price:"+ str(last_price))


time.sleep(60) #  Wait one minute before retreiving more market data

# چنانچه بخواهیم آن را به صورت روزانه روی Codesphere اجرا کنیم، باید
# روزانه به‌روزرسانی داشبورد Alpaca خود را ببینیم:
