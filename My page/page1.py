# Hello World project 
# python3
# من يک رباتم manrobatam
# من یک ربات هستم نوشته شده برای ویژوال کد باپایتون 3

from time import sleep

print("من یک رباتم واسمم پایتون 9!")
print("I am a robot,My name is python 9.")
print()
# تایم داده شده برای اجرای بعدی
sleep(2)
print("ساعت وتاریخ امروز\nTime and date")
print("-"*20)
#تایم داده شده برای اجرای بعدی
sleep(2)
#درج تاریخ میلادی
import _datetime
now = _datetime.datetime.today()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
print(mm + "/" + dd +"/" + yyyy +" " + hour + ":" + mi + ":" + mi + ":" + ss)
#نوشتن تاریخ به ماه و سال و ساعت
print("-"*20)

import datetime as dt
today_date = dt.date.today()
print(today_date.strftime("the current Date is :\n \n%A %B %d,%Y"))
print("-"*20)
print()
#تايم داده شده براي اجراي بعدي
sleep(3)
# میپرسیم آیادوست داره ازش سوال کنیم
choice = input("میتونم چندتا سوال ازشمابپرسم ؟اگربله است عدد1روبزن واگرنه 2 : :\nHow many questions can I ask you :")
if choice == "2":
    print("You are logged out\n شماازبرنامه خارج شدید")
    input("And you will not continue\n ودیگردوست ندارید ادامه دهید")
else:
    print("ممنون که وقتتون روبه من دادید\nthank you for your time")
    print()
#تایم داده شده برای اجرای بعدی
sleep(2)
g = input("شمامردهستید یازن؟\n Wath is your gender,Mr.or Mrs ?")
#تایم داده شده برای اجرای بعدی
#sleep(1)
name = input("نام ونام خانوادگس شما؟ \n please enter your name ? ")
#تایم داده شده برای اجرای بعدی
#sleep(1)
city = input("متولد کدام شهرید؟ \n Born in which city {}.{} ?".format(g,name))
#تایم داده شده برای اجرای بعدی
#sleep(1)
birth_year = input("متولد چه سالی هستید؟ \n birth year ?")
#تایم داده شده برای اجرای بعدی
#sleep(1)

age = 1401 - int (birth_year)
Y = birth_year
M = int (input("متولد چه ماهی هستید؟ \n Enther Month ?"))
#تایم داده شده برای اجرای بعدی
#sleep(1)
D = int(input("متولد جه روزی هستید؟ \n Enther Day ?"))
S = city

#تايم داده شده براي اجراي بعدي
sleep(3)
print("-"*30)
print("\n"*1,"Hello","سلام","\n"*1)
print("خوش آمدید",g,name,"شما",age,"دارید وازشهر",city,"هستید.")
print("Welcome ",g ,name, "you are" ,age,"years old and You were born in " ,city , "!")

#tarekh tavalod and rooz
Month = ["Farvardin","Ordibehesht","Khordad","Tir","Mordad","Shahrivar","Mehr","Aban","Azar","Day","Bahman","Esfand"]
Month_farse =["فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","آبان","آذر","دی","بهمن","اسفند"]
end = ["st" , "nd" , "rd"] + 17*["th"] + ["st" , "nd" , "rd"] +7 * ["th"] + ["st"]

m_index = M-1
d_index = D-1
#تايم داده شده براي اجراي بعدي
sleep(4)
print()
print( "شمامتولد",D,Month_farse [m_index] ,"",Y)
print("You were born " ,D, end[d_index] ,  " " , Month[m_index] ,  " " , Y )
print()
#تايم داده شده براي اجراي بعدي
sleep(4)
year_born =  int(now.year - age)
print( "شمامتولدشدیددرسال میلادی",year_born)
print("Awesome ! you were born in ", year_born)
print("-"*30)
print()
#درآخرتایم بازی رامینویسد
import  time
start = time.time()

#تايم داده شده براي اجراي بعدي
sleep(5)
#شروی بازی
choice = input("دوست داری بازی کنیم اگربله 1 روبزن واگرنه 2؟ \n Do you want to play, if yes, press 1,if not,press 2 {}.{}:".format(g,name))
if choice == "2" :
    print("You are logged out\n شماازبرنامه خارج شدید")
    input("And you will not continue\n ودیگردوست ندارید ادامه دهید")
    root.destory()
else:
    print("ممنون که دوباره وقتتون روبه من دادید\nThank you for your time again")

print()
#تايم داده شده براي اجراي بعدي
sleep(3)

print("لطفایک شماره از 1 تا 1000 انتخاب کن وبمن نگو \nPlease select a number from 1 to 1000 and do not say")
#تايم داده شده براي اجراي بعدي
sleep(3)

print("من میپرسم تابتونم شماره روپیداکنم \nI'm asking for your Rupid number")
print()
# برنامه نوشته شده براي پيداکردن عدد انتخابي
# Written program to find the selected number
from math import floor

#تايم داده شده براي اجراي بعدي
sleep(3)
def IsGuessTrue(Min, Max, Guess, NoGuess):
    if Min == Max:
        return
    else:
        OP = input(
            "Is your number (E)اگرخودش بود بنويس\nqual to ,(B)اگربزرگتربود بنويس\nreater than or (K)اگرکوچکتربودبنويسess than %i: " % Guess)
        if (OP == 'E' or OP == 'e'):
            print("I found your number in %i Guess , it is %i" % (NoGuess, Guess))
            print("من تونستم با % i بارپرسش حدس بزنم,پس حدس من درسته: %i"% (NoGuess,Guess))
            Max = Min
            IsGuessTrue(Min, Max, Guess, NoGuess)
        elif (OP == 'B' or OP == 'b'):
            Min = Guess
            Guess = floor((Min + Max) / 2)
            NoGuess += 1
            IsGuessTrue(Min, Max, Guess, NoGuess)
        elif (OP == 'K' or OP == 'k'):
            Max = Guess
            Guess = floor((Min + Max) / 2)
            NoGuess += 1
            IsGuessTrue(Min, Max, Guess, NoGuess)
        else:
            print("Error in data")


Numbers = [x for x in range(1001)]
Min = 1
Max = 1000
Guess = floor((Min + Max) / 2)
NoGuess = 1
IsGuessTrue(Min, Max, Guess, NoGuess)
#تايم داده شده براي اجراي بعدي
sleep(4)
print()
print("ممنون که وقتتون روبه من دادید\nthank you for your time ,{}.{}".format(name,age))

#تايم داده شده براي اجراي بعدي
sleep(2)
print()
#تایم بازی راپرینت میکند
print("زمان بازی شما:\nRun Time :" + str(time.time() - start))

