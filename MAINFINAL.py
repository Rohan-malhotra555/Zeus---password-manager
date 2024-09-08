from tkinter import *   # Tkinter is a module used to build GUI applications.
import csv              # The csv module implements classes to read and write tabular data in CSV format.
import os.path          # This module is used for different purposes such as for merging, normalizing and retrieving path names in python .
import time             # This module provides various time-related functions.
import os               # This module provides functions for interacting with the operating system.
# Cryptography deals with the encryption of plaintext into ciphertext and decryption of ciphertext into plaintext.
from cryptography.fernet import Fernet

main_window = Tk()      # Creating the main window

winlogo = PhotoImage(file="newlogo.png")  # Loading the logo of the gui.
main_window.iconbitmap("icon1.ico")       # Loading the icon of the gui.
add_detail = PhotoImage(file="adddetails.png")    # Loading the add button image of the gui.
del_detail = PhotoImage(file="deletedetails.png") # Loading the delete button image of the gui.
ac_detail = PhotoImage(file="accessdetails.png")  # Loading the access button image of the gui.
update_detail = PhotoImage(file="update.png")     # Loading the update button image of the gui.
search_img = PhotoImage(file="search.png")# Loading the search button image of the gui.
signup_img = PhotoImage(file="signup.png")# Loading the signup button image of the gui.
login_img = PhotoImage(file="login.png")  # Loading the login button image of the gui.
add_img = PhotoImage(file="addimg.png")   # Loading the add button image of the gui.
delete_img = PhotoImage(file="deleteimg.png")     # Loading the delete button image of the gui.
accountname_img = PhotoImage(file="accountnameimg.png") # Loading the account name image of the gui.
username_img = PhotoImage(file="usernameimg.png") # Loading the username button image of the gui.
password_img = PhotoImage(file="passwordimg.png") # Loading the password button image of the gui.
proceed_img = PhotoImage(file="proceedimg.png")   # Loading the proceed button image of the gui.
previouspg_img = PhotoImage(file = "previous.png")# Loading the previous page button image of the gui.

# Creating a file to store Signup details of the user.
signupDetails = open("SignUpDetails.csv", "a+", newline="")
sudwriter = csv.writer(signupDetails)  # Creating a writer object.
header = ["MAIL", "USERNAME", "PASSWORD", "CPASSWORD"]

file_exists = os.path.isfile("SignUpDetails.csv")
key = b'fD4YCoU9fhHOUbtWd-AjwPddcpD8rppUenkZAo2QY4w='  # Defining a key.
cipher = Fernet(key)

def Mainwindow():                    # Defining a function for the main window.
    # Configuring the window. 
    main_window.title("ZEUS") # Setting the title of the window.
    main_window.geometry("430x600")  # Setting the dimensions of the window.
    main_window.minsize(430, 600)    # Setting the minimum and the 
    main_window.maxsize(430, 600)    # maximum size of the window.
    main_window.config(bg="white")   # Setting the background as white.

    # creating labels and buttons for main window.
    logo = Label(main_window, image=winlogo, width=150, height=125).place(x = 140, y = 40)
    title = Label(main_window, text="PASSWORD MANAGER", font="Arial 25 bold", bg="white").place(x = 25, y = 210)
    sign_in = Button(main_window, image=signup_img, borderwidth=4, font="Arial 15 bold", padx=10, pady=10,
    command=Signup).place(x=125, y=425)
    log_in = Button(main_window, image=login_img, borderwidth=4, font="Arial 15 bold", padx=10, pady=10,
    command=Login).place(x=125, y=300)


