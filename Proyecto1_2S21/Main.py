import sys

from Metodos import Metodos


class Main:
    metodos = Metodos()

    def __init__(self):
        self.presentacion()

    def presentacion(self):
        print("                                              ")
        print("                                              ")
        print("**********************************************")
        print("**********************************************")
        print("INTRODUCCIÓN A LA PROGRAMACIÓN Y COMPUTACIÓN 2")
        print("**********************************************")
        print("*************** Seccion E ********************")
        print("**********************************************")
        print("**********************************************")
        print("**********************************************")
        try:
            ter = input("--->>>>presione Cero 0 para continuar--->>>>     ")
            if ter == '0':
                self.presentacion()
        except:
            self.presentacion()

    def menuPrincipal(self):
        print("**********************************************")
        print("**************** PRINCIPAL *******************")
        print("**********************************************")
        print("1. Cargar archivo                             ")
        print("2. Procesar Archivo                           ")
        print("3. Escribir Archivo de Salida                 ")
        print("4. Mostrar datos del Estudiante               ")
        print("5. Generar gráfica                            ")
        print("6. Salir                                      ")
        try:
            opc = int(input("--->>>>Seleccione una opcion-------->>>>>>>>     "))

            # CARGAR ARCHIVO
            if opc == 1:
                print("**********************************************")
                self.metodos.cargarArchivo()
                self.continuar()
            # PROCESAR ARCHIVO
            elif opc == 2:
                print("**********************************************")
                self.metodos.procesarArchivo()
                self.continuar()
            # ESCRIBIR ARCHIVO
            elif opc == 3:
                print("**********************************************")
                self.metodos.escribirArchivo()
                self.continuar()
            # MOSTRAR DATOS
            elif opc == 4:
                print("**********************************************")
                self.mostrarDatos()
                self.continuar()
            # GENERAR GRAFICA
            elif opc == 5:
                print("No gráfica :(")
            # SALIDA
            elif opc == 6:
                print("**********************************************")
                sys.exit()
        except:
            print("                                            ")
            print("      !!!NO VALIDO, INTENTE NUEVAMENTE      ")
            self.menuPrincipal()

    def mostrarDatos(self):
        print("María Cecilia Cotzajay López", )
        print("201602659")
        print("Introducción a la Programacíon y Computación 2 \n Sección 'A' ")
        print("Ingeniería en Ciencias y Sistemas")
        print("4to Semestre")
        print("**********************************************")

    def continuar(self):
        regreso = input("--->>>>Presione cualquier tecla para Continuar--->>>>     ")
        if regreso == '0':
            self.menuPrincipal()
        else:
            self.menuPrincipal()


ipc2 = Main()
ipc2.presentacion()

# ----------------------------------------------------------------------------------------------------------------------
# PRESENTACIÓN DE PROYECTO
# MENU PRINCIPAL
# MÉTODO MOSTRAR DATOS
# MÉTODO CONTINUAR
# ----------------------------------------------------------------------------------------------------------------------
