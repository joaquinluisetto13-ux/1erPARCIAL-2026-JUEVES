class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None

class IteradorListaEnlazada:
    def __init__(self, cabeza):
        self.actual = cabeza

    def __iter__(self):
        return self

    def __next__(self):
        if not self.actual:
            raise StopIteration
        dato = self.actual.dato
        self.actual = self.actual.siguiente
        return dato

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def __iter__(self):
        return IteradorListaEnlazada(self.cabeza)