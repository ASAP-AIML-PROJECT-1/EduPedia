
from tkinter import *


window=Tk()
window.geometry('1280x700')
window.title("home".center(100)) #centering the title ?
window.config(bg="black")


# student_login

def std():
    frame_login.place_forget()
    frame_stud_log.place(x=350,y=200)


def showpsd():
    if v.get()==1:
        entry_pwd.config(show='')
    else:
        entry_pwd.config(show='*')


def home():
    frame_stud_log.place_forget()
    frame_login.place(x=350, y=200)


# login frame

frame_login=Frame(window,width=600,height=300,bg="white")
frame_login.place(x=350,y=200)

# login button
button_stud=Button(frame_login,text="student login",bg="blue",fg='white',activebackground="green",font=("Comic Sans MS", 15, "bold"),width=12,command=lambda :std())
button_inst=Button(frame_login,text="institute login",bg="blue",fg='white',activebackground="green",font=("Comic Sans MS", 15, "bold"),width=12,command=lambda :std())
button_comp=Button(frame_login,text="company login",bg="blue",fg='white',activebackground="green",font=("Comic Sans MS", 15, "bold"),width=12,command=lambda :std())

button_stud.place(x=250,y=25)
button_inst.place(x=250,y=100)
button_comp.place(x=250,y=175)

# student login

# student login

frame_stud_log=Frame(window,bg="yellow")
label_usr=Label(frame_stud_log,text="Enter Username ",bg="yellow",font=("Helvetica", "16"))
entry_usr=Entry(frame_stud_log,font=("Helvetica", "16"))
label_pwd=Label(frame_stud_log,text="Enter Password ",bg='yellow',font=("Helvetica", "16"))
entry_pwd=Entry(frame_stud_log,show="*",font=("Helvetica", "16"))
v=IntVar(value=0)
check_pwd=Checkbutton(frame_stud_log,text="show password",variable=v,onvalue=1,offvalue=0,command=lambda :showpsd())
button_submit=Button(frame_stud_log,text="Submit",height=2,width=15,bg="green")
button_forget=Button(frame_stud_log,text="forgot password",bg="blue",fg="white")
button_create=Button(frame_stud_log,text="Create account",fg="blue")
button_back=Button(frame_stud_log,text="back",command=lambda :home())

label_usr.grid(row=0,column=0,padx=20,pady=20)
entry_usr.grid(row=0,column=1)
label_pwd.grid(row=1,column=0)
entry_pwd.grid(row=1,column=1)
check_pwd.grid(row=1,column=2,padx=10)
button_submit.grid(row=2,column=1,pady=10)
button_forget.grid(row=2,column=2)
button_create.grid(row=3,column=2)
button_back.grid(row=5,column=1)



window.mainloop()
