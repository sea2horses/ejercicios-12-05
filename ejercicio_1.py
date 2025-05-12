''' Una oficina de atención ciudadana en una alcaldía municipal en Nicaragua recibe documentos para
 revisión. Por cada solicitud, se apilan los documentos entregados en el orden en que llegan. El
 personal debe revisar el último documento entregado primero. Se debe simular el proceso de
 revisión, utilizando una pila, y permitir agregar nuevos documentos, eliminar el último revisado y
 mostrar los pendientes.
'''

from pila_definicion import Pila

# Clase de Documentos
class Documento:
    # Constructor
    def __init__(self, titulo, descripcion):
        self.Titulo = titulo
        self.Descripcion = descripcion
    
    # Método Imprimir
    def show(self):
        print(f"&{self.Titulo}\n\n-{self.Descripcion}")

# Obtener Documento
def obtener_documento() -> Documento:
    print("Ingrese el asunto del Documento")
    titulo = input("> ")
    
    print("Ingrese la descripción del Documento")
    descripcion = input("> ")
    
    return Documento(titulo, descripcion)
        
if __name__ == "__main__":
    documentos = Pila()
    
    while True:
        print("\nManejador de Documentos\n1. Agregar Documento\n2. Revisar Último Documento\n3. Eliminar Último Documento\n4. Mostrar Pendientes\n5. Salir ->")
        
        opcion = int(input("> "))
        
        if opcion == 1:
            documentos.push(obtener_documento())
        elif opcion == 2:
            if documentos.length() > 0:
                documentos.top().show()
            else:
                print("No hay documentos para mostrar!")
        elif opcion == 3:
            if documentos.length() > 0:
                documentos.pop().show()
                print("Documento eliminado de manera exitosa")
            else:
                print("No hay documentos para eliminar")
        elif opcion == 4:
            print(f"Cantidad de Documentos Pendientes: {documentos.length()}")
        elif opcion == 5:
            break
        else:
            print("La opción ingresada no es válida!")