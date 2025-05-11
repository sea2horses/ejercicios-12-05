#En una campaña de donación de sangre en un hospital de Estelí, los datos de los donantes se
#almacenan en una pila según el orden en que se procesan. Si ocurre un problema técnico, se debe
#revertir el último registro. Implementa un sistema para registrar donantes (push), eliminar el último
#(pop), y mostrar el donante actual en proceso.

from pila_definicion import Pila

while True ():
    print ("\nSistema de Donación de Sangre\n1. Agregar Donante\n2. Mostrar Donante Actual\n3. Eliminar Último Donante\n4. Salir")
    opcion = int(input("> "))
    if opcion is 1:
        nombre = input("Ingrese el nombre del donante: ")
        edad = int(input("Ingrese la edad del donante: "))
        grupo_sanguineo = input("Ingrese el grupo sanguíneo del donante: ")
        donante = Donante(nombre, edad, grupo_sanguineo)
        pila_donantes.push(donante)

    