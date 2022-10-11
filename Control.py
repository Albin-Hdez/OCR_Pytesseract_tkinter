import Modelo

class Controlador:
    
    INE = ''
    RFC = ''
    
    def Controller_INE():
        Modelo.Modelo.Select_INE()

    def Controller_RFC():
        Modelo.Modelo.Select_RFC()

    def Controller_img(valor):
        Modelo.Modelo.Muestra_img(valor)
        print(valor)

    def Controller_Scan():
        DATOS = Modelo.Modelo.Scan()
        return DATOS
    def Controller_Scan_RFC():
        RFC = Modelo.Modelo.Scan_RFC()
        return RFC
    def INSERT(ARRAY_DATOS):
        Modelo.Modelo.INSERT(ARRAY_DATOS)

    def SELECT_ALL():
        DATOS = Modelo.Modelo.Select_all()
        return DATOS
    def Buscar(cadena, tipo):
        DATOS = Modelo.Modelo.Buscar(cadena, tipo)
        return DATOS
    def modificar(DATOS):
        UP = Modelo.Modelo
        UP.modificar(0, DATOS)
    def Eliminar(id):
        DEL = Modelo.Modelo
        DEL.Eliminar(0, id)
    def Login(DATOS):
        M = Modelo.Modelo
        M.Conexion(DATOS)