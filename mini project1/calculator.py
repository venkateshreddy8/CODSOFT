from tkinter import *


root=Tk()
root.title("calculator")

input=Entry(root, width=50)
input.grid(row=0, column=0, columnspan=4, padx=15, pady=15)

def click(num):
    current=input.get()
    input.delete(0,END)
    input.insert(0, str(current) + str(num))
     


def add():
    fnum=input.get()
    global math 
    math='addition'
    global f
    f=int(fnum)
    input.delete(0,END)

def sub():
    fnum=input.get()
    global math 
    math='subtraction'
    global f
    f=int(fnum)
    input.delete(0,END)



def multiplication():
    fnum=input.get()
    global math 
    math='multiplication'
    global f
    f=int(fnum)
    input.delete(0,END)

    
def division():
    fnum=input.get()
    global math 
    math='division'
    global f
    f=int(fnum)
    input.delete(0,END)

    

def clear():
    input.delete(0,END)
    return

def equal():
    
    snum=input.get()
    input.delete(0,END)
    if math=='addition':
        input.insert(0,f+int(snum))
    elif math=='subtraction':
        input.insert(0,f-int(snum))
    elif math=='multiplication':
        input.insert(0,f*int(snum))
                     
    elif math=='division':
        input.insert(0,f /int(snum))
                     


button_1=Button(root,text="1",padx=50,pady=25,command=lambda:click(1))
button_2=Button(root,text="2",padx=50,pady=25,command=lambda:click(2))
button_3=Button(root,text="3",padx=50,pady=25,command=lambda:click(3))
button_4=Button(root,text="4",padx=50,pady=25,command=lambda:click(4))
button_5=Button(root,text="5",padx=50,pady=25,command=lambda:click(5))
button_6=Button(root,text="6",padx=50,pady=25,command=lambda:click(6))
button_7=Button(root,text="7",padx=50,pady=25,command=lambda:click(7))
button_8=Button(root,text="8",padx=50,pady=25,command=lambda:click(8))
button_9=Button(root,text="9",padx=50,pady=25,command=lambda:click(9))
button_0=Button(root,text="0",padx=50,pady=25,command=lambda:click(0))


button_equal=Button(root,text="=",padx=49,pady=25,command=equal)
button_clear=Button(root,text="AC",padx=45,pady=25,command=clear)
button_add=Button(root,text="+",padx=50,pady=25,command=add)
button_sub=Button(root,text="-",padx=52,pady=25,command=sub)
button_multiplication=Button(root,text="*",padx=52,pady=25,command=multiplication)
button_division=Button(root,text="/ ",padx=50,pady=25,command=division)



button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_add.grid(row=1,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_multiplication.grid(row=3,column=3)


button_0.grid(row=4,column=0)
button_clear.grid(row=4,column=1)
button_division.grid(row=4,column=3)

button_equal.grid(row=4,column=2)


root.mainloop()