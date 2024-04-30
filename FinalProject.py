import tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import Menu

#creating Help Window
def OpenHelpWindow():
    helpWindow = tk.Tk()
    helpWindow.title("Library Help")
    helpWindow.geometry("500x500")
    Textlabel= tk.Label(helpWindow,text="-This is a library application \n -you can use it to check in or check out books from the library database.\n -Use the check out button to check out a book.\n -Use the Return button to return a book you have checked out.\n")
    Textlabel.grid(row=0,column=2,padx=5,pady=5)


    

#creating mailing list function
def AddMailingList():

    # "submitting" mailing info by writing it to a file stored as a dictionary
    def SubmitForm():
        name = nameEntry.get()
        email = emailEntry.get()
        MailUser = {"name":name,"email":email}
        messagebox.showinfo(title="Mailing list addtion successful",message=f" User entered name: {name} and email: {email}.")
        f = open("EmailList.txt","a")
        f.write("\n")
        f.write(str(MailUser))
        f.close

    #building out mailing list window
    MailingListWindow = tk.Tk()
    MailingListWindow.title("Add to the Mailing List")
    MailingListWindow.geometry("300x300")
    nameLabel = tk.Label(MailingListWindow,text="Name:")
    nameEntry = tk.Entry(MailingListWindow)
    emailLabel = tk.Label(MailingListWindow,text="Email:")
    emailEntry = tk.Entry(MailingListWindow)
    submitButton = tk.Button(MailingListWindow,text="Submit",width=15,command=SubmitForm)
    submitButton.grid(row=2,column=1,columnspan=2,padx=10,pady=10)
    nameEntry.grid(row=0,column=1,padx=10,pady=10)
    emailEntry.grid(row=1,column=1,padx=10,pady=10)
    nameLabel.grid(row=0,column=0,padx=10,pady=10)
    emailLabel.grid(row=1,column=0,padx=10,pady=10)

    

#building out home window
homeWindow = tk.Tk()
homeWindow.title("Library Home")
homeWindow.geometry("840x410")
homeWindow.resizable(False,False)
homeWindow.config(bg="SpringGreen")

#breaking home window into 2 frames, left_frame and right_frame
left_frame = Frame(homeWindow,width=200,height=400,bg='lavender')
left_frame.grid_rowconfigure(4,weight=1)
left_frame.grid_columnconfigure(4,weight=1)
left_frame.grid_propagate(False)
left_frame.grid(row=0,column=0,padx=10,pady=5)
right_frame = Frame(homeWindow,width=600,height=400,bg='lavender')
right_frame.grid_rowconfigure(1,weight=1)
right_frame.grid_columnconfigure(1,weight=1)
right_frame.grid(row=0,column=1,padx=10,pady=5)
right_frame.grid_propagate(False)

#building menu bar
menubar = Menu(homeWindow)
filemenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Home", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Help",command=OpenHelpWindow)
homeWindow.config(menu=menubar)

#adding title to right_frame
right_frame_title = tk.Label(right_frame,text="Books",font=20,bg="lavender")

right_frame_title.grid(row=0,column=1,padx=5,pady=5)
right_frame_title.grid_rowconfigure(1,weight=1)
right_frame_title.grid_columnconfigure(1,weight=1)

#adding title to left_frame
left_frame_title = tk.Label(left_frame,text="Book News",font=20,bg='lavender')
left_frame_title.grid(row=0,column=1,padx=5,pady=5)
left_frame_title.grid_rowconfigure(1,weight=1)
left_frame_title.grid_columnconfigure(1,weight=1)

newsLabel = tk.Label(left_frame,text="New books available for checkout!\n Titles include:\n Harry Potter\nLord of the Rings\nnonfiction works\n and many many more!\nWe also have manga!",bg='lavender')
newsLabel.grid(row=1,column=1,padx=5,pady=5)
mailingList = tk.Label(left_frame,text="Click here to subscribe to our\n mailing list!",bg='lavender')
mailingList.grid(row=2,column=1,padx=5,pady=5)
mailingButton = tk.Button(left_frame,text="Click",command=AddMailingList)
mailingButton.grid(row=3,column=1,padx=5,pady=5)
homeWindow.mainloop()

