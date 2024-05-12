import tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import Menu
from datetime import date
import os
#creating Help Window
def OpenHelpWindow():
    helpWindow = tk.Tk()
    helpWindow.title("Library Help")
    helpWindow.geometry("500x500")
    Textlabel= tk.Label(helpWindow,text="-This is a library application \n -you can use it to check in or check out books from the library database.\n -Use the More Info button to open up the book's details.\n -Once that menu opens, click the Check Out button to check out the book!\n")
    Textlabel.grid(row=0,column=2,padx=5,pady=5)


    

#creating mailing list function
def AddMailingList():

    # "submitting" mailing info by writing it to a file stored as a dictionary
    def SubmitForm():
        name = nameEntry.get()
        email = emailEntry.get()
        #need to check for proper name and email
        # if name.isnumeric() == True:
        if '@' in email and '.com' in email:
            MailUser = {"name":name,"email":email}
            messagebox.showinfo(title="Mailing list addtion successful",message=f" User entered name: {name} and email: {email}.")
            path = 'C:/Users/camer/Documents/SDEV140/EmailList.txt'
            isFile = os.path.isfile(path)
            if isFile == True:
                f = open("EmailList.txt","a")
                f.write("\n")
                f.write(str(MailUser))
                f.close
            elif isFile == False:
                f = open("EmailList.txt","w")
                f.write(str(MailUser))
                f.write("\n")
                f.close
        else:
            messagebox.showerror(title="Email Error",message="Error, please enter a proper email.")
        # elif name.isnumeric() == False:
        #     messagebox.showerror(title="Name error",message="Error, name must only contain letters.")
    

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

'''
creating function for building book windows
def BuildBookWindow(image,title,name,desc):


'''
    
def OpenSorcerersStone():
    
    def CheckoutBook():

        
        # bookCheckedOut = { }
        # path = 'C:/Users/camer/Documents/SDEV140/finalProject/CheckedOutList.txt'
        # isFile = os.path.isfile(path)
        # if isFile == True:
        #     f = open("CheckedOutList.txt","a")
        #     f.write("\n")
        #     f.write(str(bookCheckedOut))
        #     f.close
        # elif isFile == False:
        #     f = open("CheckedOutList.txt","w")
        #     f.write(str(bookCheckedOut))
        #     f.write("\n")
        #     f.close

        messagebox.showinfo(title="Success",message="Success! Harry Potter and the Sorcerers Stone has been checked out")

    book1Window = tk.Tk()
    book1Window.title("Book Menu")
    book1Window.geometry("450x450")
    book1Window.resizable(False,False)
    book1Window.config(bg='lavender')
  
   
    book1_label = tk.Label(book1Window,text="Harry Potter and the Sorcerers Stone",bg='lavender')
    book1Author_label = tk.Label(book1Window,text="Author: J.K. Rowling",bg='lavender')
    book1Author_label.grid(row=1,column=1,padx=5,pady=5)
    book1_Title = tk.Label(book1Window,text="Book Info",bg='lavender')
    book1Checkout_button = tk.Button(book1Window,text="Check Out",command=CheckoutBook)
    book1Checkout_button.grid(row=1,column=2,padx=5,pady=5)
    book1_Title.grid(row=0,column=1,padx=5,pady=5)
    book1_label.grid(row=1,column=0,padx=5,pady=5)
    # image = tk.PhotoImage(file="sorcerersStone.png")
    # imageLabel = tk.Label(image=image)
    # imageLabel.grid(row=2,column=1)


def openHobbit():
    
    def CheckoutBook():

        
        # bookCheckedOut = { }
        # path = 'C:/Users/camer/Documents/SDEV140/finalProject/CheckedOutList.txt'
        # isFile = os.path.isfile(path)
        # if isFile == True:
        #     f = open("CheckedOutList.txt","a")
        #     f.write("\n")
        #     f.write(str(bookCheckedOut))
        #     f.close
        # elif isFile == False:
        #     f = open("CheckedOutList.txt","w")
        #     f.write(str(bookCheckedOut))
        #     f.write("\n")
        #     f.close

        messagebox.showinfo(title="Success",message="Success! The Hobbit has been checked out")

    book1Window = tk.Tk()
    book1Window.title("Book Menu")
    book1Window.geometry("450x450")
    book1Window.resizable(False,False)
    book1Window.config(bg='lavender')
  
   
    book1_label = tk.Label(book1Window,text="The Hobbit",bg='lavender')
    book1Author_label = tk.Label(book1Window,text="Author: J. R. R. Tolkein",bg='lavender')
    book1Author_label.grid(row=1,column=1,padx=5,pady=5)
    book1_Title = tk.Label(book1Window,text="Book Info",bg='lavender')
    book1Checkout_button = tk.Button(book1Window,text="Check Out",command=CheckoutBook)
    book1Checkout_button.grid(row=1,column=2,padx=5,pady=5)
    book1_Title.grid(row=0,column=1,padx=5,pady=5)
    book1_label.grid(row=1,column=0,padx=5,pady=5)

