# Hello World project 
# python3
# دفترچه تلفن ساده شخصی باپایتون 3
#Personal phonebook

import os
import webbrowser
#os.getcwd()
#output = open('D:\python -film\Data1.txt', 'a+')
#output.write(text)
#output.close()


phone_book = {'aref':{'phone':'09172536145','Manzel':'05522222222','Mahalkar':'05133333333',
                      'Address':'thran '},
'hamed':{'phone':'091823565892','Manzel':'02155555555','Mahalkar':'02666666666',
            'Address':'thran '},
'parviz':{'phone':'09175285854','Manzel':'0252525252','Mahalkar':'0233366666',
          'Address':'thran '},
'reza':{'phone':'09585858582','Manzel':'056565655','Mahalkar':'088888888',
         'Address':'thran'},
'maryam':{'phone':'08525855225','Manzel':'44444444','Mahalkar':'23222222',
         'Address':'thran'},
}

labels = {'phone':'phone number','Manzel':'telefon manzel','Mahalkar':'telfon mahalkar','Address':'Address'}
name = input('name = ')
   
name = name.lower()
r = input ('phone number (p) Manzel (m) Mahalkar (k) Address (a) = ')
if r == 'p': key = 'phone'
if r == 'm': key = 'Manzel'
if r == 'k': key = 'Mahalkar'
if r == 'a': key = 'Address'

if name in phone_book: print ("%s's %s is %s "%(name,labels[key],phone_book[name][key]))
else :
    print("Your request does not exist! " )
    print()
    print("وجودنداشت",name,"مشخصات")
    