def Signup(): # Defining a signup function.
    global mail, username, pass1, pass2, window2, submitdetails_button

    window2 = Toplevel()
    
    # configuring signup window
    window2.title("New Account")
    window2.geometry("430x670")
    window2.minsize(430, 670)
    window2.maxsize(430, 670)
    window2.iconbitmap("icon1.ico")
    window2.config(bg="white")

    def click1(ev1):    # This function is used to change the state of the 
        mail.config(state=NORMAL)  # label to normal when clicked by the user
        mail.delete(0, END)

    def click2(ev2):
        username.config(state=NORMAL)
        username.delete(0, END)

    def click3(ev3):
        pass1.config(state=NORMAL)
        pass1.delete(0, END)

    def click4(ev4):
        pass2.config(state=NORMAL)
        pass2.delete(0, END)

    # LABEL: Tkinter Label is a widget that is used to implement display
    #        boxes where you can place text or images.
    # ENTRY WIDGET: The Entry Widget is a Tkinter Widget used to Enter or
    #        display a single line of text.
    lbl = Label(window2, text="SIGN UP", font="Arial 30 bold", bg="white", fg="black", padx=10
    , pady=20)
    lbl2 = Label(window2, text="MAIL ID", font="Arial 13", bg="white", fg="black")
    mail = Entry(window2, width=45, borderwidth=3)
    lbl3 = Label(window2, text="USERNAME", font="Arial 13", bg="white", fg="black")
    username = Entry(window2, width=45, borderwidth=3)
    lbl4 = Label(window2, text="MASTER PASSWORD", font="Arial 13", bg="white", fg="black")
    pass1 = Entry(window2, width=45, borderwidth=3)
    lbl5 = Label(window2, text="CONFIRM MASTER PASSWORD", bg="white", fg="black"
    , font="Arial 13")
    pass2 = Entry(window2, width=45, borderwidth=3)
    login_acc = Label(window2, text="Already have a account? Login", font="Arial 10 bold", bg='white', fg="black",
    cursor='hand2')

    submitdetails_button = Button(window2, image=signup_img, command=entry_mandat, borderwidth=3, cursor="hand2")

    # Placing all the created labels and the entry widgets in the gui.
    lbl.place(x=122, y=40)  # x = 132, y = 170
    lbl2.place(x=180, y=160)
    mail.place(x=80, y=185, height=30)
    lbl3.place(x=165, y=235)
    username.place(x=80, y=260, height=30)
    lbl4.place(x=130, y=310)
    pass1.place(x=80, y=335, height=30)
    lbl5.place(x=90, y=385)
    pass2.place(x=80, y=410, height=30)
    login_acc.place(x=113, y=565)
    login_acc.bind("<Button-1>", lambda e: Login())
    submitdetails_button.place(x=124, y=480)

    mail.insert(0, "Enter Mail ID...")
    mail.config(state=DISABLED)
    mail.bind("<Button-1>", click1)

    username.insert(0, "Enter Username...")
    username.config(state=DISABLED)
    username.bind("<Button-1>", click2)

    pass1.insert(0, "Enter Password ...")
    pass1.config(state=DISABLED)
    pass1.bind("<Button-1>", click3)

    pass2.insert(0, "Re-enter Password...")
    pass2.config(state=DISABLED)
    pass2.bind("<Button-1>", click4)

def Login(): # Defining a login function.
    global username_check, pass1_check, window2

    window2 = Toplevel()

    def click5(ev5):    # This function is used to change the state of the 
                        # label to normal when clicked by the user.
        username_check.config(state=NORMAL)
        username_check.delete(0, END)

    def click6(ev6):
        pass1_check.config(state=NORMAL)
        pass1_check.delete(0, END)

    # configuring window 2
    window2.title("LOGIN")
    window2.geometry("430x600")
    window2.minsize(430, 600)
    window2.maxsize(430, 600)
    window2.iconbitmap("icon1.ico")
    window2.config(bg="white")

    # creating labels, buttons and entry widgets for login window.
    lbl6 = Label(window2, text="LOGIN", font="Arial 30 bold", bg="white", fg="black", padx=10, pady=20)

    lbl7 = Label(window2, text="USERNAME", font="Arial 13", bg="white", fg="black")
    username_check = Entry(window2, width=45, borderwidth=3)
    lbl8 = Label(window2, text="MASTER PASSWORD", font="Arial 13", bg="white", fg="black")
    pass1_check = Entry(window2, width=45, borderwidth=3)
    Signpage = Label(window2, text="Don't have a account? Create one", font="Arial 10 bold", fg="black", bg="white",
    cursor="hand2")
    submit_userbutton = Button(window2, image=login_img, command=compare_values, borderwidth=3,
    cursor="hand2")

    # Placing all the created labels and the entry widgets in the gui.
    lbl6.place(x=140, y=40)
    lbl7.place(x=165, y=160)
    username_check.place(x=80, y=185, height=30)
    lbl8.place(x=130, y=235)
    pass1_check.place(x=80, y=260, height=30)
    Signpage.place(x=103, y=420)
    Signpage.bind("<Button-1>", lambda e: Signup())
    submit_userbutton.place(x=125, y=330)
    # check_userbutton.place(x = 1000, y = 380)
    username_check.insert(0, "Enter Username...")
    username_check.config(state=DISABLED)
    username_check.bind("<Button-1>", click5)

    pass1_check.insert(0, "Enter Password...")
    pass1_check.config(state=DISABLED)
    pass1_check.bind("<Button-1>", click6)
    # window2.after(20000, lambda: window2.destroy())


