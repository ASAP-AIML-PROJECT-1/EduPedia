from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector

# connecting to edupedia database
# edupedia = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "root1234",
#     database = "edupedia"
# )
# edupedia_cursor = edupedia.cursor()


# Tkinter window
window = Tk()
window.geometry('1280x700')
window.title("home".center(100))  # centering the title ?
window.config(bg="black")


# login
def student(s):
    user = s
    frame_login.place_forget()
    print(frame_stud_log)
    login(frame_stud_log,user)

def institute(i):
    user = i
    frame_login.place_forget()
    login(frame_inst_log,user)

def company(c):
    user = c
    frame_login.place_forget()
    login(frame_comp_log,user)

# validating username and password
def validate_account(frame, entry_usr, entry_pwd,user):
    # cheking which category is loging in
    if user == "student":
        table = "student_login"
    elif user == "institute":
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
        messagebox.showinfo("success", "Login Successful")
        profile(frame,entry_usr.get(),user)
    # if username and password does not match or exist
    else:
        messagebox.showerror("Failed", "Username or password is incorrect")

def forget(frame):

    def recovery_mail(entry_mail):
        if entry_mail.get() == "":
            messagebox.showerror("Oops..!","Enter mail adddress")
        else:
            messagebox.showinfo("Success",f"Recovery mail has been sent to \"{entry_mail.get()}\"")

    frame.pack_forget()
    frame_forget = Frame(window, bg="red", width=700, height=300)
    frame_forget.place(x=350, y=200)

    label_mail = Label(frame_forget, text="Enter mail address ", bg="yellow", font=("Helvetica", "16"))
    entry_mail = Entry(frame_forget, font=("Helvetica", "16"))
    button_submit = Button(frame_forget, text="Send recovery mail", height=2, width=15, bg="yellow",command= lambda: recovery_mail(entry_mail))

    label_mail.grid(row=0, column=0, padx=20, pady=20)
    entry_mail.grid(row=0, column=1, padx=20, pady=20)
    button_submit.grid(row=1, column=1, pady=20)


# login window
def login(frame,user):
    def home(frame):
        frame.pack_forget()
        frame_login.place(x=350, y=200)

    frame.pack(side="left", padx=350)
    label_usr = Label(frame, text="Enter Username ", bg="yellow", font=("Helvetica", "16"))
    entry_usr = Entry(frame, font=("Helvetica", "16"))
    label_pwd = Label(frame, text="Enter Password ", bg='yellow', font=("Helvetica", "16"))
    entry_pwd = Entry(frame, show="*", font=("Helvetica", "16"))
    v = IntVar(value=0)
    check_pwd = Checkbutton(frame, text="show password", variable=v, onvalue=1, offvalue=0, command=lambda: showpsd(v, entry_pwd))
    button_submit = Button(frame, text="Submit", height=2, width=15, bg="green", command=lambda: validate_account(frame, entry_usr, entry_pwd,user))
    button_forget = Button(frame, text="forgot password", bg="blue", fg="white", command= lambda : forget(frame))
    button_create = Button(frame, text="Create account", fg="blue", command=lambda: create_uesr(frame,user))
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


def showpsd(v, entry_pwd):
    if v.get() == 1:
        entry_pwd.config(show='')
    else:
        entry_pwd.config(show='*')


