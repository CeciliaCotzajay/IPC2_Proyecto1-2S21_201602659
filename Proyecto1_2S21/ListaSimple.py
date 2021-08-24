from NodoSimple import NodoSimple


class ListaSimple:

    def __init__(self):
        self.primero = None
        self.tam = 0

    def insertar(self, noombre, matrizOrto):
        nuevo = NodoSimple(nombre=noombre, matrizOrtogonal=matrizOrto)
        if self.tam == 0:
            self.primero = nuevo
            self.tam += 1
        else:
            actual = self.primero
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
            self.tam += 1

    def buscarNombres(self, nombre):
        actual = self.primero
        if self.tam != 0:
            while actual is not None:
                if actual.nombre == nombre:
                    return True
                actual = actual.siguiente

    def buscarTerreno(self, nombre):
        matriz = None
        actual = self.primero
        if self.tam != 0:
            while actual is not None:
                if actual.nombre == nombre:
                    matriz = actual.matrizOrto
                actual = actual.siguiente
        return matriz

    def imprimir(self):
        if self.tam == 0:
            print("----->La lista esta Vacia")
            return
        else:
            actual = self.primero
            while actual is not None:
                print(actual.nombre, ":", actual.matrizOrto.tamN)
                actual.matrizOrto.graficarMatriz()
                print("    ↓ ")
                actual = actual.siguiente

    def imprimirSoloNombre(self):
        if self.tam == 0:
            print("----->No tiene Terrenos Registrados!!")
            return
        else:
            actual = self.primero
            cont = 1
            while actual is not None:
                print(str(cont)+":", actual.nombre)
                actual = actual.siguiente
