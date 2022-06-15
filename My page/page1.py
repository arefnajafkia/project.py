# Hello World project 
# python3
# من يک رباتم manrobatam

print  ( ' من يک رياط هستم واسمم پايتون9 است ')
print (' I am a robot , My name is python 9 .')

print()
print ("ساعت وتاريخ امروز\nTime and date")
print("-"*20) 

#درج تاريخ ميلادي 
import datetime
now = datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
print (mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)

# نوشتن تاربخ به ماه وسال وساعت
print ('-'*20)
import datetime as dt
today_date = dt.date.today()
print(today_date.strftime("The Current Date is :\n\n%A %B %d, %Y"))

print ('-'*20)
print()

print ('ميتونم چندتاسوال ازشمابپرسم؟\nHow many questions can I ask you?')
print()
g = input ( "شمامردهستيد يازن؟ What is your gender, Mr.or Mrs.?")
name = input ("  نام ونام خانوادگي شما please enter your name : ")
city = input (' متولد کدام شهريد Born in which city {}.{}:'.format(g,name))
birth_year = input ("متولد چه سالي هستي birth year: ")

age = 1401 - int (birth_year)
Y = birth_year
M = int(input('متولد چه ماهي هستيEnter Month :'))
D = int(input('متولد چه روزي هستيEnter Day :'))
S = city

print('-'*30)
print ("\n"*1,"Hello","سلام","\n"*1)
print ( '!هستيد',city,'شما',age,'داريد وازشهر',g ,name,'خوش آمديد')
print ( "Welcome ",g ,name, "you are" ,age, "years old  and You were born in  " ,city , "!" )

# tarekh tavalod and rooz 
Month = [ 'Farvardin','Ordibehesht', 'Khordad','Tir', 'Mordad', 'Shahrivar', 'Mehr', 'Aban', 'Azar', 'Day', 'Bahman','Esfand' ]
Month_farse =[ 'فروردين','ارديبهشت','خرداد','تير','مرداد','شهريور','مهر','آبان','آذر','دي','بهمن ','اسفند' ]
end = ['st' ,  'nd' ,  'rd'] + 17*['th'] + [ 'st' , 'nd' , 'rd'] +7 * ['th'] + ['st']

m_index = M-1
d_index = D-1
print()
print ( Y,'شمامتولد',D,Month_farse [m_index] ,'')
print ('You were born ' ,D, end[d_index] ,   ' ' ,  Month [m_index] ,   ' ' ,  Y )
print()
# sen karbar ra migirad and tarikh tavalod ra mydahad
#import datetime
#now = datetime.datetime.now()
#age = float(input('شماچند سال داريد What is your age? '))
year_born =  int(now.year - age)
print (year_born,"شمامتولدشديددرسال ميلادي",)
print("Awesome! you were born in ", year_born)

print('-'*30)
print()

#درآخرتايم بازي رامينويسد
import time
start = time.time()

#شروي بازي 
print ("بياباهم بازي اعدادکنيم\nLet's play numbers together {}.{}".format(g,name))
print()
print ( 'لطفا يک شماره از1تا 1000 انتخاب کن وبمن نگو\nPlease select a number from 1 to 1000 and do not say')
print ("من ميپرسم تابتونم شماره روپيداکنم\nI'm asking for your Rupid number")

print()
#برنامه نوشته شده براي پيداکردن عدد انتخابي
#Written program to find the selected number
from math import floor

def IsGuessTrue(Min, Max, Guess, NoGuess):
    if Min == Max :
        return
    else:
        OP = input ("Is your number (E)اگرخودش بود بنويس\nqual to ,(B)اگربزرگتربود بنويس\nreater than or (K)اگرکوچکتربودبنويسess than %i: " % Guess )
        if (OP == 'E' or OP == 'e'):
            print ("I found your number in %i Guess , it is %i"% (NoGuess, Guess))
            Max = Min
            IsGuessTrue(Min, Max, Guess, NoGuess)
        elif (OP == 'B' or OP == 'b'):
            Min = Guess
            Guess = floor ((Min + Max)/2)
            NoGuess += 1
            IsGuessTrue(Min, Max, Guess, NoGuess)
        elif (OP == 'K' or OP == 'k'):
            Max = Guess
            Guess = floor ((Min + Max)/2)
            NoGuess += 1
            IsGuessTrue(Min, Max, Guess, NoGuess)
        else: 
             print ("Error in data")
             

Numbers = [x for x in range (1001)]
Min = 1
Max = 1000
Guess = floor ((Min + Max)/2)
NoGuess = 1
IsGuessTrue(Min, Max, Guess, NoGuess)

print()
print ("ممنون که وقتتون روبمن داديد\nThank you for your time, {}.{} !".format(g,name))

print()
#تايم بازي راپرينت ميکند
print("زمان بازي شما\nRun Time: " + str( time.time() - start ))
