from xml.dom import minidom


class Metodos:

    def cargarArchivo(self):
        rutaArchivo = str(input("Ingrese la Ruta Completa de su Archivo: " + '\n'))
        print("----->Iniciando Carga de Datos...")
        print(".....")
        docXML = minidom.parse(rutaArchivo)
        terrenos = docXML.getElementsByTagName("terrenos")[0]
        listaTerrenos = terrenos.getElementsByTagName("terreno")
        for terreno in listaTerrenos:
            nombre = terreno.getAttribute("nombre")