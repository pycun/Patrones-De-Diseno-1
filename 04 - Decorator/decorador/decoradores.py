from abc import ABC, abstractclassmethod, abstractmethod
#Definimos una clase que herede de nuestra clase abstracta cafe
from abc import abstractmethod
from cafe import Cafe

#Creamos una Clase abstracta que hereda de cafe va definir 2 metodos abstractos
#es la Clase Base de todas nuestras clases decoradoras
class Extra(Cafe):
    @abstractmethod
    def get_descripcion(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def calcular_costo(self) -> float:
        raise NotImplementedError

#esta clase hereda de "Extra"
class CremaBatida(Extra):
    #Implementamos sus 2 metodos abstractos de la clase heredada

    #Recibimos un objecto
        def __init__(self, cafe: Cafe) -> None:
        #lo que hacemos en el constructor es guardar una copia del original
            self._cafe = cafe

        def get_descripcion(self) -> str:
            return f"{self._cafe.get_descripcion()},con crema batida"

        def calcular_costo(self) -> float:
            return self._cafe.calcular_costo() + 1.0


class Leche(Extra):

        def __init__(self, cafe: Cafe) -> None:
            self._cafe = cafe

        def get_descripcion(self) -> str:
            return f"{self._cafe.get_descripcion()},con Leche"

        def calcular_costo(self) -> float:
            return self._cafe.calcular_costo() + .5

