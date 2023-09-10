from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2 
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x700+150+50")
        self.root.title("Facial Recognition Attendance")


        title_label = Label(self.root, text="Train Dataset", font=("corbel",36, "bold"),bg="white", fg = "black")
        title_label.place(x=0, y=0, width=1200, height=60)


        img = Image.open("images/background.jpg")
        img = img.resize((1200,800), Image.ANTIALIAS)
        self.background_img = ImageTk.PhotoImage(img)

        b_img = Label(self.root, image=self.background_img)
        b_img.place(x=0,y=60,width=1200, height=700)

        b1 = Button(b_img, text="Train Data",command=self.train_classifier, cursor="hand2",font=("corbel",14, "bold"),bg="white", fg = "black")
        b1.place(x=500, y=320,width= 220, height= 60)


    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Train", imageNp)
            cv2.waitKey(1)==13
        ids = np.array(ids)


        #-----------train clasifier and save----------
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training completed!", parent=self.root)



if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()