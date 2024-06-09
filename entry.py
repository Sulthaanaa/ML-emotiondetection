from customtkinter import *

app = CTk()
app.geometry("1550x800+0+0")
app.config(bg="#0B132B")  # Night blue color

set_appearance_mode("#0B132B")  # Set appearance mode to night blue

btn_main_access = CTkButton(master=app, text="Main Access", corner_radius=32, fg_color="transparent",
                            hover_color="#4158D0", bg_color="#0B132B", border_width=2)
btn_main_access.place(relx=0.3, rely=0.5, anchor="center")

btn_patient_access = CTkButton(master=app, text="Patient Access", corner_radius=32, fg_color="transparent",
                               hover_color="#4158D0", bg_color="#0B132B", border_width=2)
btn_patient_access.place(relx=0.7, rely=0.5, anchor="center")

app.mainloop()