def profile(frame,username,user):
    frame.pack_forget()
    def update_profile(frame,username,user):
        def save_profile():
            messagebox.showinfo("Success","Profile updated succesfully")
            frame_update_profile.place_forget()
            profile(frame, username,user)

        def cancel():
            frame_update_profile.place_forget()
            profile(frame, username, user)

        update_value = []
        update_column = []
        frame.pack_forget()
        frame_update_profile = Frame(window, bg="red")
        print(frame_update_profile)
        frame_update_profile.pack()
        frame_update_profile.place(x=350, y=50)

        label_Name = Label(frame_update_profile, text="Name ", bg="yellow", font=("Helvetica", "16"))
        entry_Name = Entry(frame_update_profile, font=("Helvetica", "16"))
        label_email = Label(frame_update_profile, text="email ", bg="yellow", font=("Helvetica", "16"))
        entry_email = Entry(frame_update_profile, font=("Helvetica", "16"))
        label_phone_number = Label(frame_update_profile, text="Phone number ", bg="yellow", font=("Helvetica", "16"))
        entry_phone_number = Entry(frame_update_profile, font=("Helvetica", "16"))
        label_address = Label(frame_update_profile, text="Address ", bg="yellow", font=("Helvetica", "16"))
        entry_address = Entry(frame_update_profile, font=("Helvetica", "16"))

        button_submit = Button(frame_update_profile, text="save", height=2, width=15, bg="yellow",command= lambda: save_profile())
        button_cancel = Button(frame_update_profile, text="cancel", height=2, width=15, bg="yellow",command= lambda: cancel())


        if user == "student":
            label_college = Label(frame_update_profile, text="College ", bg="yellow", font=("Helvetica", "16"))
            entry_college = Entry(frame_update_profile, font=("Helvetica", "16"))
            label_course = Label(frame_update_profile, text="Course ", bg="yellow", font=("Helvetica", "16"))
            entry_course = Entry(frame_update_profile, font=("Helvetica", "16"))
            label_interested_areas = Label(frame, text="Interested areas ", bg="yellow", font=("Helvetica", "16"))
            entry_interested_areas = Entry(frame, font=("Helvetica", "16"))

            label_college.grid(row=4, column=0, padx=20, pady=20)
            entry_college.grid(row=4, column=1, padx=20, pady=20)
            label_course.grid(row=5, column=0, padx=20, pady=20)
            entry_course.grid(row=5, column=1, padx=20, pady=20)
            label_interested_areas.grid(row=6, column=0, padx=20, pady=20)
            entry_interested_areas.grid(row=6, column=1, padx=20, pady=20)

        elif user == "institute":
            label_courses_offered = Label(frame_update_profile, text="Courses Offered ", bg="yellow", font=("Helvetica", "16"))
            entry_courses_offered = Entry(frame_update_profile, font=("Helvetica", "16"))
            label_courses_offered.grid(row=4, column=0, padx=20, pady=20)
            entry_courses_offered.grid(row=4, column=1, padx=20, pady=20)
        else:
            label_services_offered = Label(frame_update_profile, text="Services Providing ", bg="yellow", font=("Helvetica", "16"))
            entry_services_offered = Entry(frame_update_profile, font=("Helvetica", "16"))
            label_services_offered.grid(row=4, column=0, padx=20, pady=20)
            entry_services_offered.grid(row=4, column=1, padx=20, pady=20)


        label_Name.grid(row=0, column=0, padx=20, pady=20)
        entry_Name.grid(row=0, column=1, padx=20, pady=20)
        label_email.grid(row=1, column=0, padx=20, pady=20)
        entry_email.grid(row=1, column=1, padx=20, pady=20)
        label_phone_number.grid(row=2, column=0, padx=20, pady=20)
        entry_phone_number.grid(row=2, column=1, padx=20, pady=20)
        label_address.grid(row=3, column=0, padx=20, pady=20)
        entry_address.grid(row=3, column=1, padx=20, pady=20)

        button_submit.grid(row=8, column=1, pady=20)
        button_cancel.grid(row=8, column=0, pady=20)


    def search():
        sercch_frame.place(x=200, y=150)

    def close():
        sercch_frame.place_forget()

    def logout():
        print(frame)
        frame.pack_forget()
        frame_login.place(x=350, y=200)

    # index


    def index():


            # index in profile
            index_frame = Frame(frame, bg='white', width=200, height=400)

            def goto():

                def show():

                    close(index_frame)

                    show_frame = Frame(frame, width=800, height=300, bg="white")
                    result_label = Label(show_frame, text="Results", fg="blue")
                    text_widget = Text(show_frame, width=85, height=15, bg='white', pady=20, padx=10)
                    scrollbar = Scrollbar(show_frame)
                    text_widget.config(yscrollcommand=scrollbar.set)
                    scrollbar.config(command=text_widget.yview)
                    close_button = Button(show_frame, text="X", bg="red", fg="white", width=2,
                                          command=lambda: close(show_frame))
                    result_label.grid(row=0, column=0, sticky='w', pady=10, padx=10)
                    close_button.grid(row=0, column=1, pady=10, sticky='w', padx=10)
                    text_widget.grid(row=1, column=0, sticky='w')
                    scrollbar.grid(row=1, column=0, sticky='e')
                    show_frame.place(x=300, y=180)


                    try:
                        index_of_item = list_box_index.curselection()


                        if list_box_index.get(index_of_item) == 'Monday':

                            fact = "Monday.com was founded in 2012[7] by Roy Mann, Eran Kampf and Eran Zinman.[8] By August of that year," \
                                   " the company, then called dapulse, raised $1.5 million in seed funding.[9][10][11] The product was " \
                                   "commercially launched in 2014.[12][13] In June 2016, the company announced the closing of $7.6 million" \
                                   " in a Series A round.[14][11] The round was led by Genesis Partners, with participation from existing " \
                                   "backer Entrée Capital.[11] In April 2017, the company raised $25 million.[15] The round was led by New " \
                                   "York-based firm Insight Venture Partners, with participation from existing Series A investors Genesis " \
                                   "Partners and Entrée Capital.[16] In November 2017, the company changed its brand name from dapulse to" \
                                   " Monday.com.[17]In July 2018, the company raised a $50 million Series C funding round.[8] The round was led " \
                                   "by New York-based growth equity firm, Stripes Group, with participation from existing Series A and B investors," \
                                   " Insight Venture Partners and Entrée Capital. In July 2019, the company announced it raised a $150 million Series D" \
                                   " round, bringing total funding to $234.1 million. The round was led by Sapphire Ventures with participation from Hamilton" \
                                   " Lane, HarbourVest Partners, ION Crossover Partners and Vintage Investment Partners.[4] The funding gave the company" \
                                   " a valuation of $1.9 billion, making it a unicorn.[4] As of 2021, the company reported over it was serving 127,000 customers" \
                                   " across over 200 business verticals.[18][19][20] In May 2020, the company won the 2020 Webby Award for Productivity in the category " \
                                   "Apps, Mobile & Voice.[21][22] In May 2021, the company filed for a U.S. IPO.[23][24] The company went public on June 10, 2021.[25] "
                            text_widget.insert(END, fact)

                        else:
                            fact = "nothing"
                            text_widget.insert(END, fact)
                    except Exception as e:

                        show_frame.place_forget()
                        index()
                        messagebox.showinfo("oops", "select at least one")



                def back(frame):
                    frame.place_forget()
                    index()

                try:
                    index_of_item = list_box_index.curselection()

                    if list_box_index.get(index_of_item) == 'may':
                        list_box_index.delete(0, END)
                        weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
                        for values in weekDays:
                            list_box_index.insert(END, values)
                    else:
                        pass
                except Exception as e:
                    messagebox.showinfo("oops", "select at least one")
                    index_frame.place_forget()

                back_button = Button(index_frame, text="Back", fg="green", bg="yellow",
                                     command=lambda: back(index_frame))
                back_button.grid(row=2, column=0, sticky='e', padx=60)
                show_button = Button(index_frame, text="Show ", bg='blue', fg='white', command=lambda: show())
                show_button.grid(row=2, column=0, pady=10, sticky='e', padx=10)

            def sort_reverse():

                data = list(list_box_index.get(0, END))

                def sort_true():
                    list_box_index.delete(0, END)
                    data.sort()
                    for values in data:
                        list_box_index.insert(END, values)
                    sort_button = Button(index_frame, text="A-Z", bg="red", command=lambda: sort_reverse())
                    sort_button.grid(row=0, column=0, pady=10, sticky='w')

                list_box_index.delete(0, END)
                data.sort(reverse=True)
                for values in data:
                    list_box_index.insert(END, values)
                sort_button = Button(index_frame, text="Z-A", bg="red", command=lambda: sort_true())
                sort_button.grid(row=0, column=0, pady=10, sticky='w')

            index_frame.place(x=830, y=120)
            months = ['january', 'february', 'march', 'april', 'may', 'june',
                      'july', 'august', 'september', 'october', 'november', 'december', 'january', 'february', 'march',
                      'april',
                      'may', 'june',
                      'july', 'august', 'september', 'october', 'november', 'december']
            months.sort()

            sort_button = Button(index_frame, text="Z-A", bg="red", command=lambda: sort_reverse())
            close_button = Button(index_frame, text="X", bg='green', width=2, command=lambda: close(index_frame))
            list_box_index = Listbox(index_frame, width=32, height=10)
            scrollbar_index = Scrollbar(index_frame)
            list_box_index.delete(0, END)
            for values in months:
                list_box_index.insert(END, values)

            goto_button = Button(index_frame, text="Go to", bg='blue', fg='white', command=lambda: goto())

            sort_button.grid(row=0, column=0, pady=10, sticky='w')
            close_button.grid(row=0, column=0, sticky='e')
            list_box_index.grid(row=1, column=0, sticky='w', padx=10)
            scrollbar_index.grid(row=1, column=0, sticky='e')
            list_box_index.config(yscrollcommand=scrollbar_index.set)
            scrollbar_index.config(command=list_box_index.yview)
            goto_button.grid(row=2, column=0, pady=10, sticky='e', padx=10)


    # inside frame
    frame = Frame(window, width=1280, height=700)
    frame.pack()
    top_frame = Frame(frame, width=1280, height=80, bg='green')
    left_frame = Frame(frame, width=220, height=620, bg="black")
    top_icons = Frame(frame, width=1060, bg='brown', height=40, padx=25)
    center_frame = Frame(frame, width=1060, height=580, bg="light blue")
    logo_canvas = Canvas(top_frame, height=80, width=100, )
    logo_canvas.create_text(40, 40, text="logo", fill="black")

    button_logout = Button(top_frame, text="log-out", font=("Comic Sans MS", 12, "bold"), width=6, height=1, command=lambda: logout())

    # left
    profile_text_label = Label(left_frame, font=("Helvetica", "16"), text="My profile", bg="pink", width=18, anchor="nw")
    profile_img = Image.open("resources/profile.jpg")
    profile_img = ImageTk.PhotoImage(profile_img)
    profile_canvas = Canvas(left_frame, height=180, width=220)
    profile_canvas.create_image(0, 0, image=profile_img, anchor='nw')
    profile_name_label = Label(left_frame, font=("Helvetica", "16"), text="name", bg="pink", width=18, anchor='nw')
    view_profile_butt = Button(left_frame, text="view profile", font=("Helvetica", "16"), width=18, height=2, bg="yellow")
    update_profile_butt = Button(left_frame, text="update profile", font=("Helvetica", "16"), width=18, height=2, bg="orange", command= lambda: update_profile(frame,username,user))
    vlog_butt = Button(left_frame, text="Vlogs", font=("Helvetica", "16"), bg="green", width=18, height=2)
    favorite_butt = Button(left_frame, text="favorites", font=("Helvetica", "16"), bg="light green", width=18, height=2)
    extra_butt = Button(left_frame, text="Extra", font=("Helvetica", "16"), bg="green", width=18, height=2)

    # top_icons
    search_button = Button(top_icons, text="search", bg='white', foreground='blue', font=("Helvetica", "14"), width=13, command=lambda: search())
    vlog_button = Button(top_icons, text="vlogs", bg='white', foreground='blue', font=("Helvetica", "14"), height=1, width=13)
    create_vlog_button = Button(top_icons, text="create vlogs", bg='white', foreground='blue', font=("Helvetica", "14"), height=1, width=13)
    index_button = Button(top_icons, text="index", bg='white', foreground='blue', font=("Helvetica", "14"), height=1, width=13)
    extra_button = Button(top_icons, text="Extra", bg='white', foreground='blue', font=("Helvetica", "14"), height=1, width=13)

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

    # seacrh frame
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


