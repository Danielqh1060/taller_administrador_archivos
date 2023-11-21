from tkinter import *
from tkinter import simpledialog
import os
from FuncionesAdministrador import *

class InterfazAdmin:
    def __init__(self, root):
        self.root = root
        self.inicializar_interfaz()
        self.ruta_actual = os.path.abspath("")

    def inicializar_interfaz(self):
        self.root.geometry("1000x600")
        self.root.title("Proyecto Administrador de Archivos")
        self.root.resizable(0, 0)

        # Cuadro de texto para la ruta
        self.entry_ruta = Entry(self.root)
        self.entry_ruta.place(x=5, y=5, width=800, height=30)

        # Botones
        boton1 = Button(self.root, text="Crear Archivos", command=self.crear_archivo_interfaz)
        boton1.place(x=330, y=280)

        boton2 = Button(self.root, text="Crear Directorio", command=self.crear_directorio_interfaz)
        boton2.place(x=470, y=280)

        boton3 = Button(self.root, text="Eliminar Archivo", command=self.eliminar_archivo_interfaz)
        boton3.place(x=620, y=280)

        boton4 = Button(self.root, text="Eliminar Directorio", command=self.eliminar_directorio_interfaz)
        boton4.place(x=780, y=280)

        boton5 = Button(self.root, text="Renombrar Archivo", command=self.renombrar_archivo_interfaz)
        boton5.place(x=330, y=330)

        boton6 = Button(self.root, text="Renombrar Directorio", command=self.renombrar_directorio_interfaz)
        boton6.place(x=500, y=330)

        boton7 = Button(self.root, text="Mostrar Arbol de Directorios", command=self.mostrar_arbol_interfaz)
        boton7.place(x=680, y=330)

        boton8 = Button(self.root, text="Buscar Archivo", command=self.buscar_archivo_interfaz)
        boton8.place(x=550, y=400)

        boton9 = Button(self.root, text="Salir", command=self.root.destroy)
        boton9.place(x=930, y=520)

        # Cuadro de texto para mensajes
        self.texto = Text(self.root)
        self.texto.place(x=5, y=40, width=200, height=400)

        # Cuadro de texto para mostrar el árbol
        self.texto2 = Text(self.root)
        self.texto2.place(x=230, y=50, width=650, height=200)

    def obtener_ruta_actual(self):
        return self.ruta_actual

    def establecer_ruta_actual(self, nueva_ruta):
        self.ruta_actual = os.path.abspath(nueva_ruta)

    def mostrar_mensaje(self, mensaje):
        self.texto.insert(END, mensaje + "\n")

    def limpiar_mensajes(self):
        self.texto.delete(1.0, END)

    def crear_archivo_interfaz(self):
        ruta_archivo = self.obtener_ruta_actual()

        if ruta_archivo:  # Asegúrate de que la ruta no esté vacía
            crear_archivo(ruta_archivo)
            self.limpiar_mensajes()
            self.mostrar_mensaje(f"Archivo en la ruta {ruta_archivo} creado correctamente")
        else:
            self.mostrar_mensaje("Error: La ruta del archivo está vacía.")

    def crear_directorio_interfaz(self):
        ruta_directorio = self.obtener_ruta_actual()

        if ruta_directorio:  # Asegúrate de que la ruta no esté vacía
            crear_directorio(ruta_directorio)
            self.limpiar_mensajes()
            self.mostrar_mensaje(f"Directorio en la ruta {ruta_directorio} creado correctamente")
        else:
            self.mostrar_mensaje("Error: La ruta del directorio está vacía.")

    def eliminar_archivo_interfaz(self):
        ruta_archivo = self.obtener_ruta_actual()
        eliminar_archivo(ruta_archivo)
        self.limpiar_mensajes()
        self.mostrar_mensaje(f"Archivo en la ruta {ruta_archivo} eliminado correctamente")

    def eliminar_directorio_interfaz(self):
        ruta_directorio = self.obtener_ruta_actual()
        eliminar_directorio(ruta_directorio)
        self.limpiar_mensajes()
        self.mostrar_mensaje(f"Directorio en la ruta {ruta_directorio} eliminado correctamente")

    def renombrar_archivo_interfaz(self):
        ruta_archivo = self.obtener_ruta_actual()
        nuevo_nombre = simpledialog.askstring("Renombrar Archivo", "Ingrese el nuevo nombre:")
        renombrar_archivo(ruta_archivo, nuevo_nombre)
        self.limpiar_mensajes()
        self.mostrar_mensaje(f"Archivo en la ruta {ruta_archivo} renombrado correctamente")

    def renombrar_directorio_interfaz(self):
        ruta_directorio = self.obtener_ruta_actual()
        nuevo_nombre = simpledialog.askstring("Renombrar Directorio", "Ingrese el nuevo nombre:")
        renombrar_directorio(ruta_directorio, nuevo_nombre)
        self.limpiar_mensajes()
        self.mostrar_mensaje(f"Directorio en la ruta {ruta_directorio} renombrado correctamente")

    def mostrar_arbol_interfaz(self):
        ruta_directorio = self.obtener_ruta_actual()
        arbol = construir_arbol_directorio(ruta_directorio)
        self.limpiar_mensajes()
        self.mostrar_mensaje("Árbol de directorios:")
        self.mostrar_arbol(arbol)

    def mostrar_arbol(self, nodo, nivel=0):
        prefijo = "|   " * nivel + "|-- " if nivel > 0 else ""
        tipo = " [Directorio]" if nodo.es_directorio else ""
        mensaje = prefijo + nodo.nombre + tipo
        self.texto2.insert(END, mensaje + "\n")
        for hijo in nodo.hijos:
            self.mostrar_arbol(hijo, nivel + 1)

    def buscar_archivo_interfaz(self):
        nombre_archivo = simpledialog.askstring("Buscar Archivo", "Ingrese el nombre del archivo:")
        ruta_directorio = self.obtener_ruta_actual()
        ruta_encontrada = buscar_archivo(ruta_directorio, nombre_archivo)
        self.limpiar_mensajes()
        if ruta_encontrada:
            self.mostrar_mensaje(f"Archivo encontrado en la ruta: {ruta_encontrada}")
        else:
            self.mostrar_mensaje(f"Archivo no encontrado")

if __name__ == "__main__":
    root = Tk()
    interfaz = InterfazAdmin(root)
    root.mainloop()