def signin_entries():    
    global mail_entry, username_entry, pass1_entry, pass2_entry, signin_entries

    mail_entry = mail.get()
    username_entry = username.get()

    pass1_entry = cipher.encrypt(pass1.get().encode())
    pass2_entry = cipher.encrypt(pass2.get().encode())

    entries = [[mail_entry, username_entry, pass1_entry.decode(), pass2_entry.decode()]]

    sudwriter.writerows(entries)
    signupDetails.flush()


def entry_mandat():     # Defining a function to check whether the password and 
                        # the confirm password are same or not.
    global pass1_entry, pass2_entry, username_entry
    if (mail.get()) and (username.get()) and (pass1.get()) and (pass2.get()):
        
        pass1_entry = (pass1.get().encode())  # Gaining the value of password.
        pass2_entry = (pass2.get().encode())  # Gaining the value of re-entered password.
        
        if pass1_entry == pass2_entry:
            signin_entries()
            ThirdScreen()

        else:

            def destroy():
                errormessage.destroy()  # Removing the error message after sometime.

            # Displaying a message if the passwords do not match.
            errormessage = Label(window2, text="Please Make Sure Your Passwords Match!!", fg="black",
            font="Arial 13 bold", bg="white")
            errormessage.place(x=50, y=610)
            errormessage.after(3000, destroy) # Destroying the message after 3000 seconds.
    else:    # Checking whether the user has filled all the required details.

        def destroy():
            errormessage.destroy()

        errormessage = Label(window2, text="Please Fill In All The Required Details!", fg="black",
        font="Arial 13 bold", bg="white")
        errormessage.place(x=70, y=610)
        errormessage.after(3000, destroy)


def compare_values():    # Defining a function to check whether the values
                         # entered by the user on login page match the signup values.
    global username_entry2, pass1_entry2
    username_entry2 = username_check.get()
    pass1_entry2 = pass1_check.get()
    with open("SignUpDetails.csv", "r") as f:  # opening the file singupdetails.csv

        freader = csv.reader(f)   # creating a reader object

        for rec in freader:

            if freader.line_num == 1: 
                
                # checking if the 2nd element of the record is equal to the 
                # username entered by the user.
                if (rec[1] == username_entry2) and (cipher.decrypt(rec[2].encode()).decode() == pass1_entry2):
                    # if true then creating the third screen
                    ThirdScreen()
            
                elif (rec[1] != username_entry2) and (rec[2] == pass1_entry2):
                    
                    # Displaying this message if the username entered is not correct.
                    errormessage1 = Label(window2, text = "Username Is Incorrect!", fg = "black",
                    font = "Arial 13 bold", bg = "white")
                    errormessage2 = Label(window2, text = "Please Try Again!", fg = "black",
                    font = "Arial 13 bold",bg = "white")

                    def destroy():
                        errormessage1.destroy() # Destroying the error
                        errormessage2.destroy() # messages after 3 seconds.

                    errormessage1.place(x = 120, y = 500)
                    errormessage2.place(x = 140, y = 530)
                    errormessage1.after(3000, destroy)
                    errormessage2.after(3000, destroy)

                elif (rec[1] == username_entry2) and (rec[2] != pass1_entry2):
                    
                    # Displaying this message if the password entered is not correct.
                    errormessage1 = Label(window2, text = "Password Is Incorrect!", fg = "black",
                    font = "Arial 13 bold", bg = "white")
                    errormessage2 = Label(window2, text = "Please Try Again!", fg = "black",
                    font = "Arial 13 bold", bg = "white")

                    def destroy():
                        errormessage1.destroy()
                        errormessage2.destroy()

                    errormessage1.place(x = 120, y = 500)
                    errormessage2.place(x = 140, y = 530)
                    errormessage1.after(3000, destroy)
                    errormessage2.after(3000, destroy)

                elif (rec[1] != username_entry2) and (rec[2] != pass1_entry2):
                    
                    # Displaying this message if both the username
                    # and password entered is not correct.
                    errormessage1 = Label(window2, text = "Password And Username Both Are Incorrect!", 
                    fg = "black", bg = "white", font = "Arial 13 bold")
                    errormessage2 = Label(window2, text = "Please Try Again!", fg = "black", 
                    font = "Arial 13 bold", bg ="white")

                    def destroy():
                        errormessage1.destroy() # removing the messages 
                        errormessage2.destroy() # after 3 seconds.
                    errormessage1.place(x = 35, y = 500)
                    errormessage2.place(x = 140, y = 530)
                    errormessage1.after(3000, destroy)
                    errormessage2.after(3000, destroy)