def OpenReadyPlayerOne():
    
    def CheckoutBook():

        
        # bookCheckedOut = { }
        # path = 'C:/Users/camer/Documents/SDEV140/finalProject/CheckedOutList.txt'
        # isFile = os.path.isfile(path)
        # if isFile == True:
        #     f = open("CheckedOutList.txt","a")
        #     f.write("\n")
        #     f.write(str(bookCheckedOut))
        #     f.close
        # elif isFile == False:
        #     f = open("CheckedOutList.txt","w")
        #     f.write(str(bookCheckedOut))
        #     f.write("\n")
        #     f.close

        messagebox.showinfo(title="Success",message="Success! Ready Player One has been checked out")

    book1Window = tk.Tk()
    book1Window.title("Book Menu")
    book1Window.geometry("450x450")
    book1Window.resizable(False,False)
    book1Window.config(bg='lavender')
  
   
    book1_label = tk.Label(book1Window,text="Ready Player One",bg='lavender')
    book1Author_label = tk.Label(book1Window,text="Author: Ernest Cline",bg='lavender')
    book1Author_label.grid(row=1,column=1,padx=5,pady=5)
    book1_Title = tk.Label(book1Window,text="Book Info",bg='lavender')
    book1Checkout_button = tk.Button(book1Window,text="Check Out",command=CheckoutBook)
    book1Checkout_button.grid(row=1,column=2,padx=5,pady=5)
    book1_Title.grid(row=0,column=1,padx=5,pady=5)
    book1_label.grid(row=1,column=0,padx=5,pady=5)

def OpenJJK():
    
    def CheckoutBook():

        
        # bookCheckedOut = { }
        # path = 'C:/Users/camer/Documents/SDEV140/finalProject/CheckedOutList.txt'
        # isFile = os.path.isfile(path)
        # if isFile == True:
        #     f = open("CheckedOutList.txt","a")
        #     f.write("\n")
        #     f.write(str(bookCheckedOut))
        #     f.close
        # elif isFile == False:
        #     f = open("CheckedOutList.txt","w")
        #     f.write(str(bookCheckedOut))
        #     f.write("\n")
        #     f.close

        messagebox.showinfo(title="Success",message="Success! Jujutsu Kaisen Volume 1 has been checked out")

    book1Window = tk.Tk()
    book1Window.title("Book Menu")
    book1Window.geometry("450x450")
    book1Window.resizable(False,False)
    book1Window.config(bg='lavender')
  
   
    book1_label = tk.Label(book1Window,text="Jujutsu Kaisen Vol. 1",bg='lavender')
    book1Author_label = tk.Label(book1Window,text="Author: Gege Akutami",bg='lavender')
    book1Author_label.grid(row=1,column=1,padx=5,pady=5)
    book1_Title = tk.Label(book1Window,text="Book Info",bg='lavender')
    book1Checkout_button = tk.Button(book1Window,text="Check Out",command=CheckoutBook)
    book1Checkout_button.grid(row=1,column=2,padx=5,pady=5)
    book1_Title.grid(row=0,column=1,padx=5,pady=5)
    book1_label.grid(row=1,column=0,padx=5,pady=5)


