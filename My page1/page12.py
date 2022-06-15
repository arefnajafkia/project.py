# Hello World project 
# python3
# بازي با تاس تاهرچقدر بخواهيد ميتوانيد بازي کنيد
#تاس بازی باکامپیوترباهرباربازی برنده گفته میشه
import random


while True:
    start = input ('Start ? (Y/N) \n شروع کن :').upper()
    if start == 'Y':
        a = random.randint(1,6)
        print (a,':شماره شما شد ')
        b = random.randint(1,6)
        print (b,':شماره من شد ')
        print()
    if a>b:
        print('You came 😯 شمابرديد')
    if a<b:
        print ('I won 😀 من بردم')
    if a == b:
        print ('We were equal 😊 مساوي شديم ')
        print()
        print(5*'=')
    else:
        print ('Program Closed ! \n اين مرحله تموم شد! ')
        print()
        print (5*'=')
        pass
