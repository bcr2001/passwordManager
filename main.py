from tkinter import *
import time

# This fucntion is executed if the username and password are correct
def commandWindow():
    global authentication_image
   
    myCommandWindow = Toplevel()
    
    myCommandWindow.title("Central Command")
    myCommandWindow.geometry("650x450")
    myCommandWindow.config(bg="black")
    myCommandWindow.iconphoto(False, PhotoImage(
        file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\password.png"))

    authentication_image = PhotoImage(file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\checkmeResized.png")
    authentication_label = Label(myCommandWindow,text="Welcome To the Authentication Window",font=("Dubai",20),image=authentication_image,compound=LEFT,fg="white",bg="black")
    authentication_label.pack()



    myCommandWindow.resizable(False,False)
    myCommandWindow.mainloop()

   
    


def rejection():
    global sorry_image
    global wUsername_Image
    rejectionWindow = Toplevel()

    rejectionWindow.title("Invalid Credentials")
    rejectionWindow.iconphoto(False, PhotoImage(
        file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\stop.png"))
    rejectionWindow.config(bg="white")
    rejectionWindow.geometry("350x350")

    sorry_image = PhotoImage(
        file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\sorryResized.png")

    sorryImage_label = Label(rejectionWindow, image=sorry_image, bg="white")
    sorryImage_label.pack()

    wUsername_Image = PhotoImage(
        file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\access-deniedResized.png")

    wUsername_label = Label(rejectionWindow, text="Access Denied", image=wUsername_Image,
                            compound=RIGHT, bg="white", font=("Dubai", 20, "bold"))

    wUsername_label.pack(side=BOTTOM)


def logInHandler():

    # getting entry field data
    entered_username = userName_entry.get()
    entered_password = password_entry.get()

    infoFileOpener = open(
        "C:\\Users\\Hx101X\\Desktop\\informationFile\\user1.txt", "r")
    readInfo = infoFileOpener.read()
    infoList = readInfo.split(",")
    realUserName = infoList[0]
    realpassword = infoList[1]

    if (entered_username != realUserName and entered_password != realpassword):
        rejection()
    else:
        commandWindow()



def mainTkinterWindow():
    global myMainWindow

    myMainWindow = Tk()
    myMainWindow.title("INFO")
    myMainWindow.iconphoto(False, PhotoImage(
        file="C:\\Users\\Hx101X\\Desktop\\passwordManager\\Images\\password.png"))
    myMainWindow.config(bg="Black")
    myMainWindow.geometry("650x450")

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
    userName_label = Label(userName_frame, text="Secret Username", font=(
        "Century Schoolbook", 18, "bold"), image=secretImage, compound=RIGHT, bg="black", fg="white")
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
    logIn_Button.place(x=350, y=350)

    myMainWindow.resizable(False, False)
    myMainWindow.mainloop()


if __name__ == "__main__":
    mainTkinterWindow()
