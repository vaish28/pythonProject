from tkinter import *
import random

root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Rock, Paper & Scissors Game')
root.config(bg='light blue')  # Change the background color here
Label(root, text='Rock, Paper & Scissors Game', font='Helvetica 20 bold', bg='light blue').pack()


Label(root, text='Choose any one: rock, paper, scissors', font='Helvetica 12 bold', bg='light blue').place(x=50, y=70)
user_take = Entry(root, font='Helvetica 10 bold', bg='white')
user_take.place(x=110, y=130)

choices = ['rock', 'paper', 'scissors']
comp_pick = random.choice(choices)

Result = StringVar()


def play():
    user_pick = user_take.get()
    result_messages = {
        'rock': {'rock': 'tie, you both select same', 'paper': 'you lose, computer select paper',
                 'scissors': 'you win, computer select scissors'},
        'paper': {'rock': 'you win, computer select rock', 'paper': 'tie, you both select same',
                  'scissors': 'you lose, computer select scissors'},
        'scissors': {'rock': 'you lose, computer select rock', 'paper': 'you win, computer select paper',
                     'scissors': 'tie, you both select same'}
    }

    if user_pick not in result_messages or comp_pick not in result_messages[user_pick]:
        Result.set('Invalid: choose any one -- rock, paper, scissors')
    else:
        Result.set(result_messages[user_pick][comp_pick])


def ResetUserInput():
    Result.set("")
    user_take.delete(0, END)

def ExitGame():
    root.destroy()

Entry(root, font = 'arial 10 bold', textvariable = Result, bg ='white',width = 50,).place(x=25, y = 250)

Button(root, font = 'arial 13 bold', text = 'PLAY'  ,padx =5,bg ='seashell2' ,command = play).place(x=150,y=190)

Button(root, font = 'arial 13 bold', text = 'RESET'  ,padx =5,bg ='seashell2' ,command = ResetUserInput).place(x=70,y=310)

Button(root, font = 'arial 13 bold', text = 'EXIT'  ,padx =5,bg ='seashell2' ,command = ExitGame).place(x=230,y=310)


root.mainloop()