def ThirdScreen():   # Defining the function for third screen.
    global window3
    window2.destroy()  # Destroying the window 2 when window 3 is created.
    window3 = Toplevel()
    window3.title("WINDOW 3")
    window3.geometry("620x670")
    window3.minsize(620, 670)
    window3.maxsize(620, 670)
    window3.iconbitmap("icon1.ico")
    window3.title("TASKS")
    window3.config(bg="white")

    # creating labels and buttons for third window.
    Lbl = Label(window3, text="Hey ", font="Arial 25 bold", bg="white", fg="black")
    lbl = Label(window3, text="WHAT WOULD YOU LIKE TO DO", font="Arial 23 bold",
    bg="white", fg="black")

    lbl1 = Label(window3, text="ADD ACCOUNT", font="Arial 15",
    bg="white", fg="black")
    add_acd = Button(window3, image=add_detail, command=lambda: click(1)
    , borderwidth=3, cursor="hand2")
    lbl2 = Label(window3, text="DELETE ACCOUNT", font="Arial 15",
    bg="white", fg="black")
    del_acd = Button(window3, image=del_detail, command=lambda: click(2),
    borderwidth=3, cursor="hand2")
    lbl3 = Label(window3, text="ACCESS ACCOUNTS", font="Arial 15",
    bg="white", fg="black")
    ac_acd = Button(window3, image=ac_detail, command=lambda: click(3)
    , borderwidth=3, cursor="hand2")
    lbl4 = Label(window3, text="UPDATE ACCOUNTS", font="Arial 15",
    bg="white", fg="black")
    update_acd = Button(window3, image=update_detail, command=lambda: click(4)
    , borderwidth=3,
    cursor="hand2")

    # Placing all the created labels and the entry widgets in the gui.
    Lbl.pack(side=TOP, pady=60)
    lbl.place(x=65, y=140)
    lbl1.place(x=100, y=270)
    add_acd.place(x=127, y=320)
    lbl2.place(x=350, y=270)
    del_acd.place(x=387, y=320)
    lbl3.place(x=73, y=460)
    ac_acd.place(x=127, y=510)
    lbl4.place(x=350, y=460)
    update_acd.place(x=387, y=510)


