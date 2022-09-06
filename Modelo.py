from asyncio.windows_events import NULL
from pickle import GLOBAL
from zlib import DEF_BUF_SIZE
import pymysql
import easygui
import cv2
import numpy as np
import pytesseract
from PIL import Image
class Modelo:
    INE = ''
    Foto_RFC = ''

    def Select_INE():
        global INE
        INE = easygui.fileopenbox()
        print(INE)
    def Select_RFC():
        global RFC
        RFC = easygui.fileopenbox()
        print(RFC)
    
    def Muestra_img(tipo):
        global INE
        global Foto_RFC

        valor = 'INE'
        try:
            if tipo == valor:
                imagen = Image.open(INE)
                imagen.show()
            else:
                imagen = Image.open(RFC)
                imagen.show()
        except NameError:  
            print("No se selecciono una imagen")
        else:
            print("Fine")
    
    def Scan_INE():
        global INE
        pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'
        #read image
        img_raw = cv2.imread(INE)

        img_gris = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
        #select ROIs function
        ROIs = cv2.selectROIs("Select Rois",img_gris)

        #print rectangle points of selected roi
        print(ROIs)

        #Crop selected roi ffrom raw image

        #counter to save image with different name
        crop_number=0 

        #loop over every bounding box save in array "ROIs"
        arr=[]
        for rect in ROIs:
            x1=rect[0]
            y1=rect[1]
            x2=rect[2]
            y2=rect[3]

            #crop roi from original image
            img_crop=img_gris[y1:y1+y2,x1:x1+x2]
            text = pytesseract.image_to_string(img_crop, lang='spa')
            arr.append(text)
            cv2.imshow("crop"+str(crop_number),img_crop)
            #cv2.imwrite("crop"+str(crop_number)+".jpg",img_crop)
                
            crop_number+=1

        #hold window
        cv2.waitKey(0)

        #limpiar la cadena de texto por saltos de linea que se añaden
        #str.split GENERA UN ARREGLO SEPARANDO LAS PALABRAS DENTRO DE EL
        Nombre = str.split(arr[0])
        arr[0]=Nombre

        #Limpiar la direccion de saltos de linea
        direccion = []
        dir=''
        for i in arr[1]:
            if i in ['.']:
                direccion.append(i)
                dir=dir+i
                break
            if i in ['\n']:
                i=', '
                direccion.append(i)
                dir=dir+i
            else:
                direccion.append(i)
                dir=dir+i

        #Limpiar CURP de saltos de linea
        CURP = str.split(arr[2])
        #Limpiar fecha de nacimiento de salto de linea
        #FN = str.split(arr[3])

        x = len(Nombre)
        #print(x)
        if x==4:
            INSERT=[Nombre[0],Nombre[1],Nombre[2]+' '+Nombre[3], dir, CURP[0]]
            #print(INSERT)
            Nombres = str(Nombre[2]+' '+Nombre[3])
            return [Nombre[0],Nombre[1],Nombres, dir, CURP[0]]

        if x==3:
            INSERT=[Nombre[0],Nombre[1],Nombre[2], dir, CURP[0]]
            #print(INSERT)
            ARRAY_DATOS = [Nombre[0],Nombre[1],Nombre[2], dir, CURP[0]]
            return ARRAY_DATOS

    def Valida_INE(CURP):
        print(CURP)

    def Conexion():
        try:
            conexion = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='sed')
            print("Conectado con exito")
            return conexion
        except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
                        print("Ocurrió un error al conectar: ", e)
    
    def INSERT(DATOS):
        
        APELLIDO_P = DATOS[0]
        APELLIDO_M = DATOS[1]
        NOMBRES    = DATOS[2]
        DIRECCION  = DATOS[3]
        CURP       = DATOS[4]
        RFC        = DATOS[5]
        global INE
        global Foto_RFC
        STATUS = 1

        conexion_sql = Modelo.Conexion()
        cursor = conexion_sql.cursor()
        consulta = "INSERT INTO clientes(APELLIDO_P, APELLIDO_M, NOMBRES, DIRECCION, CURP, RFC, FOTO_INE, FOTO_RFC, STATUS) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"

        if len(RFC) == 0:
            
            Foto_RFC = None
            RFC = "PENDIENTE"

            cursor.execute(consulta, (APELLIDO_P, APELLIDO_M, NOMBRES, DIRECCION, CURP, RFC, INE, Foto_RFC, STATUS))
            print(Foto_RFC)

        else:
            cursor.execute(consulta, (APELLIDO_P, APELLIDO_M, NOMBRES, DIRECCION, CURP, RFC, INE, Foto_RFC, STATUS))

            print("todo bien")
    
    def Select_all():
        conexion_sql = Modelo.Conexion()
        cursor = conexion_sql.cursor()
        consulta = "select * from clientes;"

        cursor.execute(consulta)
        
        rows = cursor.fetchall()

        return rows
 
    def Buscar(cadena, tipo):
        conexion_sql = Modelo.Conexion()
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
        
        print(consulta)
        print(cadena)
        cursor.execute(consulta, (cadena))
        rows = cursor.fetchall()
        return rows
        
