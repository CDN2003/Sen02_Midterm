from tkinter import *
from tkinter import messagebox
import json
import pyttsx3
from difflib import get_close_matches

engine = pyttsx3.init()

def wordaudio():
    wordAudio = engine.getProperty('voices')
    engine.setProperty('voice', wordAudio[0].id)
    engine.say(enterWordEntry.get())
    engine.runAndWait()


def meaningaudio():
    meaningAudio = engine.getProperty('voices')
    engine.setProperty('voice', meaningAudio[1].id)
    engine.say(textArea.get(1.0,END))
    engine.runAndWait()


def iexit():
    end = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if end == True:
        source.destroy()

    else:
        pass


def clear():
    textArea.config(state=NORMAL)
    enterWordEntry.delete(0, END)
    textArea.delete(1.0, END)
    textArea.config(state=DISABLED)


def search():
    info = json.load(open('data.json'))
    word = enterWordEntry.get()

    word = word.lower()

    if word in info:
        meaning = info[word]

        textArea.config(state=NORMAL)
        textArea.delete(1.0, END)
        for item in meaning:
            textArea.insert(END, u'\u2022' + " " + item + '\n\n')

        textArea.config(state=DISABLED)

    elif len(get_close_matches(word, info.keys())) > 0:

        match = get_close_matches(word, info.keys())[0]

        con = messagebox.askyesno('Confirm', 'Did you mean ' + match + ' instead?')
        enterWordEntry.delete(0, END)
        if con == True:
            textArea.config(state=NORMAL)
            enterWordEntry.insert(END, match)
            meaning = info[match]
            textArea.delete(1.0, END)
            #textArea.config(state=DISABLED)
            for item in meaning:
                textArea.insert(END, u'\u2022' + " " + item + '\n\n')

            textArea.config(state=DISABLED)

        else:
            textArea.config(state=NORMAL)
            textArea.delete(1.0, END)
            messagebox.showinfo('Information', 'Please type a correct word.')
            enterWordEntry.delete(0, END)
            textArea.config(state=DISABLED)
    else:
        messagebox.showerror('Error', 'The word does not exist. Please double check it.')
        messagebox.config()
        enterWordEntry.delete(0, END)


source = Tk()
source.geometry('1000x626+100+50')
sourceImage = PhotoImage(file='iconsTotoro.png')
source.iconphoto(False, sourceImage)
source.title('Talking Dictionary created by Flores, Munoz, and Salem')
source.resizable(0, 0)

bgImage = PhotoImage(file='libBG.png')
bgLabel = Label(source, image=bgImage)
bgLabel.place(x=0, y=0)


enterWordImage = PhotoImage(file='wordBG-removebg-preview.png')
bgWordImage = Label(source, image=enterWordImage, bg='whitesmoke')
bgWordImage.place(x=455, y=20)

enterWordEntry = Entry(source, font=('arial', 23, 'bold'), fg='white', bg='sienna4', bd=8, relief=GROOVE, justify=CENTER)
enterWordEntry.place(x=335, y=80)
enterWordEntry.focus_set()

searchImage = PhotoImage(file='searchBtn.png')
searchButton = Button(source, image=searchImage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                      command=search)
searchButton.place(x=445, y=150)

micImage = PhotoImage(file='micBtn.png')
micButton = Button(source, image=micImage, bd=0, bg='whitesmoke', activebackground='whitesmoke',
                   cursor='hand2',command=wordaudio)
micButton.place(x=540, y=150)


meaningLabel = PhotoImage(file='meaningBG-removebg-preview.png')
bgMeaningLabel = Label(source, image=meaningLabel, bg='whitesmoke')
bgMeaningLabel.place(x=457, y=225)

textArea = Text(source, font=('arial', 14, 'normal'), fg='white', bg='sienna4', height=10, width=50, bd=8, relief=GROOVE, wrap='word')
textArea.place(x=227, y=280)

audioImage = PhotoImage(file='micBtn.png')
audioButton = Button(source, image=audioImage, bd=0, bg='whitesmoke', activebackground='whitesmoke',
                     cursor='hand2',command=meaningaudio)
audioButton.place(x=395, y=530)

clearImage = PhotoImage(file='clearBtn.png')
clearButton = Button(source, image=clearImage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2'
                     , command=clear)
clearButton.place(x=495, y=530)

exitImage = PhotoImage(file='exitBtn.png')

exitButton = Button(source, image=exitImage, bd=0, bg='whitesmoke', 
activebackground='whitesmoke', cursor='hand2', command=iexit)

exitButton.place(x=595, y=530)



source.mainloop()
