from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from Gestion_usuario import Gestion_user
from login import Login

class OCR(tk.Frame): 
    ROOT2 = None
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        #Menu
        mi_menu = Menu(self)
        ROOT.config(menu = mi_menu)

        #Apartado Config
        Conf = Menu(mi_menu, tearoff=0)
        Conf.add_command(label="Login", command=self.login)
        #Apartado Cliente
        Cliente = Menu(mi_menu, tearoff=0)
        Cliente.add_command(label="Gestion Cliente", command=self.gestion_clientes)
       
        mi_menu.add_cascade(label="Configuración", menu=Conf)
        mi_menu.add_cascade(label="Clientes", menu=Cliente)

        self.parent.title("SISTEMA de EXTRACCION DE DATOS")
        

    
    def gestion_clientes(self):
        ins_gc = Gestion_user()
        ins_gc.Lista()
    def login(self):
        ins_log = Login()
        ins_log.login_w(ROOT2)

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("900x270")
    APP = OCR(parent=ROOT)
    global ROOT2

    ROOT2 = ROOT
    #Fondo
    imagen = Image.open('Fotos/patron.png')
    render = ImageTk.PhotoImage(imagen)
    Label(ROOT, image=render).pack(anchor="nw")

    login = Login()
    login.login_w(ROOT)
    APP.mainloop()
    #ROOT.destroy()


