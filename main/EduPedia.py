from tkinter import *
from tkinter import messagebox
import mysql.connector

## connecting to edupedia database
edupedia = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root1234",
    database = "edupedia"
)
edupedia_cursor = edupedia.cursor()


# Tkinter window
window=Tk()
window.geometry('1280x700')
window.title("home".center(100)) # centering the title ?
window.config(bg="black")

# login
def student():
    frame_login.place_forget()
    frame_stud_log.place(x=200, y=100)
    login(frame_stud_log)

def institute():
    frame_login.place_forget()
    frame_inst_log.place(x=200, y=100)
    login(frame_inst_log)

def company():
    frame_login.place_forget()
    frame_comp_log.place(x=200, y=100)
    login(frame_comp_log)

def validate_account(frame,entry_usr,entry_pwd):
    # cheking which category is loging in
    if frame == frame_stud_log:
        table = "student_login"
    elif frame == frame_inst_log:
        table = "institute_login"
    else:
        table = "company_login"

    # validating account
    sql = f"select * from {table} where user_name = %s and password = %s"
    values = (entry_usr.get(), entry_pwd.get())
    edupedia_cursor.execute(sql, values)
    # collecting the matches from the login table
    results = edupedia_cursor.fetchall()
    # checking if any matches found for given username and password
    if results:
            messagebox.showinfo("success","Login Succesfull")
    # if username and password does not match or exist
    else:
        messagebox.showerror("Failed","Username or password is incorrect")
        

# login window
def login(frame):
    label_usr = Label(frame, text="Enter Username ", bg="yellow", font=("Helvetica", "16"))
    entry_usr = Entry(frame, font=("Helvetica", "16"))
    label_pwd = Label(frame, text="Enter Password ", bg='yellow', font=("Helvetica", "16"))
    entry_pwd = Entry(frame, show="*", font=("Helvetica", "16"))
    v = IntVar(value=0)
    check_pwd = Checkbutton(frame, text="show password", variable=v, onvalue=1, offvalue=0,
                            command=lambda: showpsd(v, entry_pwd))
    button_submit = Button(frame, text="Submit", height=2, width=15, bg="green",command = lambda: validate_account(frame,entry_usr,entry_pwd))
    button_forget = Button(frame, text="forgot password", bg="blue", fg="white")
    button_create = Button(frame, text="Create account", fg="blue")
    button_back = Button(frame, text="back", command=lambda: home(frame))

    label_usr.grid(row=0, column=0, padx=20, pady=20)
    entry_usr.grid(row=0, column=1)
    label_pwd.grid(row=1, column=0)
    entry_pwd.grid(row=1, column=1)
    check_pwd.grid(row=1, column=2, padx=10)
    button_submit.grid(row=2, column=1, pady=10)
    button_forget.grid(row=2, column=2)
    button_create.grid(row=3, column=2)
    button_back.grid(row=5, column=1)


def showpsd(v,entry_pwd):
    if v.get()==1:
        entry_pwd.config(show='')
    else:
        entry_pwd.config(show='*')


def home(frame):
    frame.place_forget()
    frame_login.place(x=350, y=200)


# category frames
frame_login=Frame(window,width=600,height=300,bg="white")
frame_login.place(x=350,y=200)

frame_stud_log = Frame(window, bg="yellow")
frame_inst_log = Frame(window, bg="green")
frame_comp_log = Frame(window, bg="pink")

# category button
button_stud=Button(frame_login,text="student login",bg="blue",fg='white',activebackground="green",font=("Comic Sans MS", 15, "bold"),width=12,command=lambda :student())
button_inst=Button(frame_login,text="institute login",bg="blue",fg='white',activebackground="green",font=("Comic Sans MS", 15, "bold"),width=12,command=lambda :institute())
button_comp=Button(frame_login,text="company login",bg="blue",fg='white',activebackground="green",font=("Comic Sans MS", 15, "bold"),width=12,command=lambda :company())

button_stud.place(x=250,y=25)
button_inst.place(x=250,y=100)
button_comp.place(x=250,y=175)

window.mainloop()
