# Hello World Project
# python 3
# خرید و فروش سهام با کتابخانه Alpaca Trading در پایتون
# سپس می‌توانیم کتابخانه Alpaca Trading خود را راه‌اندازی کنیم و خرید و فروش سهام را در زبان پایتون بدین صورت طراحی کنیم.
# در این مثال استراتژی ما این است که زمانی که میانگین متحرک ۵ دقیقه از قیمت ما عبور کرد، خرید و فروش کنیم.


from distutils.util import change_root
from email.mime import base
import secrets
from symtable import Symbol
from time import time
from tkinter import SEL_LAST
from matplotlib.pyplot import spy

from numpy import busday_count
from yaml import Mark
import alpaca_trade_api as tradeapi

SEC_KEY = "" # Enter Your Secret Key Here
PUB_KEY = "" # Enter Your Public Key Her
BASE_URL = 'https://paper-api.alpaca.markets' # This is the base URL for paper trading
api = tradeapi.REST(key_id=PUB_KEY,secret_key=SEC_KEY,base_uri=BASE_URL)# FOr real trading,don't enter a base-url

# Buy a stock
api.submit_order(
    Symbol='SPY'; # Replace with the ticker of the stock you want to buy
    ,qty=1
    ,side='buy'
    ,type='Market'
    ,time_in_force='gtc'# Good 'till cancelled
)

# Sell a stock (just change side to 'sell')
api.submit_order(
    symbol='spy'
    ,qty=1
    ,side='sell'
    ,type='market
    ,time_in_force='gtc'
 )