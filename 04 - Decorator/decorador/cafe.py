from abc import ABC, abstractclassmethod, abstractmethod
#from msilib.schema import Property

#Creamos la clase Abstracta
class Cafe(ABC):
        def __init__(self) -> None:
            #definimos sus propiedades del cafe
            #el cual es una propiedad privada
            self._descripcion = "Cualquier Cafe"

        #Definimos el getter y el setter de esta propiedad
        def set_descriptcion(self,valor:str) -> None:
            self._descripcion = valor
        
        def get_descripcion(self) -> str:
            return self._descripcion

        #Definimos un metodo abstracto que tendran que implementar las clases que hereden de esta clase
        @abstractmethod
        def calcular_costo(self) ->float:
            #lanzamos una excepcion si una clase intenta invocar este metodo y no a sido implementado correctamente
            raise NotImplementedError
        
#Definimos 2 clases que implemente esta clase

class Frappucino(Cafe):
    def __init__(self) -> None:
        self._descripcion = "Frappucino"
    
    def calcular_costo(self) -> float:
        return 1.99


class Latte(Cafe):
    def __init__(self) -> None:
        self._descripcion = "Latte"
    
    def calcular_costo(self) -> float:
        return 1.85
