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

    def Controller_Scan_INE():
        DATOS = Modelo.Modelo.Scan_INE()
        return DATOS
    
    def INSERT(ARRAY_DATOS):
        Modelo.Modelo.INSERT(ARRAY_DATOS)

    def SELECT_ALL():
        DATOS = Modelo.Modelo.Select_all()
        return DATOS
    def Buscar(cadena, tipo):
        DATOS = Modelo.Modelo.Buscar(cadena, tipo)
        return DATOS
       
