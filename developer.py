from tkinter import*
from tkinter import ttk
from typing import Self
from PIL import Image,ImageTk
import os
from tkinter import messagebox
import mysql.connector
import cv2




class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry ("1530x790+0+0")
        self.root.title("Mood_Detector")
        #first image
        img1=Image.open(r"C:\Users\sulthana safeer\Desktop\face_recognition_system\images\NAME.png")
        img1=img1.resize((500,150),Image.LANCZOS)              
        self.PhotoImage1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.PhotoImage1)
        f_lbl.place(x=0,y=0,width=500,height=150)

#third image
        img2=Image.open(r"C:\Users\sulthana safeer\Desktop\face_recognition_system\images\blue.png")
        img2=img2.resize((550,150),Image.LANCZOS)              
        self.PhotoImage2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.PhotoImage2)
        f_lbl.place(x=1000,y=0,width=550,height=150)
#SECOND image
        img120=Image.open(r"C:\Users\sulthana safeer\Desktop\face_recognition_system\images\blue.png")
        img120=img120.resize((550,150),Image.LANCZOS)              
        self.PhotoImage120=ImageTk.PhotoImage(img120)

        f_lbl=Label(self.root,image=self.PhotoImage2)
        f_lbl.place(x=500,y=0,width=550,height=150)

#TITLE image
        img3=Image.open(r"C:\Users\sulthana safeer\Desktop\face_recognition_system\images\title.png")
        img3=img3.resize((500,150),Image.LANCZOS)              
        self.PhotoImage3=ImageTk.PhotoImage(img3)

        f_lbl=Label(self.root,image=self.PhotoImage3)
        f_lbl.place(x=550,y=0,width=500,height=150)

#MDX IMAGE
        img10=Image.open(r"C:\Users\sulthana safeer\Desktop\face_recognition_system\images\blue.png")
        img10=img10.resize((500,150),Image.LANCZOS)              
        self.PhotoImage10=ImageTk.PhotoImage(img10)

        f_lbl=Label(self.root,image=self.PhotoImage10)
        f_lbl.place(x=1500,y=0,width=500,height=150)

#bg image
        img4=Image.open(r"C:\Users\sulthana safeer\Desktop\face_recognition_system\images\blue.png")
        img4=img4.resize((2000,1000),Image.LANCZOS)              
        self.PhotoImage4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.PhotoImage4)
        bg_img.place(x=0,y=130,width=2000,height=1000)   


        title_lbl= Label(bg_img,text=" D E V E L O P E R", font= ("times new roman", 28), bg= "gold", fg= "black")
        title_lbl.place(x=0,y=0, width=1530,height=45)

        #frame

        img69=Image.open(r"C:\Users\sulthana safeer\Desktop\face_recognition_system\images\im_sulthanafrfr .png")
        img69=img69.resize((1530,790),Image.LANCZOS)              
        self.PhotoImage69=ImageTk.PhotoImage(img69)

        f_lbl=Label(self.root,image=self.PhotoImage69)
        f_lbl.place(x=0,y=180,width=1530,height=790)



       














if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()
