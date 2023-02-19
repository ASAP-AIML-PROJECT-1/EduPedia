    def create_blog(frame,username,user):

        def submit_create_blog():
            sql_submit_blog = f"INSERT INTO blogs (username,author_name,category,blog_name,blog,tags) VALUES (%s,%s,%s,%s,%s,%s)"
            create_blog_values = (username, author_name_entry.get(), category_entry.get(), blog_name_entry.get(), blog_text_value,tags_entry.get())
            edupedia_cursor.execute(sql_submit_blog,create_blog_values)
            edupedia.commit()
            messagebox.showinfo("Success","Your blog has been uploaded succesfully")
            close(create_blog_frame)


        create_blog_frame=Frame(frame,width=800,height=550,bg="black")

        author_name_label = Label(create_blog_frame, text="author_name", font=("Helvetica", "16"), fg='white', bg="black",anchor="nw",width=15)
        author_name_entry = Entry(create_blog_frame, font=("Helvetica", "16"),width=50)
        category_label = Label(create_blog_frame, text="category", font=("Helvetica", "16"), fg='white', bg="black",anchor="nw",width=15)
        category_entry = Entry(create_blog_frame, font=("Helvetica", "16"),width=50)
        blog_name_label = Label(create_blog_frame, text="blog_name", font=("Helvetica", "16"), fg='white',
                                  bg="black",anchor="nw",width=15)
        blog_name_entry = Entry(create_blog_frame, font=("Helvetica", "16"),width=50)
        blog_label = Label(create_blog_frame, text="blog", font=("Helvetica", "16"), fg='white', bg="black",anchor="nw",width=15)
        blog_text = Text(create_blog_frame, font=("Helvetica", "16"),width=50,height=5)
        blog_text_value = blog_text.get(1.0, "end-1c")
        tags_label = Label(create_blog_frame, text="tags", font=("Helvetica", "16"), fg='white',
                                bg="black",anchor="nw",width=15)
        tags_entry = Entry(create_blog_frame, font=("Helvetica", "16"),width=50)
        close_button = Button(create_blog_frame, text="X",bg="red", width=2,command=lambda: close(create_blog_frame))
        create_button=Button(create_blog_frame,text="Create",bg="green", command= lambda : submit_create_blog())


        create_blog_frame.place(x=300,y=150)

        close_button.grid(row=0,column=2,sticky='w',pady=5,padx=10)
        author_name_label.grid(row=2,column=0)
        author_name_entry.grid(row=2,column=1)
        category_label.grid(row=3,column=0,pady=20)
        category_entry.grid(row=3,column=1)
        blog_name_label.grid(row=4,column=0)
        blog_name_entry.grid(row=4,column=1)
        blog_label.grid(row=5,column=0,pady=20)
        blog_text.grid(row=5,column=1,pady=20)
        tags_label.grid(row=6,column=0)
        tags_entry.grid(row=6,column=1)
        create_button.grid(row=8,column=1,pady=20)
