from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import numpy as np
from time import strftime
from datetime import datetime


class Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x700+150+50")
        self.root.title("Facial Recognition Attendance")

        title_label = Label(self.root, text="Face Detection", font=("corbel",36, "bold"),bg="white", fg = "black")
        title_label.place(x=0, y=0, width=1200, height=60)
        
        img = Image.open("images/background.jpg")
        img = img.resize((1200,800), Image.ANTIALIAS)
        self.background_img = ImageTk.PhotoImage(img)

        b_img = Label(self.root, image=self.background_img)
        b_img.place(x=0,y=60,width=1200, height=700)

        b1 = Button(b_img, text="Detect Face", cursor="hand2", command=self.detector,font=("corbel",14, "bold"),bg="white", fg = "black")
        b1.place(x=500, y=320,width= 220, height= 60)


    #-----------attendance----------
    def attendance(self,i,r,n,d):
        with open("attendance.csv", "r+", newline="\n") as f:
            dataList = f.readlines()
            name_list = []
            for line in dataList:
                entry = line.split((","))
                name_list.append(entry[0])
            
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                timeString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{timeString},{d1}, Present")


    #-----------face recognition------------
    def detector(self):
        def boundary(img, classifier, scaleFactor, min_neighbor, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, min_neighbor)

            coordinates = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w, y+h), (0,255,0), 3)
                id, predict = clf.predict(gray_img[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="face_recognition")
                my_cursor = conn.cursor()

                my_cursor.execute("select name from student where id =" +str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)
                
                my_cursor.execute("select roll from student where id =" +str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)
                
                my_cursor.execute("select dep from student where id =" +str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)
                
                my_cursor.execute("select id from student where id =" +str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)




                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x,y-80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Roll No.:{r}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Name:{n}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    cv2.putText(img, f"Department:{d}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)
                    self.attendance(i,r,n,d)

                else:
                    cv2.rectangle(img,(x,y),(x+w, y+h), (0,0,255), 2)
                    cv2.putText(img, "Unknown", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 2)

                coordinates = [x,y,w,h]
            return coordinates
        def recognize(img, clf, faceCascade):
            coordinates = boundary(img, faceCascade,1.1,10,(255,25,255), "Face", clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_capture = cv2.VideoCapture(0)

        while True:
            ret, img = video_capture.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Face Detection", img)

            if cv2.waitKey(1)==13:
                break
        video_capture.release()
        cv2.destroyAllWindows
        







if __name__ == "__main__":
    root = Tk()
    obj = Recognition(root)
    root.mainloop()