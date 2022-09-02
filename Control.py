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
        Modelo.Modelo.Scan_INE()

