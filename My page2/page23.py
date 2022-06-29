# Hello World Project
# python3
# بک تست یک استراتژی در پایتون با API
# اگر علاقه‌ای به این ندارید که منتظر بمانید تا عملکرد صحیح الگوریتم خود را ببینید،
# می‌توانید از API داده‌های بازار Alpaca برای بک تست
# لگوریتم پایتون خود در برابر داده‌های قدیمی استفاده کنید:


from matplotlib.pyplot import spy
import alpaca_trade_api as tradeapi
import numpy as np
import time	


SEC_KEY = ""  # Enter Your Secret Key Here
PUB_KEY = "" # Enter Your Public Key Her
ASE_URL='https://paper-api.alpaca.markets'
api = tradeapi.REST(key_id= PUB_KEY, secret_key=SEC_KEY, base_url=BASE_URL)

symb="spy"
pos_held= False
hours_to_test = 2
print("Checking price")
market_data = api.get_barset(symb, 'minute', limit=(60 * hours_to_test)) # Pull market data from the past 60x minutes

close_list=[]
for bar in market_data[symb]:

    close_list.append(bar.c)



print("open: " + str(close_list[0]))
print("Close: " + str(close_list[60 * hours_to_test-1]))


   close_list = np.array(close_list,dtype=np.float64)
   starBal = 2000 # Start out with 2000 dollars
   balance = starBal
   buys = 0
   sells = 0



   for i in range(4,60 * hours_to_test): # Start four minutes in, so that MA can be calculated
       ma = np.mean(close_list[i-4:i+1])
       last_price = close_list[i]


print("Moving Average:" + str(ma))
print("Last price:" + str (last_price))

     if ma + 0.1 < last_price and not pos_held

print("Buy")
     balance-= last_price
     pos_held = True
     buys += 1
elif : 
    ma-0.1>last_price and pos_held
    print("Sell")
    balance+= last_price
    pos_held = False
    sells += 1
    print(balance)
    time.sleep(0.01)

    print("")
    print("Buys:" + str(buys))
    print("Sells:" + str(sells))


    if buys>sells:
            balance += close_list[60 * hours_to_test – 1] # Add back your equity to your balance
            print("Final Balance:"+str (balance))

            print(“Profit if held: ” + str(close_list[60 * hours_to_test – 1] – close_list[0]))
            print(“Profit from algorithm: ” + str(balance – startBal))


# حالاشمایک ربات معامله گر ابتدایی دارید
# ربات معاملاتی نرم افزاری است که به API صرافی مورد نظر معامله گرمتصل میشود
# تابه صورت خودکار باآن تعامل داشته باشد
# برای اتصال به صرافی مورد نظر باید ای پی صرافی مورد نظررابه ریات معامله گرداد API
#  

