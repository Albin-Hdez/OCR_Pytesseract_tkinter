from tkinter import *
from tkinter import ttk, font
from PIL import Image, ImageTk
from Control import Controlador

class Insert():
        def ventana_reg(self):
                self.registrar = Toplevel()
                self.registrar.geometry("660x430")
                self.registrar.resizable(width=False, height=False)
                self.registrar.title("Registrar Cliente")
                #Background
                fondo = Image.open('Fotos/fondo.jpg')
                render_fondo = ImageTk.PhotoImage(fondo)
                Label(self.registrar, image=render_fondo).pack(anchor="nw")

                #Labelframe Datos Personales
                self.labelframe1 = LabelFrame(self.registrar, text="INE y RFC", width=625, height=150)
                self.labelframe1.place(x=20, y=20)

                #Id Cliente Label y Textbox
                self.lb_Id = ttk.Label(self.registrar, text="Seleccion de Imagenes", width=20, anchor="center")
                self.lb_Id.place(x=100, y=40)
                
                #Boton para seleccionar foto de INE
                self.btn_ine = ttk.Button(self.registrar, text='Seleccionar Foto de INE', width=44, command=Controlador.Controller_INE)
                self.btn_ine.place(x=25, y=70, width=275, height=40)

                #Boton para seleccionar foto de RFC
                self.btn_rfc = ttk.Button(self.registrar, text='Seleccionar Foto de RFC', width=44, command=Controlador.Controller_RFC)
                self.btn_rfc.place(x=25, y=120, width=275, height=40)
                
                #Mostrar Fotos Label y Combobox
                self.lb_cb = ttk.Label(self.registrar, text="Mostrar INE ó RFC", width=30,anchor="center")
                self.lb_cb.place(x=410, y=40)
                
                self.cb_fotos = ttk.Combobox(self.registrar, state="readonly", values=["INE", "RFC"], width=30)
                self.cb_fotos.current(0)
                self.cb_fotos.place(x=360, y=70, width=275, height=40)

                #Boton Mostrar
                img_save = PhotoImage(file="Fotos/save.png")
                self.btn_guardar = ttk.Button(self.registrar, text="Mostrar Imagenes",compound = LEFT, command=lambda: Controlador.Controller_img(self.cb_fotos.get()))
                self.btn_guardar.place(x=360, y=120, width=275, height=40)
                
                #Labelframe Datos Personales
                self.labelframe3 = LabelFrame(self.registrar, text="Datos Personales", width=625, height=245)
                self.labelframe3.place(x=20, y=170)

                #Apellido Paterno
                self.lb_ape1 = ttk.Label(self.registrar, text="Apellido Paterno", width=15)
                self.lb_ape1.place(x=25, y=190)
                
                self.Ape1 = StringVar()
                self.txt_Ape1 = ttk.Entry(self.registrar, textvariable=self.Ape1, width=30)
                self.txt_Ape1.place(x=25, y=220)

                #Apellido Materno
                self.lb_ape2 = ttk.Label(self.registrar, text="Apellido Materno", width=15)
                self.lb_ape2.place(x=220, y=190)
                
                Ape2 = StringVar()
                self.txt_Ape2 = ttk.Entry(self.registrar, textvariable=Ape2, width=30)
                self.txt_Ape2.place(x=220, y=220)

                #Nombre
                self.lb_nom = ttk.Label(self.registrar, text="Nombre(s)", width=15)
                self.lb_nom.place(x=420, y=190)
                
                self.Nom = StringVar()
                self.txt_nom = ttk.Entry(self.registrar, textvariable=self.Nom, width=34)
                self.txt_nom.place(x=420, y=220)

                #Direccion
                self.lb_dir = ttk.Label(self.registrar, text="Direccion", width=15)
                self.lb_dir.place(x=25, y=250)
                
                self.Dir = StringVar()
                self.txt_dir = ttk.Entry(self.registrar, textvariable=self.Dir, width=42)
                self.txt_dir.place(x=25, y=280, width=382, height=42)

                #CURP
                self.lb_curp = ttk.Label(self.registrar, text="CURP", width=15)
                self.lb_curp.place(x=25, y=330)
                
                self.CURP = StringVar()
                self.txt_curp = ttk.Entry(self.registrar, textvariable=self.CURP, width=30)
                self.txt_curp.place(x=25, y=360)

                #RFC
                self.lb_curp = ttk.Label(self.registrar, text="RFC", width=15)
                self.lb_curp.place(x=220, y=330)
                
                self.RFC = StringVar()
                self.txt_rfc = ttk.Entry(self.registrar, textvariable=self.RFC, width=30)
                self.txt_rfc.place(x=220, y=360)

                #Boton Escanear INE
                img_id = PhotoImage(file="Fotos/id.png")
                self.btn_guardar = ttk.Button(self.registrar, text="Escanear INE",image=img_id, compound = TOP, command=self.rellena_INE)
                self.btn_guardar.place(x=420, y=250, width=100, height=100)

                #Boton Escanear RFC
                image_doc = PhotoImage(file="Fotos/doc.png")
                self.btn_guardar = ttk.Button(self.registrar, text="Escanear RFC",image=image_doc, compound = TOP, command=self.SCAN_RFC)
                self.btn_guardar.place(x=530, y=250, width=100, height=100)
                
                #Boton REGISTRAR
                self.btn_guardar = ttk.Button(self.registrar, text="Registrar Cliente", compound = LEFT, command=self.INSERT)
                self.btn_guardar.place(x=420, y=360, width=210, height=40)
        
        def rellena_INE(self):
                DATOS = Controlador.Controller_Scan_INE()
                self.txt_Ape1.insert(0, DATOS[0])
                self.txt_Ape2.insert(0, DATOS[1])
                self.txt_nom.insert(0, DATOS[2])
                self.txt_dir.insert(0, DATOS[3])
                self.txt_curp.insert(0 ,DATOS[4])

        def INSERT(self):
                ARRAY_DATOS = []

                APELLIDO_P = self.txt_Ape1.get()
                APELLIDO_M = self.txt_Ape2.get()
                NOMBRES = self.txt_nom.get()
                DIRECCION = self.txt_dir.get()
                CURP = self.txt_curp.get()
                RFC = self.txt_rfc.get()
                
                ARRAY_DATOS = [APELLIDO_P, APELLIDO_M, NOMBRES, DIRECCION, CURP, RFC]

                Controlador.INSERT(ARRAY_DATOS)

        def SCAN_RFC(self):
                Controlador.SELECT_ALL()