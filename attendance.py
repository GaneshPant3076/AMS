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
import csv
from tkinter import filedialog

myData=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x700+150+50")
        self.root.title("Facial Recognition Attendance")

        #========variables============
        self.var_attendance_id = StringVar()
        self.var_attendance_name = StringVar()
        self.var_attendance_date = StringVar()
        self.var_attendance_dep = StringVar()
        self.var_attendance_roll = StringVar()
        self.var_attendance_time = StringVar()
        self.var_attendance_attendance = StringVar()

        title_label = Label(self.root, text="Attendance Management", font=("corbel",36, "bold"),bg="white", fg = "black")
        title_label.place(x=0, y=0, width=1200, height=60)

        main_frame = Frame(self.root, bd=2)
        main_frame.place(x=0, y=60, width=1200, height=640)

        #left label frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,bg="white", text="Student Attendance Details",font=("corbel",18, "bold"))
        left_frame.place(x=0, y=0, width=530, height=630)
        
        #left inside label frame
        in_frame = LabelFrame(left_frame, bd=2, relief=RIDGE,bg="white", text="Student Information",font=("corbel",18, "bold"))
        in_frame.place(x=0, y=0, width=530, height=180)

        #----------- labels and entry------------
        
        #attendance ID
        attendanceId_label = Label(in_frame, text= 'Attendance ID:',font=("corbel",12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx= 5, sticky=W)

        attendanceId_entry = ttk.Entry(in_frame, width=15, textvariable= self.var_attendance_id,font=("corbel",12, "bold"))
        attendanceId_entry.grid(row=0, column=1, padx=5, sticky=W)
        

        #name
        name_label = Label(in_frame, text= 'Name:',font=("corbel",12, "bold"), bg="white")
        name_label.grid(row=0, column=2, padx= 5, sticky=W)

        name_entry = ttk.Entry(in_frame, width=15, textvariable=self.var_attendance_name,font=("corbel",12, "bold"))
        name_entry.grid(row=0, column=3, padx=5, sticky=W)

        #date
        date_label = Label(in_frame, text= 'Date:',font=("corbel",12, "bold"), bg="white")
        date_label.grid(row=1, column=0, padx= 5, pady=10, sticky=W)

        date_entry = ttk.Entry(in_frame, width=15, textvariable=self.var_attendance_date,font=("corbel",12, "bold"))
        date_entry.grid(row=1, column=1, padx=5, pady=10, sticky=W)

        #department 
        dep_label = Label(in_frame, text= 'Department:',font=("corbel",12, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx= 5, sticky=W)

        dep_combo = ttk.Combobox(in_frame, textvariable=self.var_attendance_dep, font=("corbel",8, "bold"), width=17,state="readonly")
        dep_combo["values"] = ("Select Department", "Computer", "Civil", "Architecture")
        dep_combo.current(0)
        dep_combo.grid(row=1, column=3, padx=5, pady=5, sticky=W)
        
        #roll no
        roll_label = Label(in_frame, text= 'Roll no.:',font=("corbel",12, "bold"), bg="white")
        roll_label.grid(row=2, column=0, padx= 5, pady=10, sticky=W)

        roll_entry = ttk.Entry(in_frame, width=15, textvariable=self.var_attendance_roll,font=("corbel",12, "bold"))
        roll_entry.grid(row=2, column=1, padx=5,pady=10, sticky=W)
        
        #time
        time_label = Label(in_frame, text= 'Time:',font=("corbel",12, "bold"), bg="white")
        time_label.grid(row=2, column=2, padx= 5, pady=10, sticky=W)

        time_entry = ttk.Entry(in_frame, width=15, textvariable=self.var_attendance_time,font=("corbel",12, "bold"))
        time_entry.grid(row=2, column=3, padx=5,pady=10, sticky=W)

        #attendance status 
        attendance_label = Label(in_frame, text= 'Attendance Status:',font=("corbel",12, "bold"), bg="white")
        attendance_label.grid(row=3, column=0, padx= 10, sticky=W)

        attendance_combo = ttk.Combobox(in_frame, textvariable=self.var_attendance_attendance, font=("corbel",8, "bold"), width=17,state="readonly")
        attendance_combo["values"] = ("Select Status", "Present", "Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3, column=1, padx=5, pady=10, sticky=W)

        #button frame
        btn_frame = Frame(left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=200, width=530, height=150)

        #import csv button
        import_btn = Button(btn_frame, text="Import CSV",command= self.importCsv, font=("corbel",12, "bold"))
        import_btn.grid(row=0, column=0, padx= 10, pady=10, sticky=W)
        
        #export csv
        export_btn = Button(btn_frame, text="Export CSV", command=self.exportCsv, font=("corbel",12, "bold"))
        export_btn.grid(row=0, column=1, padx= 10, pady=10, sticky=W)

        #update button
        update_btn = Button(btn_frame, text="Update", font=("corbel",12, "bold"))
        update_btn.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        #reset button
        reset_btn = Button(btn_frame, text="Reset",command=self.reset_data, font=("corbel",12, "bold"))
        reset_btn.grid(row=1, column=1, padx=10, pady=10, sticky=W)


        #right label frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE,bg="white", text="Attendance Details",font=("corbel",18, "bold"))
        right_frame.place(x=530, y=0, width=660, height=630)

        #table frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE,bg="white")
        table_frame.place(x=5, y=5, width=660, height=425)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.attendanceTable = ttk.Treeview(table_frame, columns=("id", "roll", "name", "dep", "time", "date","attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill= X)
        scroll_y.pack(side=RIGHT, fill= Y)

        scroll_x.config(command=self.attendanceTable.xview)
        scroll_y.config(command=self.attendanceTable.yview)

        self.attendanceTable.heading("id", text="Attendance ID")
        self.attendanceTable.heading("name", text="Name")
        self.attendanceTable.heading("date", text="Date")
        self.attendanceTable.heading("dep", text="Department")
        self.attendanceTable.heading("roll", text="Roll No")
        self.attendanceTable.heading("time", text="Time")
        self.attendanceTable.heading("attendance", text="Attendance")
        self.attendanceTable["show"] = "headings"
        
        self.attendanceTable.column("id", width=100)
        self.attendanceTable.column("name", width=100)
        self.attendanceTable.column("date", width=100)
        self.attendanceTable.column("dep", width=100)
        self.attendanceTable.column("roll", width=100)
        self.attendanceTable.column("time", width=100)
        self.attendanceTable.column("attendance", width=100)
        
        
        self.attendanceTable.pack(fill=BOTH, expand=1)
        self.attendanceTable.bind("<ButtonRelease>", self.get_cursor)

    #=================================fetch data=================
    def fetchData(self,rows):
        self.attendanceTable.delete(*self.attendanceTable.get_children())
        for i in rows:
            self.attendanceTable.insert("", END, values=i)

    #import 
    def importCsv(self):
        global myData
        myData.clear()
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*csv"),("All File", "*.*")), parent=self.root)
        with open(filename) as myfile:
            csvread= csv.reader(myfile, delimiter=",")
            for i in csvread:
                myData.append(i)
            self.fetchData(myData)

    #export
    def exportCsv(self):
        try:
            if len(myData)<1:
                messagebox.showerror("No Data","No data to export", parent=self.root)
                return False
            filename = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*csv"),("All File", "*.*")), parent=self.root)
            with open(filename, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in myData:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Data exported to "+os.path.basename(filename)+" successfully!")
        except Exception as es:
            messagebox.showerror("Error", f"Due To : {str(es)}, parent=self.root")

    #====get variables======
    def get_cursor(self, event=""):
        cursor_row = self.attendanceTable.focus()
        content = self.attendanceTable.item(cursor_row)
        rows = content['values']
        self.var_attendance_id.set(rows[0])
        self.var_attendance_name.set(rows[2])
        self.var_attendance_date.set(rows[5])
        self.var_attendance_dep.set(rows[3])
        self.var_attendance_roll.set(rows[1])
        self.var_attendance_time.set(rows[4])
        self.var_attendance_attendance.set(rows[6])

    #===========reset=====
    def reset_data(self):
        self.var_attendance_id.set("")
        self.var_attendance_name.set("")
        self.var_attendance_date.set("")
        self.var_attendance_dep.set("")
        self.var_attendance_roll.set("")
        self.var_attendance_time.set("")
        self.var_attendance_attendance.set("")


    


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()