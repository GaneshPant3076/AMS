from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

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










if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()