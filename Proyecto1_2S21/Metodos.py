from xml.dom import minidom

from Casilla import Casilla
from ListaSimple import ListaSimple


class Metodos:
    listaS = ListaSimple()

    def cargarArchivo(self):
        rutaArchivo = str(input("Ingrese la Ruta Completa de su Archivo: " + '\n'))
        print("----->Iniciando Carga de Datos...")
        print(".....")
        docXML = minidom.parse(rutaArchivo)
        terrenos = docXML.getElementsByTagName("terrenos")[0]
        listaTerrenos = terrenos.getElementsByTagName("terreno")
        for terreno in listaTerrenos:
            nombre = terreno.getAttribute("nombre")
            if self.listaS.buscarNombres(nombre):
                print("La lista con el nombre: " + nombre + "ya existe!!")
            else:
                listaPosicionIni = terreno.getElementsByTagName("posicioninicio")[0]
                X0_ini0 = listaPosicionIni.getElementsByTagName("x")[0]
                x_ini = X0_ini0.firstChild.data
                Y0_ini0 = listaPosicionIni.getElementsByTagName("y")[0]
                y_ini = Y0_ini0.firstChild.data
                listaPosicioFin = terreno.getElementsByTagName("posicionfin")[0]
                X0_fin0 = listaPosicioFin.getElementsByTagName("x")[0]
                x_fin = X0_fin0.firstChild.data
                Y0_fin0 = listaPosicioFin.getElementsByTagName("y")[0]
                y_fin = Y0_fin0.firstChild.data
                listaPosiciones = terreno.getElementsByTagName("posicion")
                # print("nombre", nombre)
                # print("IniX", str(x_ini), "IniY", str(y_ini))
                # print("FinX", str(x_fin), "FinY", str(y_fin))
                for posicion in listaPosiciones:
                    x_pos = posicion.getAttribute("x")
                    y_pos = posicion.getAttribute("y")
                    valor = posicion.firstChild.data
                    # print("x:", x_pos,"y:",y_pos,"val:",valor)
                    casilla = Casilla(x_pos,y_pos,valor)