def FourthScreenadd():   # Defining a function for the fourth screen.

    global accountdetail, name, password, cpassword

    window3.destroy()  # destroying window 3 on creation of window 4.
    window4 = Toplevel()

    # configuring window 4.
    window4.geometry("620x690")
    window4.title("NEW ACCOUNT")
    window4.iconbitmap("icon1.ico")
    window4.minsize(620, 690)
    window4.maxsize(620, 690)
    window4.configure(background="white")
    CPassword = Entry(window4, width=45)

    # opening the file userdetails in order to add new account.
    file = open("userdetails.csv", "a+", newline="")
    filewriter = csv.writer(file)

    def add():   # defining the add function.
 
        global errormessage, accountdetail, name, password, cpassword
                    
        # obtaining the values of all entry widgets using
        # the .get() function.
        accountdetail = AccountID.get()
        name = Username.get()
        password = Password.get()
        cpassword = CPassword.get()
                    
        # checking if the password and confirm password
        # entry widgets have same value.
        if password == cpassword:

            details = [[accountdetail, name, cipher.encrypt(password.encode()).decode()]]
            filewriter.writerows(details)
            file.flush() # flushing the data into the file.

            def destroy():
                message.destroy()

            message = Label(window4, text="ACCOUNT ADDED",
            font="Arial 13 bold", fg="black", bg="white")
            message.place(x=237, y=610)
            message.after(4000, destroy)
            file.close()

        else:   # Displaying this message if the passwords
                # do not match.
            def destroy():
                errormessage.destroy()

            errormessage = Label(window4, text="Please Make Sure That Your Passwords Match!"
            , font="Arial 13 bold", fg="black", bg="white")
            errormessage.place(x=130, y=610)
            errormessage.after(3000, destroy)
                
    def prevpg():    # Defining a function to go to the previous page.
        window4.destroy()
        ThirdScreen()

    # creating labels, buttons and entry widgets for fourth window.
    header = Label(window4, text="ADD ACCOUNT", font="Arial 25 bold",
    bg="white", fg="black").place(x=190, y=90)
    label1 = Label(window4, text="ACCOUNT", font="Arial 15",
    bg="white", fg="black")
    AccountID = Entry(window4, width=45, borderwidth=3)
    label2 = Label(window4, text="USERNAME", font="Arial 15",
    bg="white", fg="black")
    Username = Entry(window4, width=45, borderwidth=3)
    label3 = Label(window4, text="PASSWORD", font="Arial 15",
    bg="white", fg="black")
    Password = Entry(window4, width=45, borderwidth=3)
    label4 = Label(window4, text="CONFIRM PASSWORD", font="Arial 15",
    bg="white", fg="black")
    CPassword = Entry(window4, width=45, borderwidth=3)
    Add = Button(window4, image=add_img, borderwidth=3, cursor="hand2",
    command=add, pady=20, padx=20)
    previouspg = Button(window4, image = previouspg_img, command = prevpg,borderwidth=3, cursor='hand2')
    previouspg.place(x = 5, y = 5)


    def click1(event):  # Functin for the placeholder
        AccountID.config(state=NORMAL)
        AccountID.delete(0, END)

    def click2(event):  # Function for the placeholder
        Username.config(state=NORMAL)
        Username.delete(0, END)

    def click3(event):  # Function for the placeholder
        Password.config(state=NORMAL)
        Password.delete(0, END)

    def click4(event):  # Function for the placeholder
        CPassword.config(state=NORMAL)
        CPassword.delete(0, END)

    # Placeholders 
    AccountID.insert(0, "Enter Account Name...") 
    AccountID.config(state=DISABLED)
    AccountID.bind("<Button-1>", click1)  
    Username.insert(0, "Enter Username...")
    Username.config(state=DISABLED)
    Username.bind("<Button-1>", click2)
    Password.insert(0, "Enter Password...")
    Password.config(state=DISABLED)
    Password.bind("<Button-1>", click3)
    CPassword.insert(0, "Re-enter Password...")
    CPassword.config(state=DISABLED)
    Password.bind("<Button-1>", click4)

    # Placing all the created labels and the entry widgets in the gui.
    label1.place(x=260, y=180)
    AccountID.place(x=180, y=210, height=30)
    label2.place(x=253, y=260)
    Username.place(x=180, y=290, height=30)
    label3.place(x=250, y=340)
    Password.place(x=180, y=370, height=30)
    label4.place(x=205, y=420)
    CPassword.place(x=180, y=450, height=30)
    Add.place(x=253, y=520)


def FourthScreendelete(): # Defining a function for the fourth screen.
                
    window3.destroy() # destroying window 3 on creation of window 4.
    window4 = Toplevel()

    # configuring window 4.
    window4.title("DELETE ACCOUNT")
    window4.geometry("620x650")
    window4.minsize(620, 650)
    window4.maxsize(620, 650)
    window4.iconbitmap("icon1.ico")
    window4.configure(background="white")

    header = Label(window4, text="DELETE ACCOUNT", font="Arial 25 bold",
    bg="white", fg="black").place(x=160, y=60)

    def delete(): # defining the delete function.
                    
        # opening the file userdetails.csv
        file = open("userdetails.csv", "r")
        filereader = csv.reader(file)
        nfile = open("newuserdetails.csv", "w+", newline="")
        nfilewriter = csv.writer(nfile)

        # obtaining the value of userinput
        userinput_entry = userinput.get()
        found = False

        for rec in filereader:
                        
            # checking if the 1st value of record is
            # equal to the userinput_entry
            if rec[0] == userinput_entry:
                            found = True

            else:
                nfilewriter.writerow(rec)

        file.close()  # closing both 
        nfile.close() # the files.

        if found == False:

            def destroy():
                l1.destroy()

            # displaying this message is no account 
            # is found with the entered name.
            l1 = Label(window4, text="No Account Found",
            font="Arial 15 bold", bg="white", fg="black")
            l1.place(x=227, y=380)
            l1.after(3000, destroy)

        else:
            def destroy1():
                l.destroy()

            l = Label(window4, text="The Account Has Been Deleted.", font="Arial 15 bold",
            bg="white", fg="black")
            l.place(x=160, y=380)
            l.after(3000, destroy1)

        os.remove("userdetails.csv") # removing the file userdetails.csv
        # renaming the file newuserdetails.csv as userdetails.csv
        os.rename("newuserdetails.csv", "userdetails.csv")

    def click1(event):  # For the placeholder
        userinput.config(state=NORMAL)
        userinput.delete(0, END)
                
    def prevpg():  # function to go back to the previous page
        window4.destroy() # first destroying the window 4
        ThirdScreen()  # then calling the third window again

    # creating entry widgets and buttons for fourth window.
    deletebutton = Button(window4, image=delete_img, command=delete
    ,borderwidth=3).place(x=225, y=280)
    previouspg = Button(window4, image = previouspg_img, command = prevpg,borderwidth=3, cursor='hand2')
    previouspg.place(x = 5, y = 5)
    userinput = Entry(window4, width=80, borderwidth=3)
    userinput.place(x=80, y=150, height=35)
    userinput.insert(0, "Enter Account Name...")
    userinput.config(state=DISABLED)
    userinput.bind("<Button-1>", click1)  # placeh



