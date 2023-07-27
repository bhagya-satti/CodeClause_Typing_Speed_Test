import random
from tkinter import *
import tkinter.font as tkFont
import time


root = Tk(className=" Speed Typing Test ")
root.geometry("850x550")


root.configure(bg='#2a2d36')


title = Label(root, text="SPEED TYPING TEST", font=("Doctrine",25,"bold"),bg="#2a2d36",fg="#fff")
title.place(x=260, y=7)



e = Entry(root, width='45', bg="black", fg="white",font=("helvetica 20",20,"italic"))
e.place(x=70, y=330)
e.focus()

text = Label(root, height='6', width='47', fg='white', bg='black', font="helvetica 20", justify=LEFT)
text.place(x='40', y='90')

def clearfunc():
    e.delete(0, END)


reset = Button(root, text="RESET", bg="black", fg="White", font="helvetica 20", padx=20, pady=10,command=clearfunc)
reset.place(x=100, y=380)


def randomTXT():
    f = open('Sentence.txt').read()
    sentences = f.split('\n')
    display = random.choice(sentences)
    text.config(text=display)
randomTXT()


switch = Button(root, text="SWITCH-UP", bg='black', fg='white', font="helvetica 20", padx=15, pady=10, relief=RAISED, command=randomTXT)
switch.place(x=300, y=380)


t0 = time.time()
def calculate(*args,**kwargs):
    t1 = time.time()
    st = e.get()
    w_count = len(st.split())
    mylabel = Label(root, text="TOTAL WORDS: " + str(w_count))
    mylabel.place(x=85, y=435)
    mylabel = Label(root, text="TIME TAKEN: " + str(round(t1 - t0)))
    mylabel.place(x=285, y=435)
    if (t1 - t0) >= 60:
        mylabel = Label(root, text="SPEED: POOR")
        mylabel.place(x=513, y=435)
    elif(t1 - t0) >= 30 and (t1 - t0) <= 60:
        mylabel = Label(root, text="SPEED: AVERAGE")
        mylabel.place(x=513, y=435)
    else:
        mylabel = Label(root, text="SPEED: EXCELLENT")
        mylabel.place(x=513, y=435)
btn = Button(root, text="RESULT",bg='black', fg='white', font="helvetica 20", padx=10, pady=10, relief=RAISED, command=calculate)
btn.place(x=550,y=380)
calculate()

root.mainloop()