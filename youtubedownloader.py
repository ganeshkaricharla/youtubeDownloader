from pytube import YouTube
from tkinter import *

def downloadYoutube(url, path):
    yt = YouTube(url)
    print("Downloading the Video..+", yt.title)
    display = Label(root, text="Downloading"+yt.title,font=("Verdana", 10))
    display.grid(row=4, column=0, columnspan=2,pady=5)
    yt.streams.first().download(path)
    display.config(text="Download Completed")

root = Tk()
root.geometry("600x300")
root.title('Youtube Downloader')

w = Label(root, text="YOUTUBE Downloader",font=("Verdana", 25),bg="yellow")
w.grid(row=0, column=0, columnspan=2,pady=5)

link = StringVar()
Label(root, text='LINK').grid(row=1,column=0)
linkentry = Entry(root,textvariable= link,width=40,font=("Verdana", 15))
linkentry.grid(row=1,column=1,pady=5)

path  = StringVar()
Label(root, text='FILE PATH').grid(row=2,column=0)
pathentry = Entry(root,textvariable= path,width=40,font=("Verdana", 15))
pathentry.grid(row=2,column=1,pady=5)

button =Button(root, text='DOWNLOAD', command=lambda: downloadYoutube(link.get(),path.get()),font=("Verdana", 15),width=40,bg="red",fg="white")
button.grid(row=3,column=1,columnspan=2,pady=5)

root.mainloop()