def FourthScreenaccess(): # Defining a function for the fourth screen.

    global search

    window3.destroy() # destroying window 3 on creation of window 4.
    window4 = Toplevel()

    # configuring window 4.
    window4.title("ACCESS ACCOUNTS")
    window4.geometry("620x650")
    window4.minsize(620, 650)
    window4.maxsize(620, 650)
    window4.iconbitmap("icon1.ico")
    window4.configure(background="white")

    def access(): # defining the access function.

        global record
        # opening the function userdetails.csv
        file = open("userdetails.csv", "r", newline="\r\n")
        filereader = csv.reader(file)
        found = False

        userinput_entry = userinput.get()

        for rec in filereader:

            # checking whether 1st value of record
            # is equal to the userinput entry.
            if rec[0] == userinput_entry:
                found = True
                account = rec[0]
                name = rec[1]
                password = cipher.decrypt(rec[2].encode()).decode()
                record = [account, name, password]

                # creating labels for fourth window.
                label = Label(window4, text=account,
                font="Arial 15", bg="white", fg="black")
                label.place(x=340, y=300)
                label1 = Label(window4, text=name,
                font="Arial 15", bg="white", fg="black")
                label1.place(x=340, y=340)
                label2 = Label(window4, text=password,
                font="Arial 15", bg="white", fg="black")
                label2.place(x=340, y=380)
                label3 = Label(window4, text="ACCOUNT :",
                font="Arial 15 bold", bg="white", fg="black")
                label3.place(x=200, y=300)
                label4 = Label(window4, text="USERNAME :",
                font="Arial 15 bold", bg="white", fg="black")
                label4.place(x=200, y=340)
                label5 = Label(window4, text="PASSWORD:",
                font="Arial 15 bold", bg="white", fg="black")
                label5.place(x=200, y=380)

                def destroy0():
                    label.destroy()

                def destroy1():
                    label1.destroy()

                def destroy2():
                    label2.destroy()

                def destroy3():
                    label3.destroy()

                def destroy4():
                    label4.destroy()

                def destroy5():
                    label5.destroy()
                            
                # destroying the labels after 7 seconds.
                label.after(7000, destroy0)
                label1.after(7000, destroy1)
                label2.after(7000, destroy2)
                label3.after(7000, destroy3)
                label4.after(7000, destroy4)
                label5.after(7000, destroy5)

        if found == False:

            def Destroy1():
                l.destroy()

            l = Label(window4, text="No Records Found!!", fg="black",
            font="Arial 15 bold", bg="white")
            l.place(x=205, y=500)
            l.after(3000, Destroy1)
        else:
            pass

        file.close() # closing the file.

    def click1(event):  # For the placeholder
        userinput.config(state=NORMAL)
        userinput.delete(0, END)

    def prevpg():
        window4.destroy()
        ThirdScreen()

    # creating labels and buttons for fourth window.
    header = Label(window4, text="ACCESS ACCOUNTS", font="Arial 25 bold",
    bg="white", fg="black").place(x=145, y=60)
    previouspg = Button(window4, image = previouspg_img, command = prevpg,borderwidth=3, cursor='hand2')
    previouspg.place(x = 5, y = 5)
    search = Button(window4, image=search_img, command=access
    , borderwidth=3).place(x=43, y=159.5)

    userinput = Entry(window4, width=80, borderwidth=3)
    userinput.place(x=80, y=160, height=35)  # 470, 260
    userinput.insert(0, "Enter Account Name...")
    userinput.config(state=DISABLED)
    userinput.bind("<Button-1>", click1)  # placeholder



