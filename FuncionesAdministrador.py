import os
import shutil
from EstructuraAdmisnistrador import Nodo

#Imprimir el arbol como si fueran los directorios de un sistema operativo

def mostrar_arbol(nodo, nivel=0):
    prefijo = "|   " * nivel + "|-- " if nivel > 0 else ""
    tipo = " [Directorio]" if nodo.es_directorio else ""
    mensaje = prefijo + nodo.nombre + tipo
    print(mensaje)  # Puedes imprimir en la consola por ahora, o ajustar para que se muestre en la interfaz

    for hijo in nodo.hijos:
        mostrar_arbol(hijo, nivel + 1)
            
#Identifica si la ruta es un archivo o un directorio y los agrega al arbol de directorios
           
def construir_arbol_directorio(ruta_directorio):
    if not ruta_directorio:  # Asegúrate de que la ruta no esté vacía
        print("Error: La ruta del directorio está vacía.")
        return Nodo("Ruta vacía", es_directorio=True)

    if not os.path.exists(ruta_directorio):  # Asegúrate de que la ruta exista
        print(f"Error: La ruta del directorio '{ruta_directorio}' no existe.")
        return Nodo("Ruta no encontrada", es_directorio=True)

    try:
        lista_contenido = os.listdir(ruta_directorio)
    except Exception as e:
        print(f"Error: No se pudo obtener el contenido del directorio '{ruta_directorio}'.")
        print(f"Detalles del error: {e}")
        return Nodo("Error al obtener contenido", es_directorio=True)

    nodo_directorio = Nodo(ruta_directorio, es_directorio=True)

    for item_nombre in lista_contenido:
        item_ruta = os.path.join(ruta_directorio, item_nombre)

        if os.path.isdir(item_ruta):
            hijo_directorio = construir_arbol_directorio(item_ruta)
            nodo_directorio.agregar_hijo(hijo_directorio)
        else:
            hijo_archivo = Nodo(item_nombre)
            nodo_directorio.agregar_hijo(hijo_archivo)

    return nodo_directorio

#Funciones del administrador de archivos

#Funcion para eliminar un archivo de una ruta especifica
def eliminar_archivo(ruta_archivo):
    if os.path.isfile(ruta_archivo):
        os.remove(ruta_archivo)
        print(f"El archivo de la ruta {ruta_archivo} se ha eliminado correctamente")
    else:
        print("No se puede eliminar el archivo porque no existe")
        
#Funcion para eliminar un directorio de una ruta especifica        
def eliminar_directorio(ruta_directorio):
    if os.path.exists(ruta_directorio):
        try:
            # Usar shutil.rmtree para eliminar directorios no vacíos
            shutil.rmtree(ruta_directorio)
            print(f"El directorio en la ruta {ruta_directorio} se ha eliminado correctamente")
        except Exception as e:
            print(f"Error al eliminar el directorio: {e}")
    else:
        print("No se puede eliminar el directorio porque no existe")     

#Funcion para renombrar un archivo de una ruta especifica
def renombrar_archivo(ruta_archivo, nuevo_nombre):
    if os.path.isfile(ruta_archivo):
        directorio_original = os.path.dirname(ruta_archivo)
        nueva_ruta = os.path.join(directorio_original, nuevo_nombre)

        os.rename(ruta_archivo, nueva_ruta)
        print(f"El archivo se ha renombrado correctamente a {nuevo_nombre}")
    else:
        print("No se puede renombrar el archivo porque no existe")

#Funcion para renombrar un directorio de una ruta especifica
def renombrar_directorio(ruta_directorio, nuevo_nombre):
    if os.path.isdir(ruta_directorio):
        directorio_padre = os.path.dirname(ruta_directorio)
        nueva_ruta = os.path.join(directorio_padre, nuevo_nombre)

        os.rename(ruta_directorio, nueva_ruta)
        print(f"El directorio se ha renombrado correctamente a {nuevo_nombre}")
    else:
        print("No se puede renombrar el directorio porque no existe")
        
#Funcion para crear un directorio en una ruta especifica
def crear_archivo(ruta_archivo):
    if os.path.exists(ruta_archivo):
        print("El archivo ya existe en la ruta especificada.")
    else:
        try:
            with open(ruta_archivo, "w") as archivo:
                archivo.write("")  # Puedes escribir contenido inicial si lo deseas
            print(f"El archivo en la ruta {ruta_archivo} se ha creado correctamente")
        except Exception as e:
            print(f"Error al crear el archivo: {e}")
        
#Funcion para crear un directorio en una ruta especifica        
def crear_directorio(ruta_directorio):
    if os.path.isdir(ruta_directorio):
        print("El directorio ya existe")
    else:
        os.mkdir(ruta_directorio)
        print(f"El directorio en la ruta {ruta_directorio} se ha creado correctamente")

def buscar_archivo(ruta_directorio, archivo_a_buscar):
    if not ruta_directorio:
        print("Error: La ruta del directorio está vacía.")
        return

    try:
        lista_contenido = os.listdir(ruta_directorio)
    except FileNotFoundError:
        print(f"Error: La ruta del directorio '{ruta_directorio}' no existe.")
        return

    encontrado = False

    for item_nombre in lista_contenido:
        if item_nombre == archivo_a_buscar:
            encontrado = True
            print(f"El archivo '{archivo_a_buscar}' se encuentra en la ruta: {os.path.join(ruta_directorio, archivo_a_buscar)}")
            break

    if not encontrado:
        print(f"No se encontró el archivo '{archivo_a_buscar}' en la ruta: {ruta_directorio}")