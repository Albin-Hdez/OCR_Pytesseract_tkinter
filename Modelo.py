import pymysql
import easygui
import cv2
import numpy as np
import pytesseract
from PIL import Image
class Modelo:
    INE = ''
    RFC = ''

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
        global RFC

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
        print(x)
        if x==4:
            INSERT=[Nombre[0],Nombre[1],Nombre[2]+' '+Nombre[3], dir, CURP[0]]
            #print(INSERT)
            Nombres = str(Nombre[2]+' '+Nombre[3])
            ARRAY_DATOS = [Nombre[0],Nombre[1],Nombres, dir, CURP[0]]
            return ARRAY_DATOS
            #BD.insert(Nombre[0],Nombre[1],Nombres, dir, CURP[0])
        if x==3:
            INSERT=[Nombre[0],Nombre[1],Nombre[2], dir, CURP[0]]
            #print(INSERT)
            ARRAY_DATOS = [Nombre[0],Nombre[1],Nombre[2], dir, CURP[0]]
            return ARRAY_DATOS
            #BD.insert(Nombre[0],Nombre[1],Nombre[2], dir, CURP[0])