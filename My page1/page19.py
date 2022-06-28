# Hello World project 
# python3
# ساخت یک ربات نمونه برای IWOR باپایتون
# توجه: کلیه کدهای درون این متن آموزشی و همچنین کدهای درون دایرکتوری '(sample/robots/Tutorial(Python' تحت قوانین اجازه نامه عمومی گنو (GPL) منتشر شده‌اند.
# در ابتدا ربات باید به سرور شبیه ساز متصل شود.
# . کاری که باید انجام شود باز کردن یک socket و اتصال آن به این پورت است.
# استفاده از socket در پایتون بسیار ساده است. خطوط اولیه ربات ما به این شکل خواهد بود:


import sys
from socket import *

server = socket(AF_INET, SOCK_STREAM) #Creating a socket.
server.connect(('localhost', 7200))   #Connecting to the server.


# بعد از اتصال به سرور، ربات ما باید مشخصات خود را به سرور ارسال کند تا بتواند وارد بازی شود
import sys
from socket import *

server = socket(AF_INET, SOCK_STREAM) #Creating a socket.
server.connect(('localhost', 7200))   #Connecting to the server.

#Initilizing ...
server.send('INIT&1&Pitiless Killer&0&')
serverMessage = server.recv(256)
while (serverMessage != '255'):
   server.send('INIT&1&Tutorial&0&')
   serverMessage = server.recv(256)

   # در این بخش، ما متدی به نام randomMove به کد خود اضافه خواهیم کرد

  import random

def randomMove():
   rndint = (int)(random.random() * 4)
   if rndint == 0:
      return 'MOVE&NORTH&'
   elif rndint == 1:
      return 'MOVE&EAST&'
   elif rndint == 2:
      return 'MOVE&SOUTH&'
   else:
      return 'MOVE&WEST&'
      
      movingCommand = 'MOVE&EAST&'

#Moving around ...
while (True):
   server.send(movingCommand)
   serverMessage = server.recv(256)
   if (serverMessage != '255'):
      #I hit a wall or something, changing the direction.
      movingCommand = randomMove()


      def seekCrystal(senseResult):
   index = 0
   lastAmpPosition = 0
   result = ['','']

   while index < len(senseResult):
      if senseResult[index]=='&':
         if (senseResult[index-1]=='C'):
            #I found a crystal!
            i = lastAmpPosition
            j = lastAmpPosition
            k = 0
            while (i < index-1):
               if (senseResult[i]==','):
                  result[k] = senseResult[j+1:i]
                  k=k+1
                  j = i
               
               i = i+1
            
         lastAmpPosition = index

      index = index+1

   return result

#این کد آنقدر که به نظر می‌رسد پیچیده نیست. در ابتدا، کاراکترهای '&' را پیدا خواهد کرد و برسی می‌کند که آیا کاراکتر قبلی آن یک کریستال است یا خیر:

   while index < len(senseResult):
      if senseResult[index]=='&':
         if (senseResult[index-1]=='C'):
            #I found a crystal!
            
            
            lastAmpPosition = index

            index = index+1
      
#ر کریستالی درون رشته دریافتی بود، ما موقعیت آن را احتیاج داریم. تنها کاری که باید انجام شود پیدا کردن ',' درست قبل از کاراکتر 'C' است:

   while (i < index-1):
      if (senseResult[i]==','):
         result[k] = senseResult[j+1:i]
         k=k+1
         j = i
                  
         i = i+1

# http://iwor.sourceforge.net/fa/Make-Simple-Bot(Python)-Persian.html#con مرجع دانلود
  