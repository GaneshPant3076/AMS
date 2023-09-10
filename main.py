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
    root = Tk()
    obj = Facial_Recognition(root)
    root.mainloop()