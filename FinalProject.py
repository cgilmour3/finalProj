import tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import Menu

def OpenHelpWindow():
    helpWindow = tk.Tk()
    helpWindow.title("Library Help")
    helpWindow.geometry("500x500")
    Textlabel= tk.Label(helpWindow,text="This is a library application, \n you can use it to check in or check out books from the library database.")
    Textlabel.grid(row=0,column=2,padx=5,pady=5)

homeWindow = tk.Tk()
homeWindow.title("Library Home")
homeWindow.geometry("840x410")
homeWindow.config(bg="SpringGreen")
left_frame = Frame(homeWindow,width=200,height=400,bg='lavender')
left_frame.grid(row=0,column=0,padx=10,pady=5)
right_frame = Frame(homeWindow,width=600,height=400,bg='lavender')
right_frame.grid(row=0,column=1,padx=10,pady=5)
menubar = Menu(homeWindow)
filemenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Home", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help",command=OpenHelpWindow)
homeWindow.config(menu=menubar)


homeWindow.mainloop()

