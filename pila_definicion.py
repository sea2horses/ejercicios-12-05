# Creamos el nodo elemental de una pila
class Nodo:
  # Constructor constructor

  # Como es LIFO, en lugar de siguiente, usamos anterior
  # de esta manera, el elemento cabeza es el último en lugar del primero
  def __init__(self, valor, anterior):
    self.Valor = valor
    self.Anterior = anterior


class Pila:
  # Let's go
  def __init__(self):
    self.Cabeza = None
    self.Tamaño = 0
  
  # Push
  # Agrega un valor a la pila
  def push(self, valor):
    # Creamos el nuevo nodo y como será la cabeza le ponemos la cabeza actual de nodo anterior
    nuevo_nodo: Nodo = Nodo(valor, self.Cabeza)
    # Asignamos la cabeza al nuevo nodo
    self.Cabeza = nuevo_nodo
    # ACtualizamos el tamaño
    self.Tamaño += 1
  
  # Pop
  # Retorna la cabeza quitandola de la pila
  def pop(self):
    # Si ya no hay elementos tira una excepción
    if self.Cabeza == None:
      raise Exception("illegal pop in stack")
    # Obtenemos el nodo cabeza actual
    vieja_cabeza = self.Cabeza
    # Ahora actualizamos la cabeza para ser el nodo anterior
    self.Cabeza = vieja_cabeza.Anterior
    # Actualizamos el tamaño
    self.Tamaño -= 1
    # Retornamos el valor de la cabeza vieja
    return vieja_cabeza.Valor
  
  # Top
  # Retorna la cabeza sin quitarla de la pila
  def top(self):
    # Si ya no hay elementos tira una excepción
    if self.Cabeza == None:
      raise Exception("illegal top in stack")
    return self.Cabeza.Valor
  
  # Length
  # Devuelve el tamaño
  def length(self):
    return self.Tamaño
  
  # Print
  # Imprime la pila
  def print(self):
    
    # Debido a como funcionan las pilas, necesitamos una lista temporal para imprimirla ordenada
    temp = []
    
    actual = self.Cabeza
    
    while actual != None:
      temp.insert(0, actual.Valor)
      actual = actual.Anterior
    
    print(temp)