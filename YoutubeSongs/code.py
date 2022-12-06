import pywhatkit
from tkinter import * 
root = Tk()
root.title("Youtube Songs")
root.geometry('500x300')
def playsongs():
    s=song.get()
    pywhatkit.playonyt(s)
heading=Label(root,text='Youtube Songs',font=('bold',20)).place(x=190,y=50)
label=Label(root,text="Enter the name of the song: ",font=('bold',15)).place(x=150,y=100)
song=StringVar()
song_name=Entry(root,textvariable=song,bd=5)
song_name.place(x=150,y=150)
gobutton=Button(root,text='GO',width=12,command=playsongs)
gobutton.place(x=200,y=200)
root.mainloop()