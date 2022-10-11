import pymysql
import easygui
import cv2
import pytesseract
from PIL import Image
from tkinter import messagebox
class Modelo:
    INE = ''
    Foto_RFC = ''
    Conn = None

    def Select_INE():
        global INE
        INE = easygui.fileopenbox()
        print(INE)
    def Select_RFC():
        global Foto_RFC
        Foto_RFC = easygui.fileopenbox()
        print(Foto_RFC)
    
    def Muestra_img(tipo):
        global INE
        global Foto_RFC

        valor = 'INE'
        try:
            if tipo == valor:
                imagen = Image.open(INE)
                imagen.show()
            else:
                imagen = Image.open(Foto_RFC)
                imagen.show()
        except NameError:  
            print("No se selecciono una imagen")
        else:
            print("Fine")
    def Scan_RFC():
        global Foto_RFC
        
        #read image
        img_raw = cv2.imread(Foto_RFC)
        roi = cv2.selectROI(img_raw)

        roi_cropped = img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

        #cv2.imshow("ROI", roi_cropped)
        #cv2.waitKey(0)
        cv2.destroyAllWindows()

        #pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
        text = pytesseract.image_to_string(roi_cropped, lang='spa')
        print(text)
        return text

    def Scan():
        global INE
    
        #read image
        img_raw = cv2.imread(INE)
        roi = cv2.selectROI(img_raw)

        roi_cropped = img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

        cv2.destroyAllWindows()

        text = pytesseract.image_to_string(roi_cropped, lang='spa')
        print(text)
        return text

    def Conexion(DATOS):
        global Conn
        print(DATOS)
        host1 = DATOS[0]
        user1 = DATOS[1]
        passw = DATOS[2]
        try:
            Conn = pymysql.connect(host = host1,
                                    user = user1,
                                    password = passw,
                                    db='sed')
            print("Conectado con exito")
            return Conn
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
                        messagebox.showerror("Error de Conexion", "Error al conectar a la base de datos")
                        print("Ocurrió un error al conectar: ", e)
    
    def INSERT(DATOS):
        
        APELLIDO_P = DATOS[0]
        APELLIDO_M = DATOS[1]
        NOMBRES    = DATOS[2]
        NOMBRE_C   = DATOS[3] 
        DIRECCION  = DATOS[4]
        FECHA_N    = DATOS[5]
        CURP       = DATOS[6]
        VIGENCIA   = DATOS[7]
        RFC        = DATOS[8]
        global INE
        global Foto_RFC
        STATUS = 1

        #print(APELLIDO_P, APELLIDO_M, NOMBRES, NOMBRE_C, DIRECCION, FECHA_N, CURP, VIGENCIA, RFC, INE, STATUS)
        global Conn
        #conexion_sql = Modelo.Conexion()
        conexion_sql = Conn
        cursor = conexion_sql.cursor()
        consulta = "INSERT INTO clientes(APELLIDO_P, APELLIDO_M, NOMBRES, NOMBRE_C, DIRECCION, FECHA_N, CURP, VIGENCIA_INE, RFC, FOTO_INE, FOTO_RFC, STATUS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

        try: INE
        except NameError: INE = None
        
        if len(RFC) == 0:
            
            Foto_RFC = None
            RFC = "PENDIENTE"
        
        #print(INE)
        cursor.execute(consulta, (APELLIDO_P, APELLIDO_M, NOMBRES, NOMBRE_C, DIRECCION, FECHA_N, CURP, VIGENCIA, RFC, INE, Foto_RFC, STATUS))
        conexion_sql.commit()
        messagebox.showinfo("REGISTRO EXITOSO", "El Cliente ah sido registrado con exito")
        #cursor.close()
        #conexion_sql.close()
    
    def Select_all():
        global Conn
        conexion_sql = Conn
        #conexion_sql = Modelo.Conexion()
        cursor = conexion_sql.cursor()
        consulta = "select ID, APELLIDO_P, APELLIDO_M, NOMBRES , DIRECCION, FECHA_N, CURP, VIGENCIA_INE, RFC from clientes where STATUS = 1;"

        cursor.execute(consulta)
        
        rows = cursor.fetchall()

        return rows
 
    def Buscar(cadena, tipo):
        global Conn
        #conexion_sql = Modelo.Conexion()
        conexion_sql = Conn
        cursor = conexion_sql.cursor()

        nombre = "Nombre"
        ape = "Apellido"
        curp = "CURP"
        rfc = "RFC"
        id = "ID"
        consulta = ""

        if tipo == nombre:
            consulta = "select * from clientes where NOMBRES LIKE %s;"
        elif tipo == ape:
            consulta = "select * from clientes where APELLIDO_P LIKE %s;"
        elif tipo == curp:
            consulta = "select * from clientes where CURP LIKE %s;"
        elif tipo == rfc:
            consulta = "select * from clientes where RFC LIKE %s;"
        elif tipo == id:
            consulta = "select * from clientes where id= %s;"
        
        cursor.execute(consulta, (cadena))
        rows = cursor.fetchall()
        return rows
    
    def modificar(self, DATOS):
        
        ID = DATOS[0]
        APELLIDO_P = DATOS[1]
        APELLIDO_M = DATOS[2]
        NOMBRES    = DATOS[3]
        NOMBRE_C   = DATOS[4] 
        DIRECCION  = DATOS[5]
        CURP       = DATOS[6]
        RFC        = DATOS[7]

        #conexion = Modelo.Conexion()
        global Conn
        conexion = Conn
        cursor = conexion.cursor()

        query = "UPDATE clientes SET APELLIDO_P = %s, APELLIDO_M = %s, NOMBRES = %s, NOMBRE_C = %s, DIRECCION = %s, CURP = %s, RFC = %s WHERE ID = %s;"
        cursor.execute(query, (APELLIDO_P, APELLIDO_M, NOMBRES, NOMBRE_C, DIRECCION, CURP, RFC, ID))
        conexion.commit()
    
    def Eliminar(self, id):
        
        #conexion = Modelo.Conexion()
        global Conn
        conexion = Conn
        cursor = conexion.cursor()
        eliminado = 0

        query = "UPDATE clientes SET STATUS = %s WHERE ID = %s;"
        cursor.execute(query, (eliminado, id))
        conexion.commit()