def OpenCSM():
    
    def CheckoutBook():

        
        # bookCheckedOut = { }
        # path = 'C:/Users/camer/Documents/SDEV140/finalProject/CheckedOutList.txt'
        # isFile = os.path.isfile(path)
        # if isFile == True:
        #     f = open("CheckedOutList.txt","a")
        #     f.write("\n")
        #     f.write(str(bookCheckedOut))
        #     f.close
        # elif isFile == False:
        #     f = open("CheckedOutList.txt","w")
        #     f.write(str(bookCheckedOut))
        #     f.write("\n")
        #     f.close

        messagebox.showinfo(title="Success",message="Success! Chansaw Man Volume 1 has been checked out")

    book1Window = tk.Tk()
    book1Window.title("Book Menu")
    book1Window.geometry("450x450")
    book1Window.resizable(False,False)
    book1Window.config(bg='lavender')
  
   
    book1_label = tk.Label(book1Window,text="Chainsaw Man Vol. 1",bg='lavender')
    book1Author_label = tk.Label(book1Window,text="Author: Tatsuki Fujimoto",bg='lavender')
    book1Author_label.grid(row=1,column=1,padx=5,pady=5)
    book1_Title = tk.Label(book1Window,text="Book Info",bg='lavender')
    book1Checkout_button = tk.Button(book1Window,text="Check Out",command=CheckoutBook)
    book1Checkout_button.grid(row=1,column=2,padx=5,pady=5)
    book1_Title.grid(row=0,column=1,padx=5,pady=5)
    book1_label.grid(row=1,column=0,padx=5,pady=5)

def OpenFrieren():
    
    def CheckoutBook():

        
        # bookCheckedOut = { }
        # path = 'C:/Users/camer/Documents/SDEV140/finalProject/CheckedOutList.txt'
        # isFile = os.path.isfile(path)
        # if isFile == True:
        #     f = open("CheckedOutList.txt","a")
        #     f.write("\n")
        #     f.write(str(bookCheckedOut))
        #     f.close
        # elif isFile == False:
        #     f = open("CheckedOutList.txt","w")
        #     f.write(str(bookCheckedOut))
        #     f.write("\n")
        #     f.close

        messagebox.showinfo(title="Success",message="Success! Frieren Beyond Journeys End Volume 1 has been checked out")

    book1Window = tk.Tk()
    book1Window.title("Book Menu")
    book1Window.geometry("450x450")
    book1Window.resizable(False,False)
    book1Window.config(bg='lavender')
  
   
    book1_label = tk.Label(book1Window,text="Frieren Beyond Journeys End Vol. 1",bg='lavender')
    book1Author_label = tk.Label(book1Window,text="Author: Kanehido Yamada",bg='lavender')
    book1Author_label.grid(row=1,column=1,padx=5,pady=5)
    book1_Title = tk.Label(book1Window,text="Book Info",bg='lavender')
    book1Checkout_button = tk.Button(book1Window,text="Check Out",command=CheckoutBook)
    book1Checkout_button.grid(row=1,column=2,padx=5,pady=5)
    book1_Title.grid(row=0,column=1,padx=5,pady=5)
    book1_label.grid(row=1,column=0,padx=5,pady=5)

def OpenApothecaryDiaries():
    
    def CheckoutBook():

        
        # bookCheckedOut = { }
        # path = 'C:/Users/camer/Documents/SDEV140/finalProject/CheckedOutList.txt'
        # isFile = os.path.isfile(path)
        # if isFile == True:
        #     f = open("CheckedOutList.txt","a")
        #     f.write("\n")
        #     f.write(str(bookCheckedOut))
        #     f.close
        # elif isFile == False:
        #     f = open("CheckedOutList.txt","w")
        #     f.write(str(bookCheckedOut))
        #     f.write("\n")
        #     f.close

        messagebox.showinfo(title="Success",message="Success! Chansaw Man Volume 1 has been checked out")

    book1Window = tk.Tk()
    book1Window.title("Book Menu")
    book1Window.geometry("450x450")
    book1Window.resizable(False,False)
    book1Window.config(bg='lavender')
  
   
    book1_label = tk.Label(book1Window,text="Apothecary Diaries Vol. 1",bg='lavender')
    book1Author_label = tk.Label(book1Window,text="Author: Natsu Hyuuga",bg='lavender')
    book1Author_label.grid(row=1,column=1,padx=5,pady=5)
    book1_Title = tk.Label(book1Window,text="Book Info",bg='lavender')
    book1Checkout_button = tk.Button(book1Window,text="Check Out",command=CheckoutBook)
    book1Checkout_button.grid(row=1,column=2,padx=5,pady=5)
    book1_Title.grid(row=0,column=1,padx=5,pady=5)
    book1_label.grid(row=1,column=0,padx=5,pady=5)

