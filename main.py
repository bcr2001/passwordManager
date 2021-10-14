from tkinter import *
import time
from tkinter import messagebox
import database as mydb
from functions import *
from createAccount import *




def create_account_handler():
    new_create_window = Toplevel()
    create_window = CreateAccountWindowCreator(new_create_window)
    new_create_window.geometry("650x450")
    new_create_window.title("Create User")
    new_create_window.iconphoto(False,PhotoImage(file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\createResized.png"))
    # create_window.submission_function_handler()
    new_create_window.resizable(False,False)
    new_create_window.mainloop()



def time_function():
    time_string = time.strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    # date_string = time.strftime("%A")
    # date_label.config(text=date_string)


    myMainWindow.after(1000,time_function)
    


def commandWindow():
    global authentication_image


    global myCommandWindow
    myCommandWindow = Toplevel()

    

    # global date_label
    # date_label = Label(myCommandWindow,bg="black",fg="green",font=("Arial",15,"bold"))
    # date_label.place(x=530,y=0)

    
    myCommandWindow.title("Central Command")
    myCommandWindow.geometry("650x450")
    myCommandWindow.config(bg="black")
    myCommandWindow.iconphoto(False, PhotoImage(
        file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\password.png"))

    # setting button, image, and placement
    setting_image = PhotoImage(file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\adminResized.png")
    setting_button = Button(myCommandWindow,image=setting_image,activebackground="black",activeforeground="white",bg="black",borderwidth=0,cursor="hand2")
    setting_button.place(x=590,y=0)



    myCommandWindow.resizable(False,False)
    myCommandWindow.mainloop()

x = 0 
def logInHandler1(event):
        global x
        x+=1

        # getting entry field data
        entered_username = userName_entry.get()
        entered_password = password_entry.get()

        # database authentication
        results_from_database = mydb.database_authentication(entered_username,entered_password)


        empty = ""

        if (entered_username.lstrip()== empty) or (entered_password == empty):
            popuperrorHandler()
           
        elif results_from_database == False:
            # rejection()
            wrongUserName_Password()
            
        elif results_from_database == True:
            commandWindow()
        
        if x==3:
            myMainWindow.destroy()
      
def logInHandler():
        global x
        x+=1

        # getting entry field data
        entered_username = userName_entry.get()
        entered_password = password_entry.get()

        # database authentication
        results_from_database = mydb.database_authentication(entered_username,entered_password)


        empty = ""

        if (entered_username.lstrip()== empty) or (entered_password == empty):
            popuperrorHandler()
           
        elif results_from_database == False:
            # rejection()
            wrongUserName_Password()
            
        elif results_from_database == True:
            commandWindow()
        
        if x==3:
            myMainWindow.destroy()
     


def mainTkinterWindow():
    global myMainWindow
  

    myMainWindow = Tk()
    myMainWindow.title("INFO")
    myMainWindow.iconphoto(False, PhotoImage(
        file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\lockResized.png"))
    myMainWindow.config(bg="Black")
    myMainWindow.geometry("650x450")

    # this is the time label, it's placement and the functions that does everything 
    global time_label
    time_label = Label(myMainWindow, bg="black", fg="green",
                       font=("Arial", 15, "bold"))
    time_label.place(x=0, y=0)
    time_function()

    # Image positioning
    welcomeImage = PhotoImage(
        file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\welcomeResized.png")
    image_Label = Label(image=welcomeImage, bg="black")
    image_Label.pack()

    # Secret Username frame, Image,labal and entry

    userName_frame = Frame(myMainWindow, bg="black")
    userName_frame.place(x=0, y=150)
    secretImage = PhotoImage(file=(
        "C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\secretResized.png"))  # Image object
    userName_label = Label(userName_frame, text="Username", font=(
        "Century Schoolbook", 18, "bold"),  bg="black", fg="white")
    userName_label.pack(padx=20, side=LEFT)  # label and it's image
    global userName_entry
    userName_entry = Entry(userName_frame, font=("Century Schoolbook", 18))
    userName_entry.pack(side=RIGHT)  # entry box

    # Passwordframe, Image,labal and entry

    password_frame = Frame(myMainWindow, bg="black")
    password_frame.place(x=0, y=250)
    passwordImage = PhotoImage(file=(
        "C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\passwordResized.png"))  # Image object
    password_label = Label(password_frame, text="Password", font=(
        "Century Schoolbook", 18, "bold"), image=passwordImage, compound=RIGHT, bg="black", fg="white")
    password_label.pack(padx=20, side=LEFT)  # label and it's image

    message = Label(password_frame, text="(Password Encryption Activated)", font=(
        "Arial", 10, "bold"), fg="green", bg="black")
    message.pack(side=BOTTOM)

    global password_entry
    password_entry = Entry(password_frame, font=(
        "Century Schoolbook", 18), show="*")
    password_entry.pack(side=RIGHT)  # entry box

    # log in button and it's image

    logIn_image = PhotoImage(
        file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\doorResized.png")

    logIn_Button = Button(myMainWindow, text="log in", font=("Tahoma"), bg="black", fg="white", image=logIn_image, compound=RIGHT,
                          borderwidth=0, activebackground="black", activeforeground="white", cursor="hand2", command=logInHandler)
    logIn_Button.place(x=450, y=350)

    # Create Account Button and it's image
    getting_image = PhotoImage(file="C:\\Users\\Hx101X\Desktop\\passwordManager\\Images\\createResized.png")
    create_Account_button = Button(
        myMainWindow, text="Create Account", font=("Tahoma"),image=getting_image,compound=RIGHT,bg="black",fg="white",activebackground="black",borderwidth=0,cursor="hand2",activeforeground="white",command=create_account_handler)
    create_Account_button.place(x=0,y=370)


    myMainWindow.bind("<Return>",logInHandler1)

    myMainWindow.resizable(False, False)
    myMainWindow.mainloop()


if __name__ == "__main__":
    mainTkinterWindow()
