from tkinter import*
import random
import string

ALONE = Tk()
ALONE.geometry("300x200")
ALONE.resizable(0,0)
ALONE.title("Make PassWord")

passwordstring = StringVar()
password_lenght = IntVar()

#function to generate the password
def get_password():
    password1 = string.ascii_letters+string.digits+string.punctuation
    password=""

    for i in range(password_lenght.get()): #loop to generate the user given length for password 
        password=password+ random.choice(password1)
        passwordstring.set(password)

#tkinter COMMAND to generate the gui 
Label(ALONE,text="Password Generator",font="calibri 18 bold ",fg="#0203E2").pack()
Label(ALONE,text="Enter Length of Password",fg="#0203E2").pack(pady=9)
Entry(ALONE,textvariable=password_lenght, fg="#0203E2").pack(pady=2)
Button(ALONE,text="Generate Password",command=get_password,fg="#0203E2").pack(pady=15)
Entry(ALONE,textvariable=passwordstring , fg="#0203E2").pack(pady=2)

ALONE.mainloop()
