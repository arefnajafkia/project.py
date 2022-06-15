# Hello World project 
# python3
#توليد رمزعبوريکبارمصرف باپايتون3
#فقط کافيه شماتعدادکارکترهارابگوييدوبه همان تعداد به شما يک رمز
#بااون تعداد کارکتري که گفته بوديد ميده بي نهايت ميشه انجام داد


import random
print(''' Welcome To Password Generator ... ''')
pass_range = int(input('Please Enter The Password Range : \n لطفا محدوده رمز عبور را وارد کنید :'))
alefba = ('abcdefglomnp123456789_*#$@!%ASDFGHJKLMNBVCXZQWERTYUIOP')
if pass_range >= 8:
    for i in range(pass_range):
        i = random.choice(alefba)
        print(i, end= '')
        
else:
    print('You Can Not Choice >8 Number ! \n کمتراز8 کارکترنمي شود !')
