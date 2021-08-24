from Casilla import Casilla
from NodoOrtogonal import NodoOrtogonal


class MatrizOrtogonal:

    def __init__(self, f=None, c=None):
        self.Pivote = None
        self.primeroX = None
        self.primeroY = None
        self.tamY = 0
        self.tamX = 0
        self.tamG = 0

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

    def crearCabeceras(self, tamFil, tamCol):
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

    # ----------------------------------------------------------------

