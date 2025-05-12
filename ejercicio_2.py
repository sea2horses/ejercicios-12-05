'''
En una panadería tradicional en León, los panes recién horneados se apilan en una bandeja. El
primero que se vende es el último que se colocó. Simula el proceso de agregar panes a la bandeja
(push), vender uno (pop), y visualizar qué tipo de pan está listo para vender (peek).
'''

from pila_definicion import Pila

class Pan:
    # Constructor
    def __init__(self, nombre, precio):
        self.Nombre = nombre
        self.Precio = precio

if __name__ == "__main__":
    
    panes = Pila()
    
    while True:
        print("\n-- Panadería --\n1. Agregar un pan\n2.")