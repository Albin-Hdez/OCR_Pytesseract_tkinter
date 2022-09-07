from tkinter import *
from tkinter import ttk, font
from PIL import Image, ImageTk
from Control import Controlador

class Edit():
    def Pantalla_editar(self):
        self.ventana = Toplevel()
        self.ventana.geometry("660x430")
        self.ventana.resizable(width=False, height=False)
        self.ventana.title("Registrar Cliente")

        #Apellido Paterno
        self.lb_ape1 = ttk.Label(self.ventana, text="Apellido Paterno: ", width=15)
        self.lb_ape1.place(x=20, y=20)
                
        self.Ape1 = StringVar()
        self.txt_Ape1 = ttk.Entry(self.ventana, textvariable=self.Ape1, width=30)
        self.txt_Ape1.place(x=120, y=20)

        #Apellido Materno
        self.lb_ape2 = ttk.Label(self.ventana, text="Apellido Materno :", width=16)
        self.lb_ape2.place(x=20, y=45)
                
        Ape2 = StringVar()
        self.txt_Ape2 = ttk.Entry(self.ventana, textvariable=Ape2, width=30)
        self.txt_Ape2.place(x=120, y=45)

        #Nombre
        self.lb_nom = ttk.Label(self.ventana, text="Nombre(s)", width=15)
        self.lb_nom.place(x=20, y=70)
                
        self.Nom = StringVar()
        self.txt_nom = ttk.Entry(self.ventana, textvariable=self.Nom, width=30)
        self.txt_nom.place(x=120, y=70)

        #Direccion
        self.lb_dir = ttk.Label(self.ventana, text="Direccion", width=15)
        self.lb_dir.place(x=20, y=95)
                
        self.Dir = StringVar()
        self.txt_dir = ttk.Entry(self.ventana, textvariable=self.Dir, width=42)
        self.txt_dir.place(x=120, y=95, width=185, height=42)

        #CURP
        self.lb_curp = ttk.Label(self.ventana, text="CURP", width=15)
        self.lb_curp.place(x=20, y=140)
                
        self.CURP = StringVar()
        self.txt_curp = ttk.Entry(self.ventana, textvariable=self.CURP, width=30)
        self.txt_curp.place(x=120, y=140)

        #RFC
        self.lb_curp = ttk.Label(self.ventana, text="RFC", width=15)
        self.lb_curp.place(x=20, y=165)
                
        self.RFC = StringVar()
        self.txt_rfc = ttk.Entry(self.ventana, textvariable=self.RFC, width=30)
        self.txt_rfc.place(x=120, y=165)

    
        #Background
        #fondo = Image.open('Fotos/fondo.jpg')
        #render_fondo = ImageTk.PhotoImage(fondo)