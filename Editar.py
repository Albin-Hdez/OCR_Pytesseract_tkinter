from msilib import Control
from tkinter import *
from tkinter import ttk, font
from Control import Controlador

class Edit():
    def Pantalla_editar(self, ID):
        self.id_datos = ID
        print(ID)
        self.ventana = Toplevel()
        self.ventana.geometry("340x280")
        self.ventana.resizable(width=False, height=False)
        self.ventana.title("Editar Informacion de Cliente")

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

        self.img_guardar = PhotoImage(file="Fotos/save.png")
        self.btn_guardar = ttk.Button(self.ventana, text="Guardar", compound=LEFT, image=self.img_guardar, command=self.modificar)
        self.btn_guardar.place(x=168, y=200, width=140, height=40)
        
        self.img_up = PhotoImage(file="Fotos/upload.png")
        self.btn_cargar = ttk.Button(self.ventana, text="Cargar", compound=LEFT, image=self.img_up, command= lambda: self.insert(self.id_datos))
        self.btn_cargar.place(x=20, y=200, width=140, height=40)
    
    def insert(self, id):
        
        DATOS = Controlador.Buscar(id, "ID")

        for i in DATOS:
            ape1 = i[1]
            ape2 = i[2]
            nom = i[3]
            dir = i[4]
            curp = i[5]
            rfc = i[6]

        print(ape1)
        self.txt_Ape1.insert(0, ape1)
        self.txt_Ape2.insert(0,  ape2)
        self.txt_nom.insert(0,  nom)
        self.txt_dir.insert(0, dir)
        self.txt_curp.insert(0, curp)
        self.txt_rfc.insert(0, rfc)
    
    def modificar(self):
        
        ARRAY_DATOS = []

        APELLIDO_P = self.txt_Ape1.get()
        APELLIDO_M = self.txt_Ape2.get()
        NOMBRES = self.txt_nom.get()
        DIRECCION = self.txt_dir.get()
        CURP = self.txt_curp.get()
        RFC = self.txt_rfc.get()
                
        ARRAY_DATOS = [self.id_datos ,APELLIDO_P, APELLIDO_M, NOMBRES, DIRECCION, CURP, RFC]
        Controlador.modificar(ARRAY_DATOS)
        #print(ARRAY_DATOS)

