from tkinter import *

def login_verify():
    
    username1 = username_verify.get()
    password1 = password_verify.get()
    

def register_user():
    username_info = username.get()
    password_info = password.get()

    file= open(username_info+"txt", "w")
    file.write(username_info+ "/n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    
    Label(screen1, text = "Regisration Success" ,fg = "green" ,font = ("calibri" ,11)) 
    
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    
    global username
    global password
    global username_entry
    global password_entry
    
    username = StringVar()
    password = StringVar()
    
    Label(screen1, text = "Please enter details below").pack()
    Label(screen1, text = "").pack()
    Label(screen1, text = "Username * ").pack()
    global username_entry
    global password_entry
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    Label(screen1, text = "Password * ").pack()
    password_entry = Entry(screen1, textvariable = password)
    password_entry.pack()
    Label(screen1, text = "").pack()
    Button(screen1, text = "Register", width = 10, height = 1).pack()
    

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text = "Please enter details below to login").pack()
    Label(screen2, text = "").pack()

       
    Label(screen2, text = "Username * ").pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    Label(screen2, text = "Password * ").pack()
    password_entry1 = Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    Button(screen2, text = "Login", width = 10, height = 1, command = login_verify).pack()
    
def main_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Notes 1.0")
    Label(text = "Notes 1.0", bg = "grey", width = "300", height = "2", font = ( "Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login", height = "2", width = "300", command = login).pack()
    Label(text = "").pack()
    Button(text = "Register", height = "2", width = "300", command = register).pack()

    screen.mainloop()
    
main_screen()    
