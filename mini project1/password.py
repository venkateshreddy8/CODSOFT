from tkinter import *
import string
import random
import pyperclip

root=Tk()
root.title("Password Generator")
root.config(bg='gray65')
choice=IntVar()
Font=('aral',13,'bold')

def generator():
    smallcase_letters=string.ascii_lowercase
    uppercase_letters=string.ascii_uppercase
    numbers=string.digits
    symbols=string.punctuation
    all=smallcase_letters+uppercase_letters+numbers+symbols

    password_length=int(length_spinbox.get())

    if choice.get()==1:
        passwordfield.insert(0,random.sample(smallcase_letters,password_length))

    
    if choice.get()==2:
        passwordfield.insert(0,random.sample(smallcase_letters+uppercase_letters,password_length))      
    
    if choice.get()==3:
        passwordfield.insert(0,random.sample(smallcase_letters+uppercase_letters+numbers+symbols,password_length))    



   # password=random.sample(all,password_length)
   # passwordfield.insert(0,password)

def copy():
    random_password=passwordfield.get()
    pyperclip.copy(random_password)


passwordlabel=Label(root,text="PASSWORD GENERATOR",font=('times new roman',25,'bold'),bg='gray65',fg='black')
passwordlabel.grid()

weakradiobutton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradiobutton.grid(pady=5)
pady=5
mediumradiobutton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradiobutton.grid(pady=5)

strongradiobutton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradiobutton.grid(pady=5)


passwordlabel=Label(root,text='Password Length',font=('Font',15,'bold'),bg='gray65',fg='black')
passwordlabel.grid(pady=10)

length_spinbox=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_spinbox.grid(pady=5)

generate_button=Button(root,text='Generate',font=Font,command=generator)
generate_button.grid(pady=5)

passwordfield=Entry(root,width=25,bd=3,font=Font)
passwordfield.grid()

copy_button=Button(root,text='Copy',font=Font,command=copy)
copy_button.grid(pady=8)


root.mainloop()
