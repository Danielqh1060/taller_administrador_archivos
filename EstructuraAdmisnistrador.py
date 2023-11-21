# Arbol de directorios , Estructura

class Nodo:
    def __init__(self, nombre, es_directorio=False):
        self.nombre = nombre
        self.es_directorio = es_directorio
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

