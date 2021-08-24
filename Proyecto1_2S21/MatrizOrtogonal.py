from Casilla import Casilla
from NodoOrtogonal import NodoOrtogonal


class MatrizOrtogonal:

    def __init__(self):
        self.Pivote = None
        self.primeroX = None
        self.primeroY = None
        self.x_ini = 0
        self.y_ini = 0
        self.x_fin = 0
        self.y_fin = 0
        self.tamY = 0  # TAMAÑO DE CABECERAS EN Y
        self.tamX = 0  # TAMAÑO DE CABECERAS EN X
        self.tamN = 0  # TAMAÑO DE NODOS (CANTIDAD DE NODOS)
        self.tamG = 0  # TAMAÑO GENERAL (PIVOTE,CABECERAS Y NODOS)

    # ************************************************************************
    # --------------------------CABECERAS-------------------------------------
    # ************************************************************************

    def insertarPivote(self, casilla):
        pivote = NodoOrtogonal(Casilla=casilla)
        self.Pivote = pivote

    def insertarCabeceraY(self, casilla):
        nuevo = NodoOrtogonal(Casilla=casilla)
        if self.tamY == 0:
            self.primeroY = nuevo
            self.Pivote.abajo = self.primeroY
            self.tamY += 1
            self.tamG += 1
        else:
            actual = self.primeroY
            while actual.abajo:
                actual = actual.abajo
            actual.abajo = nuevo
            nuevo.arriba = actual
            self.tamY += 1
            self.tamG += 1

    def insertarCabeceraX(self, casilla):
        nuevo = NodoOrtogonal(Casilla=casilla)
        if self.tamX == 0:
            self.primeroX = nuevo
            self.Pivote.siguiente = self.primeroX
            self.tamX += 1
            self.tamG += 1
        else:
            actual = self.primeroX
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            nuevo.anterior = actual
            self.tamX += 1
            self.tamG += 1

    def obtenerCabeceraY(self, valY):
        cabeceraY = None
        if self.tamY != 0:
            actualY = self.primeroY
            while actualY is not None:
                if actualY.Casilla.posY == valY and actualY.Casilla.posX == 0:
                    cabeceraY = actualY
                actualY = actualY.abajo
        return cabeceraY

    def obtenerCabeceraX(self, valX):
        cabeceraX = None
        if self.tamX != 0:
            actualX = self.primeroX
            while actualX is not None:
                if actualX.Casilla.posX == valX and actualX.Casilla.posY == 0:
                    cabeceraX = actualX
                actualX = actualX.siguiente
        return cabeceraX

    def crearCabeceras(self, tamFil, tamCol, xI, yI, xF, yF):
        self.x_ini = xI
        self.y_ini = yI
        self.x_fin = xF
        self.y_fin = yF
        casillaPivote = Casilla(0, 0, "P")
        self.insertarPivote(casillaPivote)
        if tamFil != 0:
            contf = 1
            while contf <= tamFil:
                casilla = Casilla(0, contf, "Y")
                self.insertarCabeceraY(casilla)
                contf += 1
        else:
            print("El número de filas es 0")
        if tamCol != 0:
            contc = 1
            while contc <= tamCol:
                casilla = Casilla(contc, 0, "X")
                self.insertarCabeceraX(casilla)
                contc += 1
        else:
            print("El número de columnas es 0")
        self.primeroX = self.Pivote.siguiente
        self.primeroY = self.Pivote.abajo

    # ************************************************************************
    # --------------------------RESTO_NODOS-----------------------------------
    # ************************************************************************

    def insertar(self, casilla):
        valY = casilla.posY
        valX = casilla.posX
        nuevo = NodoOrtogonal(Casilla=casilla)
        primeroY = self.obtenerCabeceraY(valY)
        primeroX = self.obtenerCabeceraX(valX)
        # --------------SI NO HAY NUNGUNO---------------
        if self.tamN == 0:
            primeroY.siguiente = nuevo
            nuevo.anterior = primeroY
            #
            primeroX.abajo = nuevo
            nuevo.arriba = primeroX
            self.tamN += 1
        else:
            # -------------------------RECORRIDO EN Y---------------------------------
            self.subInserccionY(primeroY, valX, nuevo)
            # -------------------------RECORRIDO EN X---------------------------------
            self.subInserccionX(primeroX, valY, nuevo)

    # -----------------------------------------------
    # -------------INSERCCION EN (Y,X)---------------
    # -----------------------------------------------

    def subInserccionY(self, primeroY, valX, nuevo):
        # -------------------------RECORRIDO EN Y---------------------------------
        actualY = primeroY
        while actualY is not None:
            # LOS VALORES DE auxY SON EL TIPO DE OPCIÓN QUE SE ENCUENTRA EN LA
            # IMAGEN S1.png
            if valX < actualY.Casilla.posX and actualY.anterior is primeroY:
                # auxY = 1
                primeroY.siguiente = nuevo
                nuevo.anterior = primeroY
                nuevo.siguiente = actualY
                actualY.anterior = nuevo
                return
            elif valX < actualY.Casilla.posX and actualY.anterior is not primeroY:
                # auxY = 2
                if valX > actualY.anterior.Casilla.posX:
                    auxAnterior = actualY.anterior
                    auxAnterior.siguiente = nuevo
                    nuevo.anterior = auxAnterior
                    nuevo.siguiente = actualY
                    actualY.anterior = nuevo
                    return
            elif valX > actualY.Casilla.posX and actualY.siguiente is None:
                # auxY = 3
                # aux = actualY.siguiente
                actualY.siguiente = nuevo
                nuevo.anterior = actualY
                return
            elif actualY.siguiente is None:
                # auxY = 4
                primeroY.siguiente = nuevo
                nuevo.anterior = primeroY
                return
            actualY = actualY.siguiente

    def subInserccionX(self, primeroX, valY, nuevo):
        actualX = primeroX
        while actualX is not None:
            # LOS VALORES DE auxY SON EL TIPO DE OPCIÓN QUE SE ENCUENTRA EN LA
            # IMAGEN S2.png
            if valY < actualX.Casilla.posY and actualX.arriba is primeroX:
                # auxY = 1
                primeroX.abajo = nuevo
                nuevo.arriba = primeroX
                nuevo.abajo = actualX
                actualX.arriba = nuevo
                self.tamN += 1
                return
            elif valY < actualX.Casilla.posY and actualX.arriba is not primeroX:
                # auxY = 2
                if valY > actualX.anterior.Casilla.posY:
                    auxAnterior = actualX.arriba
                    auxAnterior.abajo = nuevo
                    nuevo.arriba = auxAnterior
                    nuevo.abajo = actualX
                    actualX.arriba = nuevo
                    self.tamN += 1
                    return
            elif valY > actualX.Casilla.posY and actualX.abajo is None:
                # auxY = 3
                # aux = actualX.abajo
                actualX.abajo = nuevo
                nuevo.arriba = actualX
                self.tamN += 1
                return
            elif actualX.abajo is None:
                # auxY = 4
                primeroX.abajo = nuevo
                nuevo.arriba = primeroX
                self.tamN += 1
                return
            actualX = actualX.abajo

    # ************************************************************************
    # ------------------------METODOS-AUXILIARES------------------------------
    # ************************************************************************

    def graficarMatriz(self):
        auxf = self.Pivote
        while auxf is not None:
            auxc = auxf
            cad = ""
            while auxc is not None:
                cad += auxc.Casilla.valor + '\t'
                auxc = auxc.siguiente
            print(cad)
            auxf = auxf.abajo
