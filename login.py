from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Students
import mysql.connector
import os
from train import Train
from recognition import Recognition
from attendance import Attendance
import tkinter
from tkinter import messagebox
from main import Facial_Recognition


def main():
    win = Tk()
    app = Login(win)
    win.mainloop()

class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x700+150+50")
        self.root.title("Login")

        img = Image.open("images/login.jpg")
        img = img.resize((1200,700), Image.ANTIALIAS)
        self.background_img = ImageTk.PhotoImage(img)

        b_img = Label(self.root, image=self.background_img)
        b_img.place(x=0,y=0,width=1200, height=700)


        frame = Frame(self.root, bg = "black")
        frame.place(x=400,y=100,width=400, height=500)

        img1 = Image.open("images/user.png")
        img1 = img1.resize((100,100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        labelimg1 = Label(image=self.photoimage1, bg="black",borderwidth=0)
        labelimg1.place(x=550,y=120,width=100, height=100)


        log_in = Label(frame, text="Login", font=("corbel",24, "bold"),bg="black", fg = "white")
        log_in.place(x=157, y=120)

        #-----------username-------------
        username = Label(frame, text="Username:",font=("corbel",15, "bold"),bg="black", fg = "white")
        username.place(x=10, y=200)

        self.username_entry = ttk.Entry(frame,font=("corbel",12, "bold"))
        self.username_entry.place(x=120,y=200, width=270)

        #-----------password-------------
        password = Label(frame, text="Password:",font=("corbel",15, "bold"),bg="black", fg = "white")
        password.place(x=10, y=250)

        self.password_entry = ttk.Entry(frame,font=("corbel",12, "bold"))
        self.password_entry.place(x=120,y=250, width=270)


        #----------login button---------
        login_btn = Button(frame, text="Login",command= self.login,font=("corbel",15, "bold"), bd=3, relief=RIDGE,bg="blue", fg = "white", activeforeground="white", activebackground="blue")
        login_btn.place(x=147, y=350, width=100, height=35)

        #----------register button----------
        reg_btn = Button(frame, text="Register", command=self.reg_window,font=("corbel",15, "bold"), borderwidth=0, relief=RIDGE,bg="black", fg = "white", activeforeground="white", activebackground="black")
        reg_btn.place(x=10, y=400)


    def reg_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


    def login(self):
        if self.username_entry.get()=="" or self.password_entry.get()=="":
            messagebox.showerror("Error", "All fields required!", parent=self.root)
        elif self.username_entry.get()=="kabiraj" and self.password_entry.get()=="kabiraj123":
            messagebox.showinfo("Success", "Login Successful!")

        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s", (
                                                                                        self.username_entry.get(),
                                                                                        self.password_entry.get()
            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid username and password!")
            else:
                open_main = messagebox.askyesno("Yes or No", "Access only admin?")
                if open_main>0:
                    self.new_window = Toplevel(self.root)
                    self.app= Facial_Recognition(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

            

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1200x700+150+50")

        #-----------vairables----------
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_email=StringVar()
        self.var_contact=StringVar()
        self.var_sec_question=StringVar()
        self.var_sec_ans=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        img = Image.open("images/login.jpg")
        img = img.resize((1200,700), Image.ANTIALIAS)
        self.background_img = ImageTk.PhotoImage(img)

        b_img = Label(self.root, image=self.background_img)
        b_img.place(x=0,y=0,width=1200, height=700)
        
        frame = Frame(self.root, bg = "white")
        frame.place(x=300,y=100,width=600, height=500)

        #-----------register----------
        reg_in = Label(frame, text="Register", font=("corbel",24, "bold"),bg="white", fg = "black")
        reg_in.place(x=250, y=10)

        #----------labels and entry--------
        fname = Label(frame, text="First Name:",font=("corbel",15, "bold"),bg="white", fg = "black" )
        fname.place(x=10, y=100)

        self.fname_entry = ttk.Entry(frame,font=("corbel",10, "bold"), textvariable=self.var_fname)
        self.fname_entry.place(x=12,y=130, width=270)

        
        lname = Label(frame, text="Last Name:",font=("corbel",15, "bold"),bg="white", fg = "black" )
        lname.place(x=300, y=100)

        self.lname_entry = ttk.Entry(frame,font=("corbel",10, "bold"), textvariable=self.var_lname)
        self.lname_entry.place(x=302,y=130, width=270)

        email = Label(frame, text="E-mail:",font=("corbel",15, "bold"),bg="white", fg = "black" )
        email.place(x=10, y=170)

        self.email_entry = ttk.Entry(frame,font=("corbel",10, "bold"), textvariable=self.var_email)
        self.email_entry.place(x=12,y=200, width=270)

        contact = Label(frame, text="Contact:",font=("corbel",15, "bold"),bg="white", fg = "black" )
        contact.place(x=300, y=170)

        self.contact_entry = ttk.Entry(frame,font=("corbel",10, "bold"), textvariable=self.var_contact)
        self.contact_entry.place(x=302,y=200, width=270)

        sec_question = Label(frame, text="Security Question:",font=("corbel",15, "bold"),bg="white", fg = "black" )
        sec_question.place(x=10, y=240)

        self.sec_question = ttk.Combobox(frame,font=("corbel",10, "bold"),state="readonly", textvariable=self.var_sec_question)
        self.sec_question["values"] = ("Select Question", "Your birth place", "Your father name", "Your mother name")
        self.sec_question.current(0)
        self.sec_question.place(x=12,y=270, width=270)

        sec_ans = Label(frame, text="Security Answer:",font=("corbel",15, "bold"),bg="white", fg = "black" )
        sec_ans.place(x=300, y=240)

        self.sec_ans_entry = ttk.Entry(frame,font=("corbel",10, "bold"), textvariable=self.var_sec_ans)
        self.sec_ans_entry.place(x=302,y=270, width=270)

        password = Label(frame, text="Password:",font=("corbel",15, "bold"),bg="white", fg = "black" )
        password.place(x=10, y=310)

        self.password_entry = ttk.Entry(frame,font=("corbel",10, "bold"), textvariable=self.var_pass)
        self.password_entry.place(x=12,y=340, width=270)

        confirm_pass = Label(frame, text="Confirm Password:",font=("corbel",15, "bold"),bg="white", fg = "black" )
        confirm_pass.place(x=300, y=310)

        self.confirm_pass_entry = ttk.Entry(frame,font=("corbel",10, "bold"), textvariable=self.var_confpass)
        self.confirm_pass_entry.place(x=302,y=340, width=270)


        #-----------check button-----------
        
        self.var_chk=IntVar()
        chkbtn = Checkbutton(frame, text="I agree to the terms and conditions",variable=self.var_chk,font=("corbel",10, "bold"), onvalue=1, offvalue=0)
        chkbtn.place(x=10, y=380)


        #--------------buttons-----------
        reg_btn = Button(frame, text="Register",font=("corbel",15, "bold"),command=self.reg_data, borderwidth=0, relief=RIDGE,bg="blue", fg = "white", activeforeground="white", activebackground="blue", cursor="hand2")
        reg_btn.place(x=175, y=440, width=100)


        login_btn = Button(frame, text="Login",font=("corbel",15, "bold"), borderwidth=0, relief=RIDGE,bg="blue", fg = "white", activeforeground="white", activebackground="blue", cursor="hand2")
        login_btn.place(x=300, y=440, width=100)


    #-------------functions--------------
    def reg_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="" or self.var_sec_question.get()=="Select Question" or self.var_sec_ans.get()=="":
            messagebox.showerror("Error", "All fields are required!")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password does not match!")
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "You need to agree to the terms and conditions!")
        else:
            conn=mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognition")
            my_cursor = conn.cursor()
            query = ("select * from register where email = %s")
            value = (self.var_email.get(),)
            my_cursor.execute(query,value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already registered!")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                                                                            self.var_fname.get(),
                                                                            self.var_lname.get(),
                                                                            self.var_email.get(),
                                                                            self.var_contact.get(),
                                                                            self.var_sec_question.get(),
                                                                            self.var_sec_ans.get(),
                                                                            self.var_pass.get()
                ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "User registered successfully!", parent=self.root)

class Facial_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x700+150+50")
        self.root.title("Facial Recognition Attendance")

        img = Image.open("images/background.jpg")
        img = img.resize((1200,700), Image.ANTIALIAS)
        self.background_img = ImageTk.PhotoImage(img)

        b_img = Label(self.root, image=self.background_img)
        b_img.place(x=0,y=0,width=1200, height=700)

        title_label = Label(b_img, text="Facial Recognition Attendance System", font=("corbel",36, "bold"),bg="white", fg = "black")
        title_label.place(x=0, y=0, width=1200, height=60)

        # student button
        img_student = Image.open("images/student.png")
        img_student = img_student.resize((220,220), Image.ANTIALIAS)
        self.student_img = ImageTk.PhotoImage(img_student)

        b1 = Button(b_img, image = self.student_img, command=self.student_details, cursor="hand2")
        b1.place(x=100, y=100,width= 220, height= 220)
        
        b1 = Button(b_img, text="Student Details", command=self.student_details, cursor="hand2",font=("corbel",14, "bold"),bg="white", fg = "black")
        b1.place(x=100, y=320,width= 220, height= 40)
        
        
        # face detection
        img_face = Image.open("images/facedetection.png")
        img_face = img_face.resize((220,220), Image.ANTIALIAS)
        self.face_img = ImageTk.PhotoImage(img_face)

        b2 = Button(b_img, image = self.face_img, command= self.recognizer, cursor="hand2")
        b2.place(x=480, y=100,width= 220, height= 220)
        
        b2 = Button(b_img, text="Face Detection", command= self.recognizer, cursor="hand2",font=("corbel",14, "bold"),bg="white", fg = "black")
        b2.place(x=480, y=320,width= 220, height= 40)
        
        
        # attendance
        img_attendance = Image.open("images/attendance.png")
        img_attendance = img_attendance.resize((220,220), Image.ANTIALIAS)
        self.attendance_img = ImageTk.PhotoImage(img_attendance)

        b3 = Button(b_img, image = self.attendance_img, command= self.attendance_data, cursor="hand2")
        b3.place(x=880, y=100,width= 220, height= 220)
        
        b3 = Button(b_img, text="Attendance", command= self.attendance_data, cursor="hand2",font=("corbel",14, "bold"),bg="white", fg = "black")
        b3.place(x=880, y=320,width= 220, height= 40)
        
        
        #exit
        img_exit = Image.open("images/exit.png")
        img_exit = img_exit.resize((220,220), Image.ANTIALIAS)
        self.exit_img = ImageTk.PhotoImage(img_exit)

        b4 = Button(b_img, image = self.exit_img, command=self.exit, cursor="hand2")
        b4.place(x=880, y=400,width= 220, height= 220)
        
        b4 = Button(b_img, text="Exit", cursor="hand2", command=self.exit,font=("corbel",14, "bold"),bg="white", fg = "black")
        b4.place(x=880, y=620,width= 220, height= 40)
        
        
        
        # train face
        img_train = Image.open("images/trainface.png")
        img_train = img_train.resize((220,220), Image.ANTIALIAS)
        self.train_img = ImageTk.PhotoImage(img_train)

        b5 = Button(b_img, image = self.train_img,command=self.train_data, cursor="hand2")
        b5.place(x=100, y=400,width= 220, height= 220)
        
        b5 = Button(b_img, text="Train Data",command=self.train_data, cursor="hand2",font=("corbel",14, "bold"),bg="white", fg = "black")
        b5.place(x=100, y=620,width= 220, height= 40)

        
        # faces
        img_faces = Image.open("images/face.png")
        img_faces = img_faces.resize((220,220), Image.ANTIALIAS)
        self.faces_img = ImageTk.PhotoImage(img_faces)

        b6 = Button(b_img, image = self.faces_img, cursor="hand2", command=self.open_img)
        b6.place(x=480, y=400,width= 220, height= 220)
        
        b6 = Button(b_img, text="Faces", cursor="hand2", command=self.open_img, font=("corbel",14, "bold"),bg="white", fg = "black")
        b6.place(x=480, y=620,width= 220, height= 40)


    def open_img(self):
        os.startfile("data")



    #-------------function buttons--------------
    def student_details(self):
        self.new_win = Toplevel(self.root)
        self.app = Students(self.new_win)
    
    
    def train_data(self):
        self.new_win = Toplevel(self.root)
        self.app = Train(self.new_win)

    def recognizer(self):
        self.new_win = Toplevel(self.root)
        self.app = Recognition(self.new_win)
    
    def attendance_data(self):
        self.new_win = Toplevel(self.root)
        self.app = Attendance(self.new_win)

    def exit(self):
        self.exit=tkinter.messagebox.askyesno("Face Recognition", "Are you sure you want to exit?", parent= self.root)
        if self.exit >0:
            self.root.destroy()
        else:
            return





if __name__ == "__main__":
    main()