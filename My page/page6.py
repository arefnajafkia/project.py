# Hello World project 
# python3
#پيداکردن اسم از درون ليست
# D:\python -film\Data2.txt آدرس فایل جدید روباید جایگذین کنید تاکارکندبجای 
masir_file = 'D:\python -film\Data2.txt'
with open (masir_file)as f:

    mohtaviat = f.read()
    name = input ("Enther username ?\n اسم موردنظرتان رابه انگليسي بنويسيد:")
    if name in (mohtaviat) :

        print()
        print ('Welcome' ,name ,'\n اسم شمادرليست مابود!''\n your name was on the list!')
        print()
        print ('='*20)
        print()
        print ('دراين ليست ميباشد',name)
        print()
        print (mohtaviat)
    else:
        print()
        print ('Welcome',name,'\nاسم شما درليست مانبود !''\n sorry name is missing !')
        print()
        print('='*20)
