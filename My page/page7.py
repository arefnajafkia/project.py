# Hello World project 
# python3
print ('='*20)
#روش  اول ========
# تهيه ليست به دوروش - درروش اول هم ميتوان عدد داد وهم اسم 
# ولي درروش دوم فقط بايدعددبدهيد
 

input_string = input('ليست خودرابايک فاصله بين اسم ياعدد وياهرچيزديگرواردکنيد :')
print("\n")
user_list = input_string.split()
# چاپ لیست
print('list: ', user_list)
print ()
print ("="*20)
#روش دوم  ============

number_list = []
n = int(input("تعداد اعداد خود را وارد کنید :"))

print("\n")
for i in range(0, n):
    print("عدد شماره ", i, " را وارد کنید")
    item = int(input())
    number_list.append(item)
#چاپ لیست
print("User list is ", number_list)
print ('='*20)
print ( 'Thanks for your cooperation \n ممنون ازهمکاري شما ')
