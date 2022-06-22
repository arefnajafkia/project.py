
#barname phone ba save and delet and bacgrand meshge
from logging import root
from tkinter import messagebox
from tkinter import *
import webbrowser
import pyperclip
import random
import os


root = Tk()
root.title('Coontact Book')
root.geometry('650x300')
background = '#121212'
root.config(bg=background)

#contact Name label✔
#contact Name Entry✔

#contact Number label✔
#contact Number Entry✔

#Add contact Button✔
#Save list Button✔

#copy phone Number Button✔
#Open Saved Fille Button✔
#Delete Contact Button✔
#Exit App Button✔
# ListBox  For Contacts✔

# Functons
def add_contact() :
    contact_string = name_entry.get() + ': ' + phone_entry.get()
    listbox.insert(END, contact_string)
    
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    
def delete_contact():
        listbox.delete(ANCHOR)
        
def save_list():
    """ Save the list to a simple txt file """
            
    with open('D:\Visual Studio\MyProject\Contact Book\Data2.txt','w') as  f:
          list_tuple = listbox.get(0, END)
          for item in list_tuple:
               if item.endswith('\n'):
                    f.write(item)
               else:
                    f.write(item+'\n')
def open_list():
        with open('D:\Visual Studio\MyProject\Contact Book\Data2.txt','r') as  f:
            for line in f:
                listbox.insert(END, line)
def open_dir():
        webbrowser.open('D:\Visual Studio\MyProject\Contact Book\Data2.txt')  

def copy_number():
        selected_contact = listbox.get(ANCHOR)
        number = selected_contact.split(': ')
        pyperclip.copy(number[1].replace('\n', ""))         

def exit():
          choice = messagebox.askquestion('Exit Aplictation', 'Are you sure you want to ciose the application ?')
          if choice =='yes':
             root.destroy()
          else:
               return 
    
#labellist For Contact
name_label = Label(root, text='Contact Name:', bg=background,  fg='white',  font=('calibri',12), anchor='w', justify=LEFT )
name_label. place(relx=0.1, rely=0.1, anchor='c')

name_entry = Entry(root, bg='white', fg=background, width=30, borderwidth=2)
name_entry. place(relx=0.4, rely=0.1, anchor='c')

phone_label = Label(root, text='   Contact:', bg=background,  fg='white',  font=('calibri',12), anchor='w', justify=LEFT )
phone_label. place(relx=0.1, rely=0.2, anchor='c')


phone_entry = Entry(root, bg='white', fg=background, width=30, borderwidth=2)
phone_entry. place(relx=0.4, rely=0.2, anchor='c')

add_btn = Button(root, text='Add Contact',  bg=background, fg='white', borderwidth=3, padx=125,command=add_contact )
add_btn.place(relx=0.29, rely=0.35, anchor='c')

save_btn = Button(root, text='Save List',  bg=background, fg='white',borderwidth=3, padx=135, command=save_list)
save_btn. place(relx=0.29, rely=0.5, anchor='c')

copyPhone = Button(root, text='Copy Phone Number',  bg=background, fg='white',borderwidth=3, padx=10, command=copy_number )
copyPhone. place(relx=0.15, rely=0.65, anchor='c')

deletePhone = Button(root, text='Delete Contact',  bg=background, fg='white', borderwidth=3, padx=28 ,  command=delete_contact)
deletePhone.place(relx=0.15, rely=0.77, anchor='c')

openSaved = Button(root, text='Open Saved File',  bg=background, fg='white',borderwidth=3, padx=30, command=open_dir )
openSaved.place(relx=0.42, rely=0.65, anchor='c')

exit = Button(root, text='Exit App',  bg=background, fg='white',borderwidth=3, padx=50, command=exit)
exit.place(relx=0.42, rely=0.77, anchor='c')

listbox = Listbox(root, width=40, height=15)
listbox.place(relx=0.75, rely=0.47, anchor='c')



open_list()
root.mainloop ()
