# Hello World project
# python3

# هرچه سوال دارید میتوانید بپرسید
# ربات فوق درحال تکمیل شدن میباشد
# ---------- smart Robot Afp ----------

from time import sleep
txt = '  I am a smart robot Afp  '
txt2 = '  ربات هوشمند ای اف پی هستم  '
x = txt.center(70,  '*')
y = txt2.center(70,  '=')
print(x)
print()
sleep(1) # تایم داده شده برای اجرای بعد
print(y)
print()
sleep(2) # تایم داده شده برای اجرای بعد
print("ساعت وتاریخ امروز <-- Time and date    ")
print("-"*40)
sleep(2) # تایم داده شده برای اجرای بعد
#درج تاریخ میلادی
import  _datetime
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
sleep(3) #  تایم داده شده برای اجرای بعد
# میپرسیم آیادوست داره ازش سوال کنیم
choice = input("""
میتونم چند تاسوال ازشمابپرسم ؟
اگرجواب شمابله است عدد 1رو بزن واگرنه 2 :
Can I ask you a few questions?
If the answer is yes, press the number 1, otherwise, press 2:
""")

if choice == "2":
    print("You are logged out\n شماازبرنامه خارج شدید")
    print()
    sleep(3)  # تایم داده شده برای اجرای بعد
    input("If we want, we can start again, press the number 1!\nاگربخواهید میتونید دوباره شروع کنید عدد 1روبزن !")
    print()
else:
    print("ممنون که وقتتون روبه من دادید\nthank you for your time")
    print()
    sleep(2)  # تایم داده شده برای اجرای بعد
    try:
        print('''
        Please write the answers to the questions in English
        Write the date, month and day in numbers
        Otherwise you will get an error
        لطفا جواب سوالات را به انگلیسی بنویسید
وتاریخ , ماه وروز را به عدد بنویسید        
درغیر این صورت با خطا مواجه خواهید شد        
        ''')
        sleep(7)  # تایم داده شده برای اجرای بعد
        g = input("شمامردهستید یازن؟\n Wath is your gender,Mr.or Mrs ?")

        name = input("نام ونام خانوادگس شما؟ \n please enter your name ? ")

        city = input("متولد کدام شهرید؟ \n Born in which city {}.{} ?".format(g, name))

        birth_year = input("متولد چه سالی هستید؟ \n birth year ?")


        age = 1401 - int(birth_year)
        Y = birth_year
        M = int(input("متولد چه ماهی هستید؟ \n Enther Month ?"))

        D = int(input("متولد جه روزی هستید؟ \n Enther Day ?"))
        S = city

        sleep(3) # تايم داده شده براي اجراي بعدي
        print("-" * 30)
        print("\n" * 1, "Hello", "سلام", "\n" * 1)
        print("خوش آمدید", g, name, "شما", age, "دارید وازشهر", city, "هستید.")
        print("Welcome ", g, name, "you are", age, "years old and You were born in ", city, "!")

        # tarekh tavalod and rooz
        Month = ["Farvardin", "Ordibehesht", "Khordad", "Tir", "Mordad", "Shahrivar", "Mehr", "Aban", "Azar", "Day",
                 "Bahman", "Esfand"]
        Month_farse = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن",
                       "اسفند"]
        end = ["st", "nd", "rd"] + 17 * ["th"] + ["st", "nd", "rd"] + 7 * ["th"] + ["st"]

        m_index = M - 1
        d_index = D - 1

        sleep(4) # تايم داده شده براي اجراي بعدي
        print()
        print("شمامتولد", D, Month_farse[m_index], "", Y)
        print("You were born ", D, end[d_index], " ", Month[m_index], " ", Y)
        print()

        sleep(4) # تايم داده شده براي اجراي بعدي
        year_born = int(now.year - age)
        print("شمامتولدشدیددرسال میلادی", year_born)
        print("Awesome ! you were born in ", year_born)
        print("-" * 30)
        print()
    except SyntaxError:
        print('لطفا انگلیسی تایپ کنید')
    except ValueError:
        print('لطفا با عدد بنویسید')
    except:
        print('Error \n خطایی رخ داده دوباره سعی کنید')

    # درآخرتایم بازی رامینویسد
    import time

    start = time.time()

    # تايم داده شده براي اجراي بعدي
    sleep(5)
    # شروی بازی
    choice = input(
        "دوست داری بازی کنیم اگربله 1 روبزن واگرنه 2؟ \n Do you want to play, if yes, press 1,if not,press 2 {}.{}:".format(
            g, name))
    if choice == "2":
        print("You are logged out\n شماازبرنامه خارج شدید")
        input("And you will not continue\n ودیگردوست ندارید ادامه دهید")
    else:
        print("ممنون که دوباره وقتتون روبه من دادید\nThank you for your time again")
    print()

    sleep(3)  # تايم داده شده براي اجراي بعدي
    print("لطفایک شماره از 1 تا 1000 انتخاب کن وبمن نگو \nPlease select a number from 1 to 1000 and do not say")
    sleep(3)  # تايم داده شده براي اجراي بعدي
    print("من میپرسم تابتونم شماره روپیداکنم \nI'm asking for your Rupid number")
    print()
    # برنامه نوشته شده براي پيداکردن عدد انتخابي
    # Written program to find the selected number
    from math import floor

    sleep(3)  # تايم داده شده براي اجراي بعدي

    def IsGuessTrue(Min, Max, Guess, NoGuess):
        if Min == Max:
            return
        else:
            OP = input(
                "Is your number (E)اگرخودش بود بنويس\nqual to ,(B)اگربزرگتربود بنويس\nreater than or (K)اگرکوچکتربودبنويسess than %i: " % Guess)
            if (OP == 'E' or OP == 'e'):
                print("I found your number in %i Guess , it is %i" % (NoGuess, Guess))
                print("من تونستم با % i بارپرسش حدس بزنم,پس حدس من درسته: %i" % (NoGuess, Guess))
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

    sleep(4)  # تايم داده شده براي اجراي بعدي
    print()
    print("ممنون که وقتتون روبه من دادید\nthank you for your time ,{}.{}".format(name, age))
    sleep(2)  # تايم داده شده براي اجراي بعدي
    print()
    # تایم بازی راپرینت میکند
    print("زمان بازی شما:\nRun Time :" + str(time.time() - start))

    #input('Ask me any questions you have.\n هرچه سوال دارید ازمن بپرسید.')