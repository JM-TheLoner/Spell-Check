from tkinter import *
from textblob import TextBlob

root = Tk()
root.geometry("700x280")
root.title("Spell Checker")
root.config(bg="#CBD6EE")
root.resizable(True, False)

def check_it():
    word = text.get()
    a = TextBlob(word)
    right=str(a.correct())

    cs=Label(root, text="Correct text is :", font=("arial", 15, "bold"), bg="#CBD6EE", fg="#364971")
    cs.place(x=100,y=250)
    spell.config(text=right)

heading = Label(root, text="Spelling Checker", fg="#314877", font=("calibri", 28, "bold"), bg="#CBD6EE").place(x=215, y=30)

text = Entry(root, width=45, border=2, bg="white", font=("arial", 15, "bold"), justify="center")
text.place(x=100, y=80)
text.focus()

check = Button(root, width="8", height="1", bg="red", text="Check", font=("arial", 12, "bold"), fg="white", command=check_it)
check.place(x=295,y=115)

spell = Label(root, fg="#364971", font=("calibri", 23, "bold"), bg="#CBD6EE")
spell.place(x=250, y=240)

mainloop()