from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

import mysql.connector

## connecting to edupedia database
# edupedia = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "root1234",
#     database = "edupedia"
# )
# edupedia_cursor = edupedia.cursor()
#

# Tkinter window
window=Tk()
window.geometry('1280x700')
window.title("home".center(100)) # centering the title ?
window.config(bg="black")

# login
def student():
    val='student'
    frame_login.place_forget()
    login(frame_stud_log,val)


def institute():

    val='institute'
    frame_login.place_forget()
    login(frame_inst_log,val)

def company():
    val='company'
    frame_login.place_forget()
    login(frame_comp_log,val)

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
            messagebox.showinfo("success","Login Successful")
            profile(frame)
    # if username and password does not match or exist
    else:
        messagebox.showerror("Failed","Username or password is incorrect")
        

# login window
def login(frame,who):
    def home(frame):
        frame.pack_forget()
        frame_login.place(x=350, y=200)

    frame.pack(side="left", padx=350)
    label_usr = Label(frame, text="Enter Username ", bg="yellow", font=("Helvetica", "16"))
    entry_usr = Entry(frame, font=("Helvetica", "16"))
    label_pwd = Label(frame, text="Enter Password ", bg='yellow', font=("Helvetica", "16"))
    entry_pwd = Entry(frame, show="*", font=("Helvetica", "16"))
    v = IntVar(value=0)
    check_pwd = Checkbutton(frame, text="show password", variable=v, onvalue=1, offvalue=0,
                            command=lambda: showpsd(v, entry_pwd))
    button_submit = Button(frame, text="Submit", height=2, width=15, bg="green",
                           command=lambda:validate_account())

    button_forget = Button(frame, text="forgot password", bg="blue", fg="white")
    button_create = Button(frame, text="Create account", fg="blue", command=lambda: create_uesr(frame,who))
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


def profile(frame):
    frame.pack_forget()

    def search():
        sercch_frame.place(x=200, y=150)

    def close():
        sercch_frame.place_forget()

    def logout():
        frame.pack_forget()
        frame_login.place(x=350, y=200)

    # inside frame
    frame = Frame(window, width=1280, height=700)
    frame.pack()
    top_frame = Frame(frame, width=1280, height=80, bg='green')
    left_frame = Frame(frame, width=220, height=620, bg="black")
    top_icons = Frame(frame, width=1060, bg='brown', height=40, padx=25)
    center_frame = Frame(frame, width=1060, height=580, bg="light blue")
    logo_canvas = Canvas(top_frame, height=80, width=100, )
    logo_canvas.create_text(40, 40, text="logo", fill="black")

    button_logout = Button(top_frame, text="log-out", font=("Comic Sans MS", 12, "bold"), width=6, height=1,
                           command=lambda: logout())

    # left

    profile_text_label = Label(left_frame, font=("Helvetica", "16"), text="My profile", bg="pink", width=18,
                               anchor="nw")
    profile_img = Image.open("resources/profile.jpg")
    profile_img = ImageTk.PhotoImage(profile_img)
    profile_canvas = Canvas(left_frame, height=180, width=220)
    profile_canvas.create_image(0, 0, image=profile_img, anchor='nw')
    profile_name_label = Label(left_frame, font=("Helvetica", "16"), text="name", bg="pink", width=18, anchor='nw')
    view_profile_butt = Button(left_frame, text="view profile", font=("Helvetica", "16"), width=18, height=2,
                               bg="yellow")
    update_profile_butt = Button(left_frame, text="update profile", font=("Helvetica", "16"), width=18, height=2,
                                 bg="orange")
    vlog_butt = Button(left_frame, text="Vlogs", font=("Helvetica", "16"), bg="green", width=18, height=2)
    favorite_butt = Button(left_frame, text="favorites", font=("Helvetica", "16"), bg="light green", width=18, height=2)
    extra_butt = Button(left_frame, text="Extra", font=("Helvetica", "16"), bg="green", width=18, height=2)

    # top_icons

    search_button = Button(top_icons, text="search", bg='white', foreground='blue', font=("Helvetica", "14"), width=13,
                           command=lambda: search())
    vlog_button = Button(top_icons, text="vlogs", bg='white', foreground='blue', font=("Helvetica", "14"), height=1,
                         width=13)
    create_vlog_button = Button(top_icons, text="create vlogs", bg='white', foreground='blue', font=("Helvetica", "14"),
                                height=1, width=13)
    index_button = Button(top_icons, text="index", bg='white', foreground='blue', font=("Helvetica", "14"), height=1,
                          width=13)
    extra_button = Button(top_icons, text="Extra", bg='white', foreground='blue', font=("Helvetica", "14"), height=1,
                          width=13)

    # top frame

    top_frame.place(x=0, y=0)
    left_frame.place(x=0, y=80)
    logo_canvas.place(x=0, y=0)

    button_logout.place(x=1150, y=20)
    top_icons.place(x=225, y=80)
    center_frame.place(x=225, y=120)

    # left frame

    profile_text_label.grid(row=0, column=0)
    profile_canvas.grid(row=1, column=0)
    profile_name_label.grid(row=2, column=0)
    view_profile_butt.grid(row=3, column=0, pady=10)
    update_profile_butt.grid(row=4, column=0)
    vlog_butt.grid(row=5, column=0, pady=10)
    favorite_butt.grid(row=6, column=0)
    extra_butt.grid(row=7, column=0)

    # top icons

    search_button.grid(row=0, column=1, padx=25)
    vlog_button.grid(row=0, column=2, padx=25)
    create_vlog_button.grid(row=0, column=3, padx=20)
    index_button.grid(row=0, column=4, padx=25)
    extra_button.grid(row=0, column=5, padx=25)

    sercch_frame = Frame(center_frame, bg="orange", width=700, height=300)

    search_img = Image.open("resources/search.png")
    search_img = ImageTk.PhotoImage(search_img)
    search_button = Button(sercch_frame, image=search_img, font=("Comic Sans MS", 15, "bold"), anchor='nw', border=0)
    search_Entry = Entry(sercch_frame, font=("Comic Sans MS", 14), width=40)
    close_img = Image.open("resources/close.png")
    close_img = ImageTk.PhotoImage(close_img)
    close_button = Button(sercch_frame, image=close_img, borderwidth=0, command=lambda: close())

    search_button.place(x=540, y=100)
    search_Entry.place(x=50, y=100)
    close_button.place(x=670, y=0)
    window.mainloop()



