import tkinter as tk
from tkinter import *
import random
import os
from PIL import Image, ImageTk

gw = tk.Tk()
gw.configure(bg="sky blue")
gw.geometry("750x450")
gw.title("Number Gussing Game")

answer = StringVar()
lives = IntVar()
lives1 = IntVar()
your_number = IntVar()
the_number = random.randint(1,100)
answer.set("Guess My Number Between 1 To 100")
lives.set(10)
lives1.set(lives.get())

def playfun():
    lives1.set(lives.get())
    if lives1.get() > 0:
        
        if your_number.get()> 100 or your_number.get()<0:
            answer.set("Enter Between 1-100. You just lost 1 live!")
            lives.set(lives.get()-1)
            lives1.set(lives.get())

        elif the_number == your_number.get():
            answer.set("Wow! You Won The Game!!")
            lives.set(lives.get()-1)
            lives1.set(lives.get())

        elif the_number > your_number.get():
            answer.set("You Entered A Small Number: Guess a Bigger Number")
            lives.set(lives.get()-1)
            lives1.set(lives.get())

        elif the_number < your_number.get():
            answer.set("You Entered A Big Number: Guess a Smaller Number")
            lives.set(lives.get()-1)
            lives1.set(lives.get())

    else:
        answer.set("GAME OVER")



def play_again():
    the_number = random.randint(1,100)
    answer.set("Guess My Number Between 1 To 100")
    lives.set(10)
    lives1.set(lives.get())


key1 = Entry(gw, textvariable = your_number,width=5,font = ('Arial',50),relief=GROOVE)
key1.place(relx=0.5, rely=0.3, anchor=CENTER)

key2 = Entry(gw, textvariable = answer, width = 50, font = ('Arial',20),relief=GROOVE)
key2.place(relx=0.5, rely=0.7, anchor=CENTER)

key3 = Entry(gw, textvariable = lives1, width = 2, font = ('Arial',20),relief=GROOVE)
key3.place(relx=0.61, rely=0.85, anchor=CENTER)

text1 = Label(gw, text = "Guess My Number Between 1 To 100", font = ('Arial',25),relief = GROOVE)
text1.place(relx=0.5, rely=0.09, anchor=CENTER)

text2 = Label(gw, text='Lives',font=("Courier", 25), relief=GROOVE)
text2.place(relx=0.3, rely=0.85, anchor=CENTER)

playb = Button(gw, width=8, text='PLAY', font=('Courier', 25), command=playfun, relief=GROOVE)
playb.place(relx=0.5, rely=0.5, anchor=CENTER)

stop = tk.Button(gw, text='stop', width=40, command=gw.destroy,bg="red", activebackground="red", relief=GROOVE)
stop.place(relx=0.25, rely=1, anchor=S)

reset = tk.Button(gw, text='Restart', width=40, command=play_again,bg="red", activebackground="red", relief=GROOVE)
reset.place(relx=0.75, rely=1, anchor=S)

gw.mainloop()
