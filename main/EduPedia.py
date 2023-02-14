from tkinter import *
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


# login window
def login(frame):
    label_usr=Label(frame,text="Enter Username",)
    entry_usr=Entry(frame)
    label_pwd=Label(frame,text="Enter Password")
    entry_pwd=Entry(frame,show="*")
    v=IntVar(value=0)
    check_pwd=Checkbutton(frame,variable=v,onvalue=1,offvalue=0,command=lambda :showpsd())
    button_submit=Button(frame,text="Submit")
    button_forget=Button(frame,text="forgot password")
    button_create=Button(frame,text="Create account")
    button_back=Button(frame,text="back",command=lambda :home(frame))

    label_usr.grid(row=0,column=0)
    entry_usr.grid(row=0,column=1)
    label_pwd.grid(row=1,column=0)
    entry_pwd.grid(row=1,column=1)
    check_pwd.grid(row=1,column=2)
    button_submit.grid(row=2,column=1)
    button_forget.grid(row=3,column=1)
    button_create.grid(row=4,column=1)
    button_back.grid(row=5,column=1)


def showpsd():
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

frame_stud_log=Frame(window,bg="yellow")
frame_inst_log=Frame(window,bg="green")
frame_comp_log=Frame(window,bg="pink")

# category button
button_stud=Button(frame_login,text="student login",bg="blue",fg='white',activebackground="green",font=("Comic Sans MS", 15, "bold"),width=12,command=lambda :student())
button_inst=Button(frame_login,text="institute login",bg="blue",fg='white',activebackground="green",font=("Comic Sans MS", 15, "bold"),width=12,command=lambda :institute())
button_comp=Button(frame_login,text="company login",bg="blue",fg='white',activebackground="green",font=("Comic Sans MS", 15, "bold"),width=12,command=lambda :company())

button_stud.place(x=250,y=25)
button_inst.place(x=250,y=100)
button_comp.place(x=250,y=175)

window.mainloop()