def OpenHellsing():
    
    def CheckoutBook():

        
        # bookCheckedOut = { }
        # path = 'C:/Users/camer/Documents/SDEV140/finalProject/CheckedOutList.txt'
        # isFile = os.path.isfile(path)
        # if isFile == True:
        #     f = open("CheckedOutList.txt","a")
        #     f.write("\n")
        #     f.write(str(bookCheckedOut))
        #     f.close
        # elif isFile == False:
        #     f = open("CheckedOutList.txt","w")
        #     f.write(str(bookCheckedOut))
        #     f.write("\n")
        #     f.close

        messagebox.showinfo(title="Success",message="Success! Hellsing Volume 1 has been checked out")

    book1Window = tk.Tk()
    book1Window.title("Book Menu")
    book1Window.geometry("450x450")
    book1Window.resizable(False,False)
    book1Window.config(bg='lavender')
  
   
    book1_label = tk.Label(book1Window,text="Hellsing Vol. 1",bg='lavender')
    book1Author_label = tk.Label(book1Window,text="Author: Kohta Hirano",bg='lavender')
    book1Author_label.grid(row=1,column=1,padx=5,pady=5)
    book1_Title = tk.Label(book1Window,text="Book Info",bg='lavender')
    book1Checkout_button = tk.Button(book1Window,text="Check Out",command=CheckoutBook)
    book1Checkout_button.grid(row=1,column=2,padx=5,pady=5)
    book1_Title.grid(row=0,column=1,padx=5,pady=5)
    book1_label.grid(row=1,column=0,padx=5,pady=5)

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
right_frame.grid_rowconfigure(10,weight=1)
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

#labels and buttons for books in right frame
book1_label = tk.Label(right_frame,text="Harry Potter and the Sorcerers Stone",bg='lavender')
book1_label.grid(row=1,column=0)
book1_button = tk.Button(right_frame,text="More Info",bg='lavender',command=OpenSorcerersStone)
book1_button.grid(row=1,column=1,padx=10,pady=10)

book2_label = tk.Label(right_frame,text="The Hobbit",bg='lavender')
book2_label.grid(row=2,column=0)
book2_button = tk.Button(right_frame,text="More Info",bg='lavender',command=openHobbit)
book2_button.grid(row=2,column=1,padx=10,pady=10)

book3_label = tk.Label(right_frame,text="Ready Player One",bg='lavender')
book3_label.grid(row=3,column=0)
book3_button = tk.Button(right_frame,text="More Info",bg='lavender',command=OpenReadyPlayerOne)
book3_button.grid(row=3,column=1,padx=10,pady=10)

book4_label = tk.Label(right_frame,text="Jujutsu Kaisen Vol. 1",bg='lavender')
book4_label.grid(row=4,column=0)
book4_button = tk.Button(right_frame,text="More Info",bg='lavender',command=OpenJJK)
book4_button.grid(row=4,column=1,padx=10,pady=10)

book5_label = tk.Label(right_frame,text="Chainsaw Man Vol. 1",bg='lavender')
book5_label.grid(row=5,column=0)
book5_button = tk.Button(right_frame,text="More Info",bg='lavender',command=OpenCSM)
book5_button.grid(row=5,column=1,padx=10,pady=10)

book6_label = tk.Label(right_frame,text="Frieren Beyond Journeys End Vol. 1",bg='lavender')
book6_label.grid(row=6,column=0)
book6_button = tk.Button(right_frame,text="More Info",bg='lavender',command=OpenFrieren)
book6_button.grid(row=6,column=1,padx=10,pady=10)

book7_label = tk.Label(right_frame,text="Apothecary Diaries Vol. 1",bg='lavender')
book7_label.grid(row=7,column=0)
book7_button = tk.Button(right_frame,text="More Info",bg='lavender',command=OpenApothecaryDiaries)
book7_button.grid(row=7,column=1,padx=10,pady=10)

book8_label = tk.Label(right_frame,text="Hellsing Vol. 1",bg='lavender')
book8_label.grid(row=8,column=0)
book8_button = tk.Button(right_frame,text="More Info",bg='lavender',command=OpenHellsing)
book8_button.grid(row=8,column=1,padx=10,pady=10)

homeWindow.mainloop()