def create_uesr(frame,who):


    frame.pack_forget()

    def close(f,who):
        frame_create_usr.place_forget()
        login(f,who)

    frame_create_usr = Frame(window, bg='pink', width=500, height=400)

    label_usr = Label(frame_create_usr, text="Enter Username ", bg="yellow", font=("Helvetica", "16"), width=16,
                      anchor='nw')
    entry_usr = Entry(frame_create_usr, font=("Helvetica", "16"))
    label_pwd = Label(frame_create_usr, text="Enter Password ", bg='yellow', font=("Helvetica", "16"), width=16,
                      anchor='nw')
    v = IntVar(value=0)
    check_pwd = Checkbutton(frame_create_usr, text="show password", variable=v, onvalue=1, offvalue=0,
                            command=lambda: showpsd(v, entry_pwd))
    entry_pwd = Entry(frame_create_usr, show="*", font=("Helvetica", "16"))
    label_conpwd = Label(frame_create_usr, text="Conform Password ", bg='yellow', font=("Helvetica", "16"), width=16,
                         anchor='nw')
    entry_conpwd = Entry(frame_create_usr, show="*", font=("Helvetica", "16"))
    label_mob = Label(frame_create_usr, text="Enter Mobile no ", bg="yellow", font=("Helvetica", "16"), width=16,
                      anchor='nw')
    entry_mob = Entry(frame_create_usr, font=("Helvetica", "16"))
    label_email = Label(frame_create_usr, text="Enter Email id", bg="yellow", font=("Helvetica", "16"), width=16,
                      anchor='nw')
    entry_email = Entry(frame_create_usr, font=("Helvetica", "16"))


    if who == 'student':
        entry_collage = Entry(frame_create_usr, font=("Helvetica", "16"))
        label_collge = Label(frame_create_usr, text="Enter Collage name ", bg="yellow", font=("Helvetica", "16"), width=16,
                            anchor='nw')
        label_collge.grid(row=6, column=0, pady=10)
        entry_collage.grid(row=6, column=1)
    elif who=='company':
        entry_company = Entry(frame_create_usr, font=("Helvetica", "16"))
        label_company = Label(frame_create_usr, text="Enter company name", bg="yellow", font=("Helvetica", "16"), width=16,
                            anchor='nw')
        label_company.grid(row=6, column=0, pady=10)
        entry_company.grid(row=6, column=1)
    else:
        entry_institue = Entry(frame_create_usr, font=("Helvetica", "16"))
        label_institue = Label(frame_create_usr, text="Enter institute name", bg="yellow", font=("Helvetica", "16"), width=16,
                            anchor='nw')
        label_institue.grid(row=6, column=0, pady=10)
        entry_institue.grid(row=6, column=1)

    close_button = Button(frame_create_usr, text="X", bg="red", fg="white", width=3, command=lambda: close(frame,who))
    submit_button = Button(frame_create_usr, text="submit", bg="green", fg="yellow", font=("Helvetica", "16"))

    frame_create_usr.place(x=300, y=200)
    close_button.grid(row=0, column=2, sticky='e')
    label_usr.grid(row=1, column=0, pady=10, padx=10)
    entry_usr.grid(row=1, column=1, padx=5)
    label_pwd.grid(row=2, column=0, pady=10)
    entry_pwd.grid(row=2, column=1)
    check_pwd.grid(row=2, column=2, padx=10)
    label_conpwd.grid(row=3, column=0, pady=10)
    entry_conpwd.grid(row=3, column=1)
    label_mob.grid(row=4, column=0, pady=10)
    entry_mob.grid(row=4, column=1)
    label_email.grid(row=5, column=0, pady=10)
    entry_email.grid(row=5, column=1)
    submit_button.grid(row=7, column=1, pady=10)



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
