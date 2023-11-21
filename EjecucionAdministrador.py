from FuncionesAdministrador import *
from InterfazAdministrador import *

#Pruebas

ruta_directorio_raiz = "C:/Users/57311/Desktop/Prueba_Proyecto"

prueba_crear_archivo =  "C:/Users/57311/Desktop/Prueba_Proyecto/hola2.txt"

prueba_eliminar_archivo = "C:/Users/57311/Desktop/Prueba_Proyecto/hola2.txt"

prueba_crear_directorio =  "C:/Users/57311/Desktop/Prueba_Proyecto/3"

prueba_eliminar_directorio = "C:/Users/57311/Desktop/Prueba_Proyecto/3"

archivo = "hola2.txt"

prueba_renombrar_archivo = "C:/Users/57311/Desktop/Prueba_Proyecto/hola2.txt"

nombre_nuevo_archivo = "hola3.txt"

prueba_renombrar_directorio = "C:/Users/57311/Desktop/Prueba_Proyecto/3"

nombre_nuevo_directorio = "4"

#Menu del administrador de archivos Para pruebas, debe hacerse estas funciones desde La interfaz grafica

def menu():
    while True:
        print("Bienvenido al administrador de archivos")
        print("1. Crear Archivo")
        print("2. Crear directorio")
        print("3. Eliminar archivo")
        print("4. Eliminar directorio")
        print("5. Renombrar archivo")
        print("6. Renombrar directorio")
        print("7. Mostrar el arbol de directorios")
        print("8. Abrir administrador de archivos graficamente") 
        print("9. Salir")

        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            crear_archivo(prueba_crear_archivo)
            print("\n")
            pass
        elif opcion == 2:
            crear_directorio(prueba_crear_directorio)
            print("\n")
            pass
        elif opcion == 3:
            eliminar_archivo(prueba_eliminar_archivo)
            print("\n")
            pass
        elif opcion == 4:
            eliminar_directorio(prueba_eliminar_directorio)
            print("\n")
            pass
        elif opcion == 5:
            renombrar_archivo(prueba_renombrar_archivo, nombre_nuevo_archivo)
            print("\n")
            pass
        elif opcion == 6:
            renombrar_directorio(prueba_renombrar_directorio, nombre_nuevo_directorio)
            print("\n")
            pass
        elif opcion == 7:
            arbol = construir_arbol_directorio(ruta_directorio_raiz)
            mostrar_arbol(arbol)
            pass
        elif opcion == 8:
            interfaz()
            break
        elif opcion == 9:
            print("Hasta pronto")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu()