def FourthScreenupdate(): # Defining a function for the fourth screen.
    
    global newfile

    window3.destroy() # destroying window 3 on creation of window 4.
    window4 = Toplevel()

    # configuring window 4.
    window4.title("UPDATE ACCOUNT DETAILS")
    window4.geometry("620x650")
    window4.minsize(620, 650)
    window4.maxsize(620, 650)
    window4.iconbitmap("icon1.ico")
    window4.configure(background="white")

    lbl4 = Label(window4, text="UPDATE ACCOUNT", font="Arial 25 bold",
    bg="white", fg="black").place(x=160, y=60)

    def update():  # defining the update function.

        global listofcontent
        listofcontent = []
        found = False
        with open("userdetails.csv", "r") as file:
            content = csv.reader(file)
            for rec in content:
                listofcontent.append(rec)

        userinput_entry = userinput.get()

        for rec in listofcontent:
                        
            # checking if the 1st value of record is
            # equal to the userinput_entry
            if rec[0] == userinput_entry:

                label1 = Label(window4, text="Select Which Field Needs To Be Updated",
                font="Arial 15 bold", bg="white", fg="black")
                label1.place(x=125, y=270)
                found = True

                def click2(event):  # For the placeholder
                    newvalue.config(state=NORMAL)
                    newvalue.delete(0, END)

                def click3(event):  # For the placeholder
                    newvalue2.config(state=NORMAL)
                    newvalue2.delete(0, END)

                def click4(event):  # For the placeholder
                    newvalue3.config(state=NORMAL)
                    newvalue3.delete(0, END)

                def accountname(): # Defining this function if
                                    # the user wants to edit account name.
                    global newvalue
                    label1.destroy()
                    b1.destroy()
                    b2.destroy()
                    b3.destroy()
                    previouspg.destroy()

                    def prevpg1():
                        window4.destroy()
                        FourthScreenupdate()

                    previouspg1 = Button(window4, image = previouspg_img, command = prevpg1,borderwidth=3, cursor='hand2')
                    previouspg1.place(x = 5, y = 5)
                            
                    newvalue = Entry(window4, width=50, borderwidth=3)
                    newvalue.place(x=165, y=250, height=35)
                    newvalue.insert(0, "Enter New Account Name...")
                    newvalue.config(state=DISABLED)
                    newvalue.bind("<Button-1>", click2)

                    def acc():
                        global listofcontent
                        file = open("userdetails.csv", "r")
                        nv = newvalue.get()
                                
                        def destroy1():
                            message.destroy()

                        for rec in listofcontent:

                            if rec[0] == userinput_entry:
                                rec[0] = nv  # Setting the new value.
                                file.close()

                        file = open("userdetails.csv", "w+", newline="")
                        filewriter = csv.writer(file)
                        filewriter.writerows(listofcontent)
                        file.close()
                        message = Label(window4, text="Account Name Updated", font="Arial 15 bold",
                        fg="black", bg="white")
                        message.place(x=205, y=440)
                        message.after(3000, destroy1)
                                                          
                    button1 = Button(window4, image=proceed_img, command=acc,
                    borderwidth=3, bg="white",
                    font="Arial 15 bold")
                    button1.place(x=220, y=350, height=40)

                def username():  # Defining this function if
                                             # the user wants to edit username.
                    global newvalue2
                    label1.destroy()
                    b1.destroy()
                    b2.destroy()
                    b3.destroy()
                    previouspg.destroy()

                    def prevpg1():
                        window4.destroy()
                        FourthScreenupdate()

                    previouspg1 = Button(window4, image = previouspg_img, command = prevpg1,borderwidth=3, cursor='hand2')
                    previouspg1.place(x = 5, y = 5)

                    newvalue2 = Entry(window4, width=50, borderwidth=3)
                    newvalue2.place(x=165, y=250, height=35)
                    newvalue2.insert(0, "Enter New Username...")
                    newvalue2.config(state=DISABLED)
                    newvalue2.bind("<Button-1>", click3)

                    def uname():

                        global listofcontent
                        file = open("userdetails.csv", "r")
                        nv = newvalue2.get()

                        def destroy1():
                            message.destroy()

                        for rec in listofcontent:
                            if rec[0] == userinput_entry:
                                rec[1] = nv
                                file.close()

                        file = open("userdetails.csv", "w+", newline="")
                        filewriter = csv.writer(file)
                        filewriter.writerows(listofcontent)
                        file.close()
                        message = Label(window4, text="Username Updated", font="Arial 15 bold",
                        fg="black", bg="white")
                        message.place(x=225, y=440)
                        message.after(3000, destroy1)

                    button1 = Button(window4, image=proceed_img, command=uname,
                    borderwidth=3, bg="white",
                    font="Arial 15 bold").place(x=220, y=350, height=40)

                def password(): # Defining this function if
                                # the user wants to edit password.
                    global newvalue3
                    label1.destroy()
                    b1.destroy()
                    b2.destroy()
                    b3.destroy()
                    previouspg.destroy()

                    def prevpg1():
                        window4.destroy()
                        FourthScreenupdate()

                    previouspg1 = Button(window4, image = previouspg_img, command = prevpg1,borderwidth=3, cursor='hand2')
                    previouspg1.place(x = 5, y = 5)

                    newvalue3 = Entry(window4, width=50, borderwidth=3)
                    newvalue3.place(x=165, y=250, height=35)
                    newvalue3.insert(0, "Enter New Password...")
                    newvalue3.config(state=DISABLED)
                    newvalue3.bind("<Button-1>", click4)

                    def pw():
                        global listofcontent
                        file = open("userdetails.csv", "r")
                        nv = newvalue3.get()

                        def destroy1():
                            message.destroy()

                        for rec in listofcontent:

                            if rec[0] == userinput_entry:
                                rec[2] = cipher.encrypt(nv.encode()).decode()
                                file.close()

                        file = open("userdetails.csv", "w+", newline="")
                        filewriter = csv.writer(file)
                        filewriter.writerows(listofcontent)
                        file.close()
                        message = Label(window4, text="Password Updated", font="Arial 15 bold",
                        fg="black", bg="white")
                        message.place(x=225, y=440)
                        message.after(3000, destroy1)

                    button1 = Button(window4, image=proceed_img, command=pw,
                    borderwidth=3, bg="white",
                    font="Arial 15 bold").place(x=220, y=350, height=40)
                            
                # adding buttons to the fourth window
                b1 = Button(window4, image=accountname_img, command=accountname
                , borderwidth=3, font="Arial 15 bold", bg="white")
                b1.place(x=195, y=340, height=40)
                b2 = Button(window4, image=username_img, command=username
                , borderwidth=3, font="Arial 15 bold", bg="white")
                b2.place(x=220, y=400, height=40)
                b3 = Button(window4, image=password_img, command=password
                , borderwidth=3, font="Arial 15 bold", bg="white")
                b3.place(x=218, y=460, height=40)

        if found == False:
            def destroy2():
                lb.destroy()

            # displaying this message if no record is found.
            lb = Label(window4, text="Record Not Found!", font="Arial 15 bold",
            fg="black", bg="white")
            lb.place(x=220, y=500)
            lb.after(3000, destroy2)
        else:
            pass

    def click1(event):  # For the placeholder
        userinput.config(state=NORMAL)
        userinput.delete(0, END)
                
    def prevpg():
        window4.destroy()
        ThirdScreen()
                
    # adding buttons and entry widgets to the gui.
    search = Button(window4, image=search_img, command=update
    , borderwidth=3).place(x=50, y=150)
    previouspg = Button(window4, image = previouspg_img, command = prevpg,borderwidth=3, cursor='hand2')
    previouspg.place(x = 5, y = 5)
    userinput = Entry(window4, width=80, borderwidth=3)
    userinput.place(x=89, y=150, height=35)
    userinput.insert(0, "Enter Account Name...")
    userinput.config(state=DISABLED)
    userinput.bind("<Button-1>", click1)

def click(args):
    if args == 1:
        FourthScreenadd()

    elif args == 2:
        FourthScreendelete()

    elif args == 3:
        FourthScreenaccess()

    elif args == 4:
        FourthScreenupdate()

Mainwindow()

main_window.mainloop()
