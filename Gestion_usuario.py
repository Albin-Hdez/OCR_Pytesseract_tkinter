from msilib.schema import Control
from tkinter import *
from tkinter import ttk, font
from turtle import width
from PIL import Image, ImageTk
from Control import Controlador
from Insertar import Insert
from Editar import Edit
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
        self.txt_busqueda = ttk.Entry(self.Pantalla, textvariable=self.busqueda, width=30)
        self.txt_busqueda.place(x=20, y=40)

        #Combobox Filtros
        self.lb_cb = ttk.Label(self.Pantalla, text="Filtro de Busqueda", width=30,anchor="w")
        self.lb_cb.place(x=220, y=20)
            
        self.cb_filtro = ttk.Combobox(self.Pantalla, state="readonly", values=["Nombre", "Apellido", "CURP", "RFC", "ID"], width=20)
        self.cb_filtro.current(0)
        self.cb_filtro.place(x=220, y=40, width=100, height=20)

        #Boton Buscar
        self.img_buscar = PhotoImage(file="Fotos/lupa.png")
        self.btn_buscar = ttk.Button(self.Pantalla, text="Buscar", image=self.img_buscar, compound = LEFT, command=lambda: self.Buscar(self.txt_busqueda.get(), self.cb_filtro.get()))
        self.btn_buscar.place(x=340, y=20, width=100, height=40)

        #Boton refresh
        self.img_refresh = PhotoImage(file="Fotos/refresh.png")
        self.btn_refresh= ttk.Button(self.Pantalla, text="Recargar", image=self.img_refresh, compound = LEFT, command=self.Listar)
        self.btn_refresh.place(x=450, y=20, width=100, height=40)
        
        #Boton Registrar
        self.img_register = PhotoImage(file="Fotos/add.png")
        self.btn_registrar = ttk.Button(self.Pantalla, text="Registrar", image=self.img_register,compound=LEFT, command=self.insertar)
        self.btn_registrar.place(x=560, y=20, width=100, height=40)

        #Boton Editar
        self.img_edit = PhotoImage(file="Fotos/edit.png")
        self.btn_editar = ttk.Button(self.Pantalla, text="Editar", image=self.img_edit,compound=LEFT, command=self.editar)
        self.btn_editar.place(x=670, y=20, width=100, height=40)

        #Boton Eliminar
        self.img_del = PhotoImage(file="Fotos/bin.png")
        self.btn_del = ttk.Button(self.Pantalla, text="Eliminar", image=self.img_del,compound=LEFT)
        self.btn_del.place(x=780, y=20, width=100, height=40)

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
        DATOS = Controlador.Buscar(cadena, tipo)

        for e in self.tabla.get_children():
            self.tabla.delete(e)
        
        for i in DATOS:
            self.tabla.insert("", END, values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[9]))

    #Funciones Botones
    def insertar(self):
        ins = Insert()
        ins.ventana_reg()
    def editar(self):
        ins = Edit()
        ins.Pantalla_editar()