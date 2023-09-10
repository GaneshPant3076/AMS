from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os


class Students:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x700+150+50")
        self.root.title("Facial Recognition Attendance")


        #----------variables----------
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_class = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()


        img = Image.open("images/background.jpg")
        img = img.resize((1200,700), Image.ANTIALIAS)
        self.background_img = ImageTk.PhotoImage(img)

        b_img = Label(self.root, image=self.background_img)
        b_img.place(x=0,y=0,width=1200, height=700)

        title_label = Label(b_img, text="Student Management", font=("corbel",36, "bold"),bg="white", fg = "black")
        title_label.place(x=0, y=0, width=1200, height=60)

        main_frame = Frame(b_img,bd=2)
        main_frame.place(x=0, y=60, width=1200, height=640)

        #left label frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,bg="white", text="Student Details",font=("corbel",18, "bold"))
        left_frame.place(x=0, y=0, width=530, height=630)
        
        
        #course frame
        course_frame = LabelFrame(left_frame, bd=2, relief=RIDGE,bg="white", text="Course Detail",font=("corbel",12, "bold"))
        course_frame.place(x=0, y=0, width=530, height=80)

        #department 
        dep_label = Label(course_frame, text= 'Department:',font=("corbel",12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx= 5, sticky=W)

        dep_combo = ttk.Combobox(course_frame, textvariable=self.var_dep, font=("corbel",8, "bold"), width=15,state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "Civil", "Architecture")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        #course 
        course_label = Label(course_frame, text= 'Course:',font=("corbel",12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx= 5, sticky=W)

        course_combo = ttk.Combobox(course_frame,textvariable=self.var_course, font=("corbel",8, "bold"), width=15,state="readonly")
        course_combo["values"] = ("Select Course","BE")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        #year 
        year_label = Label(course_frame, text= 'Year:',font=("corbel",12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx= 5, sticky=W)

        year_combo = ttk.Combobox(course_frame, textvariable=self.var_year, font=("corbel",8, "bold"), width=15,state="readonly")
        year_combo["values"] = ("Select Year", "2018/19", "2019/20", "2020/21", "2021/22", "2022/23")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        #semester 
        sem_label = Label(course_frame, text= 'Semester:',font=("corbel",12, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx= 5, sticky=W)

        sem_combo = ttk.Combobox(course_frame,textvariable=self.var_sem, font=("corbel",8, "bold"), width=15,state="readonly")
        sem_combo["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        #student information frame
        student_frame = LabelFrame(left_frame, bd=2, relief=RIDGE,bg="white", text="Student Information",font=("corbel",12, "bold"))
        student_frame.place(x=0, y=80, width=530, height=515)

        #student ID
        studentId_label = Label(student_frame, text= 'Student ID:',font=("corbel",12, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx= 5, sticky=W)

        studentId_entry = ttk.Entry(student_frame,textvariable=self.var_id, width=15,font=("corbel",12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=5, sticky=W)

        #student name
        studentName_label = Label(student_frame, text= 'Student Name:',font=("corbel",12, "bold"), bg="white")
        studentName_label.grid(row=0, column=2, padx= 5, sticky=W)

        studentName_entry = ttk.Entry(student_frame,textvariable=self.var_name, width=15,font=("corbel",12, "bold"))
        studentName_entry.grid(row=0, column=3, padx=5, sticky=W)

        #class division
        class_label = Label(student_frame, text= 'Class:',font=("corbel",12, "bold"), bg="white")
        class_label.grid(row=1, column=0, padx= 5, pady=10, sticky=W)

        class_entry = ttk.Entry(student_frame,textvariable=self.var_class, width=15,font=("corbel",12, "bold"))
        class_entry.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        #roll no
        roll_label = Label(student_frame, text= 'Roll no.:',font=("corbel",12, "bold"), bg="white")
        roll_label.grid(row=1, column=2, padx= 5, pady=10, sticky=W)

        roll_entry = ttk.Entry(student_frame,textvariable=self.var_roll, width=15,font=("corbel",12, "bold"))
        roll_entry.grid(row=1, column=3, padx=5, pady=10, sticky=W)

        #gender
        gender_label = Label(student_frame, text= 'Gender:',font=("corbel",12, "bold"), bg="white")
        gender_label.grid(row=2, column=0, padx= 5, pady=5, sticky=W)

        gender_combo = ttk.Combobox(student_frame,textvariable=self.var_gender, font=("corbel",8, "bold"), width=17,state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        #dob
        dob_label = Label(student_frame, text= 'DOB:',font=("corbel",12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx= 5, pady=5, sticky=W)

        dob_entry = ttk.Entry(student_frame,textvariable=self.var_dob, width=15,font=("corbel",12, "bold"))
        dob_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        #email
        email_label = Label(student_frame, text= 'E-mail:',font=("corbel",12, "bold"), bg="white")
        email_label.grid(row=3, column=0, padx= 5, pady=5, sticky=W)

        email_entry = ttk.Entry(student_frame,textvariable=self.var_email, width=15,font=("corbel",12, "bold"))
        email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        #phone no
        phone_label = Label(student_frame, text= 'Phone:',font=("corbel",12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx= 5, pady=5, sticky=W)

        phone_entry = ttk.Entry(student_frame,textvariable=self.var_phone, width=15,font=("corbel",12, "bold"))
        phone_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        #address
        address_label = Label(student_frame, text= 'Address:',font=("corbel",12, "bold"), bg="white")
        address_label.grid(row=4, column=0, padx= 5, pady=5, sticky=W)

        address_entry = ttk.Entry(student_frame,textvariable=self.var_address, width=15,font=("corbel",12, "bold"))
        address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        #teacher name
        teacher_label = Label(student_frame, text= 'Teacher:',font=("corbel",12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx= 5, pady=5, sticky=W)

        teacher_entry = ttk.Entry(student_frame,textvariable=self.var_teacher, width=15,font=("corbel",12, "bold"))
        teacher_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        #radio buttons
        self.var_radiobtn1 = StringVar()
        radiobtn1 = ttk.Radiobutton(student_frame, variable=self.var_radiobtn1, text="Take a photo sample", value="Yes")
        radiobtn1.grid(row=5, column=0)
        
        self.var_radiobtn2 = StringVar()
        radiobtn2 = ttk.Radiobutton(student_frame, variable=self.var_radiobtn1, text="No photo sample", value="No")
        radiobtn2.grid(row=5, column=1)

        #button frame
        btn_frame = Frame(student_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=530, height=150)

        #save button
        save_btn = Button(btn_frame, command=self.add_data, text="Save", font=("corbel",12, "bold"))
        save_btn.grid(row=0, column=0, padx= 10, pady=10, sticky=W)

        #update button
        update_btn = Button(btn_frame,command=self.update_data, text="Update", font=("corbel",12, "bold"))
        update_btn.grid(row=0, column=1, padx=10, pady=10, sticky=W)

        #delete button
        delete_btn = Button(btn_frame,command=self.delete_data, text="Delete", font=("corbel",12, "bold"))
        delete_btn.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        #reset button
        reset_btn = Button(btn_frame,command=self.reset_data, text="Reset", font=("corbel",12, "bold"))
        reset_btn.grid(row=1, column=1, padx=10, pady=10, sticky=W)

        #take photo sample
        take_sample_btn = Button(btn_frame, command=self.generate_dataset, text="Take Photo Sample", font=("corbel",12, "bold"))
        take_sample_btn.grid(row=2, column=0, padx=10,pady=10, sticky=W)

        #update photo sample
        update_photo_btn = Button(btn_frame, text="Update Photo Sample", font=("corbel",12, "bold"))
        update_photo_btn.grid(row=2, column=1, padx=10, pady=10, sticky=W)

        
        #right label frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,bg="white", text="Student Details",font=("corbel",18, "bold"))
        right_frame.place(x=530, y=0, width=700, height=630)

        #-------------Search System-------------
        search_frame = LabelFrame(right_frame, bd=2, relief=RIDGE,bg="white", text="Search System",font=("corbel",12, "bold"))
        search_frame.place(x=0, y=0, width=700, height=70)

        search_label = Label(search_frame, text= 'Search:',font=("corbel",12, "bold"), bg="white")
        search_label.grid(row=0, column=0, padx= 5, pady=5, sticky=W)
        
        search_combo = ttk.Combobox(search_frame, font=("corbel",8, "bold"), width=15,state="readonly")
        search_combo["values"] = ("Select", "Roll no.", "Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame, width=20,font=("corbel",12, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)
        
        #search button
        search_btn = Button(search_frame, text="Search", font=("corbel",12, "bold"))
        search_btn.grid(row=0, column=3, padx=5, pady=5, sticky=W)
        
        #showall button
        showall_btn = Button(search_frame, text="Show All", font=("corbel",12, "bold"))
        showall_btn.grid(row=0, column=4, padx=5, pady=5, sticky=W)

        #table frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE,bg="white")
        table_frame.place(x=0, y=70, width=700, height=525)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "class", "roll", "gender", "dob", "email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill= X)
        scroll_y.pack(side=RIGHT, fill= Y)

        scroll_x.config(command=self.table.xview)
        scroll_y.config(command=self.table.yview)

        self.table.heading("dep", text="Department")
        self.table.heading("course", text="Course")
        self.table.heading("year", text="Year")
        self.table.heading("sem", text="Semester")
        self.table.heading("id", text="ID")
        self.table.heading("name", text="Name")
        self.table.heading("class", text="Class")
        self.table.heading("roll", text="Roll No.")
        self.table.heading("gender", text="Gender")
        self.table.heading("dob", text="DOB")
        self.table.heading("email", text="E-mail")
        self.table.heading("phone", text="Phone")
        self.table.heading("address", text="Address")
        self.table.heading("teacher", text="Teacher")
        self.table.heading("photo", text="Photo Sample Status")
        self.table["show"] = "headings"
        
        self.table.column("dep", width=100)
        self.table.column("course", width=100)
        self.table.column("year", width=100)
        self.table.column("sem", width=100)
        self.table.column("id", width=100)
        self.table.column("name", width=100)
        self.table.column("class", width=100)
        self.table.column("roll", width=100)
        self.table.column("gender", width=100)
        self.table.column("dob", width=100)
        self.table.column("email", width=100)
        self.table.column("phone", width=100)
        self.table.column("address", width=100)
        self.table.column("teacher", width=100)
        self.table.column("photo", width=120)
        
        self.table.pack(fill=BOTH, expand=1)
        self.table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    
    #----------function declaration----------
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All fields are required", parent= self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_sem.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_class.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radiobtn1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details have been added successfully!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent= self.root)


    #------------fetch data-------------
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        
        if len(data)!=0:
            self.table.delete(*self.table.get_children())
            for i in data:
                self.table.insert("", END, values=i)
            conn.commit()
        conn.close()

    #----------get cursor--------
    def get_cursor(self, event=""):
        cursor_focus = self.table.focus()
        content = self.table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_class.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radiobtn1.set(data[14])

    #---------update function------------
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All fields are required", parent= self.root)

        else:
            try:
                Update = messagebox.askyesno("Update", "Do you want to update?", parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set dep=%s, course=%s, year=%s, sem=%s, name=%s,class=%s, roll=%s,gender=%s,dob=%s, email=%s,phone=%s,address=%s, teacher=%s,photo=%s where id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_class.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radiobtn1.get(),
                        self.var_id.get()
                    ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Update Completed!", parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    #-----------delete function-------
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error", "Student ID required!", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete", "Confirm Delete?", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where id=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Deleted Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    #----------reset function--------
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_class.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radiobtn1.set("")




    #--------------generate dataset to take photo sample-------------
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "All fields are required", parent= self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id +=1
                my_cursor.execute("update student set dep=%s, course=%s, year=%s, sem=%s, name=%s,class=%s, roll=%s,gender=%s,dob=%s, email=%s,phone=%s,address=%s, teacher=%s,photo=%s where id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_sem.get(),
                        self.var_name.get(),
                        self.var_class.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radiobtn1.get(),
                        self.var_id.get()== id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #-----------load predefined data on face frontals----------
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_crop(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3,5)

                    #scaling factor = 1.3
                    #minimum neighbor = 5

                    for (x,y,w,h) in faces:
                        face_crop = img[y:y+h, x:x+w]
                        return face_crop
                    
                capture = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = capture.read()
                    if face_crop(my_frame) is not None:
                        img_id +=1
                        face = cv2.resize(face_crop(my_frame), (450,450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name, face)
                        cv2.putText(face, str(img_id),(50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating Data Set Completed !", parent= self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
            




if __name__ == "__main__":
    root = Tk()
    obj = Students(root)
    root.mainloop()