def create_uesr(frame,user):
    def creating_account(entry_usr,entry_pwd,entry_conpwd,entry_mob,entry_email,entry_belongs_to):
        account_details = [entry_usr, entry_pwd, entry_mob, entry_email, entry_belongs_to]
        # checking if the passwords are same
        if entry_pwd.get() != entry_conpwd.get():
            messagebox.showerror("Oops...!","Passwords are mismatching")
        else:

            if user == "student":
                table_profile = "student_profile"
                table_login = "student_login"
                column_belongs_to = "college"
            elif user == "institute":
                table_profile = "institute_profile"
                table_login = "institute_login"
                column_belongs_to = "institute_name"
            else:
                table_profile = "company_profile"
                table_login = "company_login"
                column_belongs_to = "company_name"

            # checking if the username exists
            sql_user_names = f"SELECT * FROM {table_login} WHERE user_name = %s"
            values_user_names = (entry_usr.get(),)
            edupedia_cursor.execute(sql_user_names,values_user_names)
            result = edupedia_cursor.fetchall()
            if result:
                messagebox.showerror("Oops","username already exists\nTry another one or Log in to your account with this username")
            else:
                # creating mew user with details provided
                try:
                    sql_profile = f"INSERT INTO {table_profile} (username,email,phone_number,{column_belongs_to}) VALUES (%s,%s,%s,%s)"
                    values_profile = (entry_usr.get(),entry_email.get(),entry_mob.get(),entry_belongs_to.get())
                    sql_login_details = f"INSERT INTO {table_login} (user_name,password) VALUES (%s,%s)"
                    value_login_details = (entry_usr.get(),entry_pwd.get())
                    edupedia_cursor.execute(sql_profile,values_profile)
                    edupedia_cursor.execute(sql_login_details,value_login_details)
                    messagebox.showinfo("Success", "Account created\nLogin and go to update profile to complete your account details")
                    edupedia.commit()
                    frame_create_usr.place_forget()
                    login(frame)

                except Exception as error:
                    messagebox.showerror("Error...!",f"{error}\nPlease contact the administrators")

    def close(frame):
        frame_create_usr.place_forget()
        login(frame,user)

    frame.pack_forget()
    frame_create_usr = Frame(window, bg='pink', width=500, height=400)
    label_usr = Label(frame_create_usr, text="Enter Username ", bg="yellow", font=("Helvetica", "16"), width=16, anchor='nw')
    entry_usr = Entry(frame_create_usr, font=("Helvetica", "16"))
    label_pwd = Label(frame_create_usr, text="Enter Password ", bg='yellow', font=("Helvetica", "16"), width=16, anchor='nw')
    v = IntVar(value=0)
    check_pwd = Checkbutton(frame_create_usr, text="show password", variable=v, onvalue=1, offvalue=0, command=lambda: showpsd(v, entry_pwd))
    entry_pwd = Entry(frame_create_usr, show="*", font=("Helvetica", "16"))
    label_conpwd = Label(frame_create_usr, text="Conform Password ", bg='yellow', font=("Helvetica", "16"), width=16, anchor='nw')
    entry_conpwd = Entry(frame_create_usr, show="*", font=("Helvetica", "16"))
    label_mob = Label(frame_create_usr, text="Enter Mobile no ", bg="yellow", font=("Helvetica", "16"), width=16, anchor='nw')
    entry_mob = Entry(frame_create_usr, font=("Helvetica", "16"))
    label_email = Label(frame_create_usr, text="Enter Email id", bg="yellow", font=("Helvetica", "16"), width=16, anchor='nw')
    entry_email = Entry(frame_create_usr, font=("Helvetica", "16"))
    entry_belongs_to = Entry(frame_create_usr, font=("Helvetica", "16"))
    entry_belongs_to.grid(row=6, column=1)

    if user == "student":
        label_collge = Label(frame_create_usr, text="Enter Collage name ", bg="yellow", font=("Helvetica", "16"), width=16, anchor='nw')
        label_collge.grid(row=6, column=0, pady=10)

    elif user == "institute":
        label_institue = Label(frame_create_usr, text="Enter institute name", bg="yellow", font=("Helvetica", "16"), width=16, anchor='nw')
        label_institue.grid(row=6, column=0, pady=10)
    else:
        label_company = Label(frame_create_usr, text="Enter company name", bg="yellow", font=("Helvetica", "16"), width=16, anchor='nw')
        label_company.grid(row=6, column=0, pady=10)

    close_button = Button(frame_create_usr, text="X", bg="red", fg="white", width=3, command=lambda: close(frame))
    submit_button = Button(frame_create_usr, text="submit", bg="green", fg="yellow", font=("Helvetica", "16"), command= lambda : creating_account(entry_usr,entry_pwd,entry_conpwd,entry_mob,entry_email,entry_belongs_to))

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


# mian frame categories
frame_login = Frame(window, width=600, height=300, bg="white")
frame_login.place(x=350, y=200)

frame_stud_log = Frame(window, bg="yellow")
frame_inst_log = Frame(window, bg="green")
frame_comp_log = Frame(window, bg="pink")

s,i,c = "student","institute","company"

# category button
button_stud = Button(frame_login, text="student login", bg="blue", fg='white', activebackground="green", font=("Comic Sans MS", 15, "bold"), width=12, command=lambda: student(s))
button_inst = Button(frame_login, text="institute login", bg="blue", fg='white', activebackground="green", font=("Comic Sans MS", 15, "bold"), width=12, command=lambda: institute(i))
button_comp = Button(frame_login, text="company login", bg="blue", fg='white', activebackground="green", font=("Comic Sans MS", 15, "bold"), width=12, command=lambda: company(c))

button_stud.place(x=250, y=25)
button_inst.place(x=250, y=100)
button_comp.place(x=250, y=175)

window.mainloop()
