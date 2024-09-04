from tkinter import*
from PIL import Image,ImageTk
from random import randint
root=Tk()
root.title("Rock Paper Scissor")
root.configure(bg="#9b59b6")

#image
rock_img=ImageTk.PhotoImage(Image.open("rock.jpg",))
paper_img=ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_img=ImageTk.PhotoImage(Image.open("scissor.jpg"))
rock_comp_img=ImageTk.PhotoImage(Image.open("rock.jpg"))
paper_comp_img=ImageTk.PhotoImage(Image.open("paper.jpg"))
scissor_comp_img=ImageTk.PhotoImage(Image.open("scissor.jpg"))


#insert picture
user_label=Label(root,image=scissor_img,bg="#9b59b6",fg="#9b59b6")
comp_label=Label(root,image=scissor_comp_img,bg="#9b59b6",fg="#9b59b6")
user_label.grid(row=1,column=6)
comp_label.grid(row=1,column=0)

#score
playerscore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerscore=Label(root,text=0,font=100,bg="#9b59b6",fg="white")
computerscore.grid(row=1,column=1)
playerscore.grid(row=1,column=3)
#indicator
user_indicator=Label(root,font=50,text="USER",bg="#9b59b6",fg="white").grid(row=0,column=3)
comp_indicator=Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white").grid(row=0,column=1)

#messages
msg=Label(root,font=50,bg="#9b59b6",fg="white").grid(row=5,column=4)


#update message
def updatemessage(x):
     msg['text']=X


#update user score
def updateuserscore():
     score=int(playerscore["text"])
     score+=1
     playerscore["text"]=str(score)
#update computer score
def updatecompscore():
     score=int(computerscore["text"])
     score+=1
     computerscore["text"]=str(score)    


#check winner
def checkwin(player,computer):
     if player==computer:
          updatemessage("ITS A TIE")
          updatecompscore()
     elif player=="rock":
          if computer=="paper":
               updatemessage("YOU LOOSE")
               updatecompscore()
          else:
               updatemessage("YOU WIN")
               updateuserscore()
     elif player=="paper":
          if computer=="scissor":
               updatemessage("YOU LOOSE")       
               updatecompscore() 
          else:
                updatemessage("YOU WIN")
                updateuserscore()
     elif player=="scissor":
          if computer=="rock":
                updatemessage("YOU LOOSE")       
                updatecompscore() 
          else:   
               updatemessage("YOU WIN")
               updateuserscore()             
     else:
          pass           
           
 #update choice

choices=["rock","paper","scissor"]
def updatechoice(x):
    #for computer
    compchoice=choices[randint(0,2)]
    if compchoice=="rock":
        comp_label.configure(image=rock_comp_img)
    elif compchoice=="paper":
            comp_label.configure(image=paper_comp_img)
    else:
        comp_label.configure(image=scissor_comp_img)



    #for user
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
         user_label.configure(image=paper_img)    
    else :
         user_label.configure(image=scissor_img)    
    checkwin(x,compchoice)

#buttons
rock=Button(root,width=20,height=2,text="ROCK",bg="#FF3E4D",fg="white",command=lambda:updatechoice("rock")).grid(row=2,column=1)
paper=Button(root,width=20,height=2,text="PAPER",bg="#FAD02E",fg="white",command=lambda:updatechoice("paper")).grid(row=2,column=2)
scissor=Button(root,width=20,height=2,text="SCISSOR",bg="#0ABDE3",fg="white",command=lambda:updatechoice("scissor")).grid(row=2,column=3)

root.mainloop()