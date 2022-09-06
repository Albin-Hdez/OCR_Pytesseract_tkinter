from tkinter import *
from tkinter import ttk, font
from turtle import width
from PIL import Image, ImageTk
from Control import Controlador

class Gestion_user():
    def Lista(self):
        
        self.Pantalla = Toplevel()
        self.Pantalla.geometry("1050x400")
        self.Pantalla.resizable(width=False, height=False)
        self.Pantalla.title("Gestion de Clientes")

        #Barra de Busqueda
        self.lb_busqueda = ttk.Label(self.Pantalla, text="Buscar: ", width=15)
        self.lb_busqueda.place(x=20, y=20)

        self.busqueda = StringVar()
        self.txt_busqueda = ttk.Entry(self.Pantalla, textvariable=self.busqueda, width=60)
        self.txt_busqueda.place(x=20, y=40)

        #Combobox Filtros
        self.lb_cb = ttk.Label(self.Pantalla, text="Filtro de Busqueda", width=30,anchor="w")
        self.lb_cb.place(x=400, y=20)
            
        self.cb_filtro = ttk.Combobox(self.Pantalla, state="readonly", values=["Nombre", "Apellido", "CURP", "RFC", "ID"], width=20)
        self.cb_filtro.current(0)
        self.cb_filtro.place(x=400, y=40, width=200, height=20)

        #Boton Buscar
        #img_save = PhotoImage(file="Fotos/save.png")
        self.btn_buscar = ttk.Button(self.Pantalla, text="Buscar",compound = LEFT, command=lambda: self.Buscar(self.txt_busqueda.get(), self.cb_filtro.get()))
        self.btn_buscar.place(x=610, y=20, width=200, height=40)

        #Boton Listar
        #img_save = PhotoImage(file="Fotos/save.png")
        self.btn_listar = ttk.Button(self.Pantalla, text="Listar Todos",compound = LEFT, command=self.Listar)
        self.btn_listar.place(x=820, y=20, width=200, height=40)

        # Tabla
        self.tabla = ttk.Treeview(self.Pantalla, columns=(1,2,3,4,5,6,7,8), show='headings', height=8)
        self.tabla.place(x=20, y=80, height=300)
        # self.tabla.grid(row=4,column=0,columnspan=0)

        self.tabla.column("1", width=40)
        self.tabla.column("2", width=150)
        self.tabla.column("3", width=150)
        self.tabla.column("4", width=150)
        self.tabla.column("5", width=200)
        self.tabla.column("6", width=150)
        self.tabla.column("7", width=150)
        self.tabla.column("8", width=10)

        self.tabla.heading("1",text="ID")
        self.tabla.heading("2",text="APELLIDO PATERNO")
        self.tabla.heading("3",text="APELLIDO MATERNO")
        self.tabla.heading("4",text="NOMBRE")
        self.tabla.heading("5",text="DIRECION")
        self.tabla.heading("6",text="CURP")
        self.tabla.heading("7",text="RFC")
        self.tabla.heading("8",text="STATUS")
        #self.tabla.pack()

        self.sb = Scrollbar(self.Pantalla, orient=VERTICAL)
        self.sb.place(x=1050, y=80)

        self.tabla.config(yscrollcommand=self.sb.set)
        self.sb.config(command=self.tabla.yview)

    def Listar(self):
        DATOS = Controlador.SELECT_ALL()
        
        for e in self.tabla.get_children():
            self.tabla.delete(e)
        
        for i in DATOS:
            self.tabla.insert("", END, values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[9]))
    
    def Buscar(self, cadena, tipo):
        print(cadena)
        print(tipo)
        DATOS = Controlador.Buscar(cadena, tipo)

        for e in self.tabla.get_children():
            self.tabla.delete(e)
        
        for i in DATOS:
            self.tabla.insert("", END, values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[9]))