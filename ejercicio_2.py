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
    
    def show(self):
        # Mostrar los datos del pan
        print(f"-- {self.Nombre} --\n:: {self.Precio:.2f}$\n")

def obtener_pan():
    print("Escriba el nombre del pan")
    nombre = input("> ")
    
    print("Escriba el precio del pan")
    precio = float(input("> "))
    
    return Pan(nombre, precio)

if __name__ == "__main__":
    
    panes = Pila()
    
    while True:
        print("\n-- Panadería --\n1. Agregar un pan\n2. Visualizar el pan listo para vender\n3. Vender pan\n4. Salir ->")
        
        opcion = int(input("> "))
        
        if opcion == 1:
            panes.push(obtener_pan())
        elif opcion == 2:
            if panes.length() > 0:
                panes.top().show()
            else:
                print("No hay pan listo para vender!")
        elif opcion == 3:
            if panes.length() > 0:
                pan_vendido = panes.pop()
                print(f"Pan ({pan_vendido.Nombre}) vendido satisfactoriamente! ({pan_vendido.Precio:.2f}$)")
            else:
                print("No hay pan para vender!")
        elif opcion == 4:
            break