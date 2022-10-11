from tkinter import *
from tkinter import ttk
import tkinter as tk
from Control import Controlador
from tkinter import messagebox
class Insert():
        def ventana_reg(self):
                self.registrar = Toplevel()
                self.registrar.geometry("420x430")
                self.registrar.resizable(width=False, height=False)
                self.registrar.title("Registrar Cliente")
                #Background
                #fondo = Image.open('Fotos/fondo.jpg')
                #render_fondo = ImageTk.PhotoImage(fondo)
                #Label(self.registrar, image=render_fondo).pack(anchor="nw")

                #NOTEBOOK
                self.notebook = ttk.Notebook(self.registrar)
                self.notebook.place(x=0, y=0)

                # Crea frames
                self.frame1 = ttk.Frame(self.notebook, width=420, height=430)
                self.frame2 = ttk.Frame(self.notebook, width=420, height=430)

                self.frame1.pack(fill='both', expand=True)
                self.frame2.pack(fill='both', expand=True)
                
                #--------------------------------------Empieza frame 1-------------------------------------
                #Labelframe Datos Personales
                self.labelframe1 = LabelFrame(self.frame1, text="Seleccion de Imagene", width=400, height=100)
                self.labelframe1.place(x=10, y=10)

                #Boton para seleccionar foto de INE
                self.btn_ine = tk.Button(self.frame1, text='Seleccionar INE', width=44,bg="#DCD7D7", command=self.Selecciona_INE)
                self.btn_ine.place(x=40, y=40, width=160, height=40)

                #Boton para seleccionar foto de RFC
                self.btn_rfc = tk.Button(self.frame1, text='Seleccionar RFC', width=44,bg="#DCD7D7", command=self.Selecciona_RFC)
                self.btn_rfc.place(x=220, y=40, width=160, height=40)

                #Labelframe escaneo
                self.labelframe1 = LabelFrame(self.frame1, text="Escaneo de Datos", width=400, height=200)
                self.labelframe1.place(x=10, y=120)

                #Boton Escanear Nombre
                self.btn_nombre = tk.Button(self.frame1, text="Escanear Nombre", bg="#DCD7D7", compound = TOP, command=self.scan_Nombre)
                self.btn_nombre.place(x=40, y=140, width=160, height=40)

                #Boton Escanear Direccion
                self.btn_dir = tk.Button(self.frame1, text="Escanear Direccion", bg="#DCD7D7", compound=LEFT, command=self.scan_dir)
                self.btn_dir.place(x=220, y=140, width=160, height=40)

                #Boton Escanear CURP
                self.btn_curp = tk.Button(self.frame1, text="Escanear CURP", bg="#DCD7D7", compound=LEFT, command=self.scan_CURP)
                self.btn_curp.place(x=40, y=200, width=160, height=40)

                #Boton Escanear RFC
                self.btn_srfc = tk.Button(self.frame1, text="Escanear RFC", bg="#DCD7D7", compound = TOP, command=self.rellena_RFC)
                self.btn_srfc.place(x=220, y=200, width=160, height=40)
                
                #Boton Escanear Fecha de Nacimiento
                self.btn_fn = tk.Button(self.frame1, text="Fecha de Nacimiento", bg="#DCD7D7", compound = TOP, command=self.scan_Fecha_Nac)
                self.btn_fn.place(x=40, y=260, width=160, height=40)

                #Boton Escanear vigencia
                self.btn_vig = tk.Button(self.frame1, text="Vigencia INE", bg="#DCD7D7", compound = TOP, command=self.scan_vigencia)
                self.btn_vig.place(x=220, y=260, width=160, height=40)

                #--------------------------------------Acaba frame 1----------------------------------------------------------------
                #--------------------------------------Empieza frame 2--------------------------------------------------------------
                # Añade frames al notebook

                #Apellido Paterno
                self.lb_ape1 = ttk.Label(self.frame2, text="Apellido Paterno", width=15)
                self.lb_ape1.place(x=20, y=20)

                self.Ape1 = StringVar()
                self.txt_Ape1 = ttk.Entry(self.frame2, textvariable=self.Ape1, width=30)
                self.txt_Ape1.place(x=150, y=20)

                #Apellido Materno
                self.lb_ape2 = ttk.Label(self.frame2, text="Apellido Materno", width=15)
                self.lb_ape2.place(x=20, y=50)
                
                Ape2 = StringVar()
                self.txt_Ape2 = ttk.Entry(self.frame2, textvariable=Ape2, width=30)
                self.txt_Ape2.place(x=150, y=50)

                #Nombre
                self.lb_nom = ttk.Label(self.frame2, text="Nombre(s)", width=15)
                self.lb_nom.place(x=20, y=80)
                
                self.Nom = StringVar()
                self.txt_nom = ttk.Entry(self.frame2, textvariable=self.Nom, width=30)
                self.txt_nom.place(x=150, y=80)
                #Fecha Nacimiento
                self.lb_fn = ttk.Label(self.frame2, text="Fecha de Nacimiento", width=30)
                self.lb_fn.place(x=20, y=110)

                self.FN = StringVar()
                self.txt_fn = ttk.Entry(self.frame2, textvariable=self.FN, width=30)
                self.txt_fn.place(x=150, y=110)
                #Nombre Completo
                self.lb_NC = ttk.Label(self.frame2, text="Nombre Completo", width=30)
                self.lb_NC.place(x=20, y=140)

                self.NC = StringVar()
                self.txt_NC = tk.Text(self.frame2, width=23, height=3)
                self.txt_NC.place(x=150, y=140)

                #Direccion
                self.lb_dir = ttk.Label(self.frame2, text="Direccion", width=15)
                self.lb_dir.place(x=20, y=200)
                
                self.Dir = StringVar()
                self.txt_dir = tk.Text(self.frame2, width=23, height=3)
                self.txt_dir.place(x=150, y=200)

                #CURP
                self.lb_curp = ttk.Label(self.frame2, text="CURP", width=15)
                self.lb_curp.place(x=20, y=260)
                
                self.CURP = StringVar()
                self.txt_curp = ttk.Entry(self.frame2, textvariable=self.CURP, width=30)
                self.txt_curp.place(x=150, y=260)

                #RFC
                self.lb_curp = ttk.Label(self.frame2, text="RFC", width=15)
                self.lb_curp.place(x=20, y=290)
                
                self.RFC = StringVar()
                self.txt_rfc = ttk.Entry(self.frame2, textvariable=self.RFC, width=30)
                self.txt_rfc.place(x=150, y=290)

                #Vigencia
                self.lb_vig = ttk.Label(self.frame2, text="Vigencia", width=15)
                self.lb_vig.place(x=20, y=320)

                self.vig = StringVar()
                self.txt_vig = ttk.Entry(self.frame2, textvariable=self.vig, width=30)
                self.txt_vig.place(x=150, y=320)

                #Boton REGISTRAR
                self.img_guardar = PhotoImage(file="Fotos/save.png")
                self.btn_guardar = ttk.Button(self.frame2, image=self.img_guardar, text="Registrar Cliente", compound = LEFT, command=self.INSERT)
                self.btn_guardar.place(x=100, y=360, width=200, height=40)

                #--------------------------------------Acaba frame 2--------------------------------------------------------------
                self.notebook.add(self.frame1, text='ESCANEO')
                self.notebook.add(self.frame2, text='DATOS')

        def Selecciona_INE(self):
                Controlador.Controller_INE()
                self.btn_ine.configure(bg="green")
        def Selecciona_RFC(self):
                Controlador.Controller_RFC()
                self.btn_rfc.configure(bg="green")
        def INSERT(self):
                ARRAY_DATOS = []

                APELLIDO_P = self.txt_Ape1.get()
                APELLIDO_M = self.txt_Ape2.get()
                NOMBRES = self.txt_nom.get()
                NOMBRE_C = self.txt_NC.get("1.0", END)
                DIRECCION = self.txt_dir.get("1.0", END)
                FECHA_N = self.txt_fn.get()
                CURP = self.txt_curp.get()
                VIGENCIA = self.txt_vig.get()
                RFC = self.txt_rfc.get()
                
                DIRECCION = str.split(DIRECCION)
                DIRECCION2 = ""
                DIRECCION2=' '.join([str(elem) for elem in DIRECCION])
                
                ARRAY_DATOS = [APELLIDO_P, APELLIDO_M, NOMBRES, NOMBRE_C, DIRECCION2, FECHA_N, CURP, VIGENCIA,RFC]

                self.txt_Ape1.delete(0, 'end')
                self.txt_Ape2.delete(0, 'end')
                self.txt_nom.delete(0, 'end')
                self.txt_NC.delete("1.0", END)
                self.txt_dir.delete("1.0", END)
                self.txt_fn.delete(0, 'end')
                self.txt_curp.delete(0, 'end')
                self.txt_vig.delete(0, 'end')
                self.txt_rfc.delete(0, 'end')

                Controlador.INSERT(ARRAY_DATOS)


        def rellena_RFC(self):
                RFC = Controlador.Controller_Scan_RFC()
                self.txt_rfc.insert(0 , RFC)
                self.btn_srfc.configure(bg="green")
        def scan_Nombre(self):                
                Nom = Controlador.Controller_Scan()

                #Array con el nombre en diferentes posiciones
                Nombre = str.split(Nom)
                print(Nombre)
                
                #Separar Nombres y juntarlos en un string
                x = len(Nombre)
                if x==4:
                        Nom_u = str(Nombre[2]+' '+Nombre[3])

                self.txt_Ape1.insert(0, Nombre[0])
                self.txt_Ape2.insert(0, Nombre[1])
                self.txt_nom.insert(0, Nom_u)
                self.txt_NC.insert(tk.INSERT, Nombre)
                self.btn_nombre.configure(bg="green")
        def scan_dir(self):
                Direccion = Controlador.Controller_Scan()
                
                arr_dir = []
                dir=''
                for i in Direccion:
                        if i in ['.']:
                                #arr_dir.append(i)
                                dir=dir+i
                                break
                        if i in ['\n']:
                                i=', '
                                #arr_dir.append(i)
                                dir=dir+i
                        else:
                                #arr_dir.append(i)
                                dir=dir+i

                dir = str.split(dir)
                print(dir)
                self.txt_dir.insert(tk.INSERT, dir)
                self.btn_dir.configure(bg="green")
        def scan_CURP(self):
                curp = Controlador.Controller_Scan()
                curp2 = str.split(curp)
                
                print(curp2)

                curp3 = list(curp)
                print(curp3)
                try:
                        if self.año <= 2000:
                                print("Abajo de 2000")
                                if curp3[16] in "O":
                                        curp3[16] = "0"
                                if curp3[16] in "I":
                                        curp3[16] = "1"
                                if curp3[16] in "T":
                                        curp3[16] = "7"
                                if len(curp3) >=18:
                                        curp3.pop()
                        if self.año >= 2000:
                                print("Arriba de 2000")
                except AttributeError:
                        messagebox.showinfo("Fecha de Nacimiento necesaria","Es necesario primero escanear la fecha de nacimiento")
                        return
                curp2 = ""

                for i in curp3:
                        curp2 = curp2+i

                self.txt_curp.insert(0, curp2)
                self.btn_curp.configure(bg="green")
        
        def scan_Fecha_Nac(self):
                FN = Controlador.Controller_Scan()
                Array_Fecha = []
                Fecha_corregida = []
                Fecha_final = ""
                x = 0
                for i in FN:
                        if i in ['\n']:
                                continue
                        if i in ['/']:
                                Array_Fecha.append("-")
                        else:
                                Array_Fecha.append(i)

                #año
                Fecha_corregida.append(Array_Fecha[6])
                Fecha_corregida.append(Array_Fecha[7])
                Fecha_corregida.append(Array_Fecha[8])
                Fecha_corregida.append(Array_Fecha[9])
                #mes
                Fecha_corregida.append(Array_Fecha[2])
                Fecha_corregida.append(Array_Fecha[3])
                Fecha_corregida.append(Array_Fecha[4])
                #dia
                Fecha_corregida.append(Array_Fecha[5])
                Fecha_corregida.append(Array_Fecha[0])
                Fecha_corregida.append(Array_Fecha[1])

                for i in Fecha_corregida:
                        Fecha_final = Fecha_final+i

                self.año = Fecha_corregida[0]+Fecha_corregida[1]+Fecha_corregida[2]+Fecha_corregida[3]
                self.año = int(self.año)
                
                self.txt_fn.insert(0, Fecha_final)
                self.btn_fn.configure(bg="green")

        def scan_vigencia(self):
                vig = Controlador.Controller_Scan()
                vig = str.split(vig)
                self.txt_vig.insert(0, vig)
                self.btn_vig.configure(bg="green")