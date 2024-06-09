from tkinter import*
from tkinter import ttk
from typing import Self
from PIL import Image,ImageTk
import os
from patient import Patient
from scanner import FaceScanner
from chatbott import ChatbotWindow
from developer import Developer
from helpdesk import Helpdesk




class face_recognition2:
    def __init__(self,root):
        self.root=root
        self.root.geometry ("1530x790+0+0")
        self.root.title("Mood Detector")
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



#Mood Scanner button
        
        img7=Image.open(r"C:\Users\sulthana safeer\Desktop\face_recognition_system\images\facedetection.png")
        img7=img7.resize((263,175),Image.LANCZOS)              
        self.PhotoImage7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.PhotoImage7,command=self.face_scanner, cursor= "hand2")
        b1.place(x=367.5,y=100,width=263,height=175)



        b1_1=Button(bg_img,text = "Face Scanner",command=self.face_scanner, cursor= "hand2", font= ("times new roman",15,), bg ="white", fg="Gray")
        b1_1.place(x=367.5,y=250,width=264,height=40)

#help desk button
        
        img6=Image.open(r"C:\Users\sulthana safeer\Desktop\face_recognition_system\images\helpdesk.jpg")
        img6=img6.resize((263,175),Image.LANCZOS)              
        self.PhotoImage6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.PhotoImage6, command= self.helpdesk, cursor= "hand2")
        b1.place(x=845,y=100,width=263,height=175)



        b1_1=Button(bg_img,text = "Help Desk", cursor= "hand2", command= self.helpdesk, font= ("times new roman",15,), bg ="white", fg="Gray")
        b1_1.place(x=845,y=250,width=264,height=40)



#developers button
        
        img33=Image.open(r"C:\Users\sulthana safeer\Desktop\face_recognition_system\images\DEVELOPERS.png")
        img33=img33.resize((263,175),Image.LANCZOS)              
        self.PhotoImage33=ImageTk.PhotoImage(img33)

        b1=Button(bg_img,image=self.PhotoImage33,command= self.developer, cursor= "hand2")
        b1.place(x=367.5,y=400,width=263,height=175)



        b1_1=Button(bg_img,text = "Developer", cursor= "hand2",command= self.developer, font= ("times new roman",15,), bg ="white", fg="Gray")
        b1_1.place(x=367.5,y=550,width=264,height=40)

#AICHATBOT button
        
        img34=Image.open(r"C:\Users\sulthana safeer\Desktop\face_recognition_system\images\AI.jpg")
        img34=img34.resize((263,175),Image.LANCZOS)              
        self.PhotoImage34=ImageTk.PhotoImage(img34)

        b1=Button(bg_img,image=self.PhotoImage34, command=self.chat_bot, cursor= "hand2")
        b1.place(x=845,y=400,width=263,height=175)



        b1_1=Button(bg_img,text = "Chat Bot", cursor= "hand2",  command= self.chat_bot,font= ("times new roman",15,),  bg ="white", fg="Gray")
        b1_1.place(x=845,y=550,width=264,height=40)
        #===========================Function buttons===========================



    def face_scanner(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceScanner(self.new_window)

    def chat_bot(self):
        self.new_window =Toplevel(self.root)
        self.app = ChatbotWindow(self.new_window)

    def developer(self):
        self.new_window =Toplevel(self.root)
        self.app = Developer(self.new_window)

    def helpdesk(self):
        self.new_window =Toplevel(self.root)
        self.app = Helpdesk(self.new_window)
    
    














        

if __name__ == "__main__":
    root=Tk()
    obj=face_recognition2(root)
    root.mainloop()


    
