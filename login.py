from pickle import GLOBAL
from tkinter import *
from tkinter import ttk, font
from PIL import Image, ImageTk
from Control import Controlador

class Login():

    def login_w(self, root):
        self.ventana = Toplevel()
        self.ventana.geometry("230x300")
        self.ventana.resizable(width=False, height=False)
        self.ventana.title("Login")

        image = Image.open("Fotos/logo_patron.png")
        img_r = image.resize((200,80))
        img = ImageTk.PhotoImage(img_r)
        self.lb_logo = ttk.Label(self.ventana, image=img)
        self.lb_logo.place(x=20, y=10)

        self.lbl_host = ttk.Label(self.ventana, text="Host: ", width=15)
        self.lbl_host.place(x=20, y=80)

        self.host = StringVar()
        self.txt_host = ttk.Entry(self.ventana, textvariable=self.host, width=30)
        self.txt_host.place(x=20, y=100)

        #user
        self.lb_user = ttk.Label(self.ventana, text="Usuario: ", width=15)
        self.lb_user.place(x=20, y=130)

        self.user = StringVar()
        self.txt_user = ttk.Entry(self.ventana, textvariable=self.user, width=30) 
        self.txt_user.place(x=20, y=150)

        #password
        self.lb_pass = ttk.Label(self.ventana, text="Contraseña: ", width=15)
        self.lb_pass.place(x=20, y=180)

        self.passw = StringVar()
        self.txt_pass = ttk.Entry(self.ventana, textvariable=self.passw, width=30, show="*")
        self.txt_pass.place(x=20, y=210)

        #Boton entrar
        self.btn_entrar = ttk.Button(self.ventana, text="Login", compound=LEFT, command=self.Login)
        self.btn_entrar.place(x=75, y=240)

        self.ventana.focus_force()
        self.ventana.focus_set()
        self.ventana.transient(root)
        self.ventana.grab_set() # Manetener el foco de inicio obligando la ventana inicial a estar inactiva
        self.ventana.mainloop()

    def Login(self):
        self.Host2 = self.txt_host.get()
        self.user2 = self.txt_user.get()
        self.passw2 = self.txt_pass.get()

        Datos = [self.Host2, self.user2, self.passw2]
        Controlador.Login(Datos)
        self.ventana.destroy()