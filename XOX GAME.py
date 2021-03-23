from tkinter import *

from tkinter import messagebox

game_window = Tk()

game_window.title("XOX GAME")

clicks = 0
turn_of = True

def play_game_end():
    if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X"
       or button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X"
       or button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X"
       or button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X"
       or button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X"
       or button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X"
       or button9["text"] == "X" and button6["text"] == "X" and button3["text"] == "X"
       or button7["text"] == "X" and button5["text"] == "X" and button3["text"] == "X"):

        box = messagebox.showinfo("Winner", "Player 1 won the match")
      
    elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O"
          or button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O"
          or button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O"
          or button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O"
          or button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O"
          or button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O"
          or button9["text"] == "O" and button6["text"] == "O" and button3["text"] == "O"
          or button7["text"] == "O" and button5["text"] == "O" and button3["text"] == "O"):
        box = messagebox.showinfo("Winner", "Player 2 won the match")
    elif clicks == 8:
        box = messagebox.showinfo("Winner", "Tie")


def btnClick(buttons):
    global clicks, turn_of
    if buttons["text"]==" " and turn_of==True:
        buttons["text"]="X"
        turn_of = False
        play_game_end()
        clicks+=1
    elif buttons["text"]==" " and turn_of==False:
        buttons["text"]="O"
        turn_of = True
        play_game_end()
        clicks+=1



buttons = StringVar()

button1 = Button(game_window, text=" ",font=('Arial',20),bg='sky blue',
                 fg='blue',height=2,width=4,command=lambda: btnClick(button1))
button1.grid(row=1,column=1)


button2 = Button(game_window,text=" ",font=('Arial',20),bg='sky blue',
                 fg='blue',height=2,width=4,command=lambda: btnClick(button2))
button2.grid(row=1,column=2)


button3 = Button(game_window,text=" ",font=('Arial',20),bg='sky blue',
                 fg='blue',height=2,width=4,command=lambda: btnClick(button3))
button3.grid(row=1,column=3)



button4 = Button(game_window,text=" ",font=('Arial',20),bg='sky blue',
                 fg='blue',height=2,width=4,command=lambda: btnClick(button4))
button4.grid(row=2,column=1)


button5 = Button(game_window,text=" ",font=('Arial',20),bg='sky blue',
                 fg='blue',height=2,width=4,command=lambda: btnClick(button5))
button5.grid(row=2,column=2)


button6 = Button(game_window,text=" ",font=('Arial',20),bg='sky blue',
                 fg='blue',height=2,width=4,command=lambda: btnClick(button6))
button6.grid(row=2,column=3)



button7 = Button(game_window,text=" ",font=('Arial',20),bg='sky blue',
                 fg='blue',height=2,width=4,command=lambda: btnClick(button7))
button7.grid(row=3,column=1)


button8 = Button(game_window,text=" ",font=('Arial',20),bg='sky blue',
                 fg='blue',height=2,width=4,command=lambda: btnClick(button8))
button8.grid(row=3,column=2)


button9 = Button(game_window,text=" ",font=('Arial',20),bg='sky blue',
                 fg='blue',height=2,width=4,command=lambda: btnClick(button9))
button9.grid(row=3,column=3)


s = input()

