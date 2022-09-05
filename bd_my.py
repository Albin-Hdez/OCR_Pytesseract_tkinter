import pymysql
from PIL import Image, ImageTk
imagen = Image.open('Fotos/albin.jpg')
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='sed')
	try:
		with conexion.cursor() as cursor:
			consulta = "INSERT INTO clientes(APELLIDO_P, APELLIDO_M, NOMBRES, DIRECCION, CURP, RFC, FOTO_INE, FOTO_RFC, STATUS)\
						+VALUES (%s);"
            
			cursor.execute(consulta, (imagen))
		conexion.commit()
	finally:
		conexion.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)