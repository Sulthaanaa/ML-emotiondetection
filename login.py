from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk 
from main import face_recognition_system
from patientaccess import face_recognition2  # Importing the face_recognition2 class

class login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\sulthana safeer\Desktop\face_recognition_system\images\blue1.png")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img101 = Image.open(r"C:\Users\sulthana safeer\Desktop\face_recognition_system\images\loginicon.png")
        img101 = img101.resize((100,100), Image.LANCZOS)              
        self.PhotoImage101 = ImageTk.PhotoImage(img101)
        lbling1 = Label(self.root, image=self.PhotoImage101, bg="black", borderwidth=0)
        lbling1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Admin Page", font=("times new roman",15,"bold"), fg="white", bg="black")
        get_str.place(x=125, y=110)
        # label
        username = Label(frame, text="Username", font=("times new roman",15,"bold"), fg="white", bg="black" )
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman",15,"bold"))
        self.txtuser.place(x=40, y=195, width=270)

        password = Label(frame, text="Password", font=("times new roman",15,"bold"), fg="white", bg="black")
        password.place(x=70, y=235)

        self.txtpass = ttk.Entry(frame, font=("times new roman",15,"bold"))
        self.txtpass.place(x=40, y=270, width=270)

        img303 = Image.open(r"C:\Users\sulthana safeer\Desktop\face_recognition_system\images\loginicon.png")
        img303 = img303.resize((25,25), Image.LANCZOS)
        self.photoimage303 = ImageTk.PhotoImage(img303)
        lblimg1 = Label(image=self.photoimage303, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=323, width=25, height=25)

        img304 = Image.open(r"C:\Users\sulthana safeer\Desktop\face_recognition_system\images\passwordicon.png")
        img304 = img304.resize((25,25), Image.LANCZOS)
        self.photoimage304 = ImageTk.PhotoImage(img304)
        lblimg1 = Label(image=self.photoimage304, bg="black", borderwidth=0)
        lblimg1.place(x=650, y=409, width=25, height=25)

        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman",15,"bold"),
                          bd=3, relief=RIDGE, fg="white", bg="navy blue")
        loginbtn.place(x=110, y=325, width=120, height=35)

        # registerbutton
        registerbtn = Button(frame, text="Patient Trail", command=self.open_patient_trail,
                             font=("times new roman", 10,"bold"), borderwidth=0, fg="white", bg="black",
                             activeforeground="white", activebackground="black")
        registerbtn.place(x=20, y=390, width=120,)

        forgetbtn = Button(frame, text="Forgot Your Password?", font=("times new roman", 10,"bold"),
                           borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgetbtn.place(x=170, y=390, width=160,)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "Bro fill the form smh")
        else:
            if self.txtuser.get() == "doctor@gmail.com" and self.txtpass.get() == "password":
                open_main = messagebox.askyesno("Authority Only Access", "Are you an authorized person?")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = face_recognition_system(self.new_window)
                else:
                    messagebox.showwarning("Oops", "Try Patient Trail")
            else:
                messagebox.showerror("Authorization", "Wrong Credentials! If you are not an authortized person. Please proceed with patient trails!")

    def open_patient_trail(self):
        self.new_window = Toplevel(self.root)
        self.app = face_recognition2(self.new_window)

if __name__ == "__main__":
    root = Tk()
    app = login_window(root)
    root.mainloop()
