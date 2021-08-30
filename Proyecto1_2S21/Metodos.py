from xml.dom import minidom

from graphviz import Digraph

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
        try:
            terrenos = docXML.getElementsByTagName("terrenos")[0]
        except:
            terrenos = docXML.getElementsByTagName("TERRENOS")[0]
        listaTerrenos = terrenos.getElementsByTagName("terreno")
        if len(listaTerrenos) == 0 or listaTerrenos is None:
            listaTerrenos = terrenos.getElementsByTagName("TERRENO")
        for terreno in listaTerrenos:
            try:
                nombre = terreno.getAttribute("nombre")
            except:
                nombre = terreno.getAttribute("NOMBRE")
            if self.listaS.buscarNombres(nombre):
                print("La lista con el nombre: " + nombre + "ya existe!!")
            else:
                try:
                    listadimension = terreno.getElementsByTagName("dimension")[0]
                except:
                    listadimension = terreno.getElementsByTagName("DIMENSION")[0]
                try:
                    xDimension = listadimension.getElementsByTagName("m")[0]
                except:
                    xDimension = listadimension.getElementsByTagName("M")[0]
                xDim = int(xDimension.firstChild.data)
                try:
                    yDimension = listadimension.getElementsByTagName("n")[0]
                except:
                    yDimension = listadimension.getElementsByTagName("N")[0]
                yDim = int(yDimension.firstChild.data)
                try:
                    listaPosicionIni = terreno.getElementsByTagName("posicioninicio")[0]
                except:
                    listaPosicionIni = terreno.getElementsByTagName("POSICIONINICIO")[0]
                try:
                    X0_ini0 = listaPosicionIni.getElementsByTagName("x")[0]
                except:
                    X0_ini0 = listaPosicionIni.getElementsByTagName("X")[0]
                x_ini = X0_ini0.firstChild.data
                try:
                    Y0_ini0 = listaPosicionIni.getElementsByTagName("y")[0]
                except:
                    Y0_ini0 = listaPosicionIni.getElementsByTagName("Y")[0]
                y_ini = Y0_ini0.firstChild.data
                try:
                    listaPosicioFin = terreno.getElementsByTagName("posicionfin")[0]
                except:
                    listaPosicioFin = terreno.getElementsByTagName("POSICIONFIN")[0]
                try:
                    X0_fin0 = listaPosicioFin.getElementsByTagName("x")[0]
                except:
                    X0_fin0 = listaPosicioFin.getElementsByTagName("X")[0]
                x_fin = X0_fin0.firstChild.data
                try:
                    Y0_fin0 = listaPosicioFin.getElementsByTagName("y")[0]
                except:
                    Y0_fin0 = listaPosicioFin.getElementsByTagName("Y")[0]
                y_fin = Y0_fin0.firstChild.data
                try:
                    listaPosiciones = terreno.getElementsByTagName("posicion")
                except:
                    listaPosiciones = terreno.getElementsByTagName("POSICION")
                # -------------------------------------------------
                # CONTABILIZACION DE X's y Y's PARA CREAR CABECERAS
                # -------------------------------------------------
                i = 1  # filas Y
                j = 1  # columnas X
                for posicion in listaPosiciones:
                    try:
                        x_pos = int(posicion.getAttribute("x"))
                    except:
                        x_pos = int(posicion.getAttribute("X"))
                    try:
                        y_pos = int(posicion.getAttribute("y"))
                    except:
                        y_pos = int(posicion.getAttribute("Y"))
                    if x_pos == j:
                        if y_pos != i:
                            i += 1
                    else:
                        j += 1
                        i = 1
                if xDim == j and yDim == i:
                    self.matrizOrtogonal = MatrizOrtogonal()
                    self.matrizOrtogonal.crearCabeceras(yDim, xDim, x_ini, y_ini, x_fin, y_fin)
                    # -------------------------------------------------
                    # INSERCCIÓN DE LOS NODOS
                    # -------------------------------------------------
                    for posicion in listaPosiciones:
                        try:
                            x_pos = int(posicion.getAttribute("x"))
                        except:
                            x_pos = int(posicion.getAttribute("X"))
                        try:
                            y_pos = int(posicion.getAttribute("y"))
                        except:
                            y_pos = int(posicion.getAttribute("Y"))
                        valor = posicion.firstChild.data
                        casilla = Casilla(x_pos, y_pos, valor)
                        self.matrizOrtogonal.insertar(casilla)
                    self.listaS.insertar(nombre, self.matrizOrtogonal)
                else:
                    print("----->Error con dimensiones: " + nombre + "!")
        print(".....")
        print("----->Archivo Cargado Exitosamente!")
        self.listaS.imprimir()

    def graficarTerreno(self):
        print("Terrenos Registrados: ")
        self.listaS.imprimirSoloNombre()
        nombreTerreno = str(input("Ingrese nombre del Terreno: " + '\n'))
        print("----->Graficando Terreno...")
        print(".....")
        self.matrizOrtogonal = self.listaS.buscarTerreno(nombreTerreno)
        if self.matrizOrtogonal is None:
            print(".....")
            print("----->Error! terreno NO encontrado...")
        else:
            dot = Digraph(comment=nombreTerreno,
                          encoding='utf',
                          edge_attr={'color': '#999999', 'fontcolor': '#888888', 'fontsize': '10',
                                     'fontname': 'FangSong'}
                          )
            dot.attr(bgcolor='purple:skyblue', label="'" + nombreTerreno.upper() + "'", fontcolor='blue')
            # dot.graph_attr['rankdir'] = 'LR'
            auxf = self.matrizOrtogonal.Pivote
            valorArribaY = None
            contY = 0
            while auxf is not None:
                auxc = auxf
                valorAnteriorX = None
                contX = 0
                while auxc is not None:
                    pos_X = str(auxc.Casilla.posX)
                    pos_Y = str(auxc.Casilla.posY)
                    valor = auxc.Casilla.valor
                    iD = pos_X + "," + pos_Y
                    valorActualX = iD
                    valorActualY = iD
                    if valor == "P":
                        dot.node(iD, str(valor),
                                 {'shape': 'circle', 'color': 'pink', 'fontcolor': 'black'})
                        valorArribaY = iD
                        valorAnteriorX = iD
                    elif 'X' in valor:
                        with dot.subgraph() as inicial:
                            inicial.attr(rank='same')
                            inicial.node(iD, str(valor),
                                         {'shape': 'circle', 'color': 'white', 'fontcolor': 'blue'}, group=str(contX))
                            inicial.edge(valorAnteriorX, valorActualX)
                            inicial.edge(valorActualX, valorAnteriorX)
                            valorAnteriorX = iD
                    with dot.subgraph() as resto:
                        if 'Y' in valor:
                            resto.node(iD, str(valor),
                                       {'shape': 'circle', 'color': 'white', 'fontcolor': 'blue'})
                            resto.edge(valorArribaY, valorActualY)
                            resto.edge(valorActualY, valorArribaY)
                            valorArribaY = iD  # intacto-------------
                            valorAnteriorX = iD
                        if valor.isdigit():
                            with resto.subgraph() as resto2:
                                resto2.attr(rank='same')
                                resto2.node(iD, str(valor),
                                            {'shape': 'circle', 'color': 'pink', 'fontcolor': 'black'},
                                            group=str(contX))
                                auxArribaY = str(contX)+","+str(contY-1)
                                resto2.edge(valorAnteriorX, valorActualX)  # en fila en Y, anterior-actual
                                resto2.edge(valorActualX, valorAnteriorX)  # en fila en Y, actual-anterior
                                dot.edge(auxArribaY, valorActualY)  # en columna en X, arriba-actual
                                dot.edge(valorActualY, auxArribaY)  # en columna en X, actual-arriba
                                valorAnteriorX = iD
                    contX += 1
                    auxc = auxc.siguiente

                contY += 1
                auxf = auxf.abajo
            print(dot.source)
            dot.render(nombreTerreno, "C:\\Users\\Maria\\Desktop", view=True)
            print(".....")
            print("----->Terreno graficado Exitosamente!")
