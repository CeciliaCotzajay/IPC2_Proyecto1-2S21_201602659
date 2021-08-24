from xml.dom import minidom

from Casilla import Casilla
from ListaSimple import ListaSimple
from MatrizOrtogonal import MatrizOrtogonal


class Metodos:
    listaS = ListaSimple()
    matrizOrtogonal = None

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
                """print("nombre", nombre)
                 print("IniX", str(x_ini), "IniY", str(y_ini))
                 print("FinX", str(x_fin), "FinY", str(y_fin))"""
                # #
                # CONTABILIZACION DE X's y Y's PARA CREAR CABECERAS
                # #
                i = 1  # filas Y
                j = 1  # columnas X
                for posicion in listaPosiciones:
                    x_pos = int(posicion.getAttribute("x"))
                    y_pos = int(posicion.getAttribute("y"))
                    if x_pos == j:
                        if y_pos != i:
                            i += 1
                    else:
                        j += 1
                        i = 1
                    """valor = posicion.firstChild.data
                    print("x:", x_pos,"y:",y_pos,"val:",valor)
                print("x:", j, "y:", i)"""
                self.matrizOrtogonal = MatrizOrtogonal()
                self.matrizOrtogonal.crearCabeceras(i, j)
