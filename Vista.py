from logging import root
from msilib.schema import AppId
from tkinter import *
from PIL import Image, ImageTk
from Control import Controlador
import tkinter as tk
from Insertar import Insert

class OCR(tk.Frame):  
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        #Menu
        mi_menu = Menu(self)
        ROOT.config(menu = mi_menu)

        #Apartado Cliente
        Cliente = Menu(mi_menu, tearoff=0)
        Cliente.add_command(label="Registrar Cliente", command=self.insertar)
        Cliente.add_command(label="Gestion Cliente")
        
        mi_menu.add_cascade(label="Clientes", menu=Cliente)

        self.parent.title("SISTEMA de EXTRACCION DE DATOS")
    
    def insertar(self):
        print("akkkk")
        obj_ins = Insert()
        obj_ins.ventana_reg()

if __name__ == "__main__":
    ROOT = tk.Tk()
    ROOT.geometry("900x270")
    APP = OCR(parent=ROOT)

    #Fondo
    imagen = Image.open('Fotos/patron.png')
    render = ImageTk.PhotoImage(imagen)
    Label(ROOT, image=render).pack(anchor="nw")

    APP.mainloop()
    #ROOT.destroy()


