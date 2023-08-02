from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Constructor(ABC):
    """
    La interfaz Constructor especifica los métodos para crear las diferentes partes de
    los objetos Producto.
    """

    @property
    @abstractmethod
    def producto(self):
        pass

    @abstractmethod
    def producir_parte_a(self):
        pass

    @abstractmethod
    def producir_parte_b(self):
        pass

    @abstractmethod
    def producir_parte_c(self):
        pass


class ProductoConstructor(Constructor):
    """
    Las clases ConstructorConcreto siguen la interfaz Constructor y proveen
    implementaciones específicas de los pasos de construcción. Tu programa puede
    tener varias variaciones de Constructores, implementadas de manera diferente.
    """

    def __init__(self):
        """
        Una instancia de constructor recién creada contiene un objeto producto en blanco,
        que se usará para su posterior ensamblaje.
        """
        self.reiniciar()

    def reiniciar(self):
        self._producto = Producto()

    @property
    def producto(self) -> Producto:
        """
        Los Constructores Concretos deben proveer sus propios métodos para obtener resultados.
        Esto se debe a que distintos tipos de constructores pueden crear productos completamente
        diferentes que no siguen la misma interfaz. Por lo tanto, dichos métodos no pueden ser
        declarados en la interfaz Constructor base (al menos en lenguajes de programación de tipado
        estático).

        Usualmente, después de regresar el resultado final al cliente, se espera que una instancia
        del constructor esté lista para empezar a producir otro producto. Por eso es una práctica
        común llamar al método reiniciar al final del cuerpo del método getProduct. Sin embargo,
        este comportamiento no es obligatorio y puedes hacer que tus constructores esperen una
        llamada explícita de reiniciar por parte del código cliente antes de deshacerse del resultado
        anterior.
        """
        producto = self._producto
        self.reiniciar()
        return producto

    def producir_parte_a(self):
        self._producto.agregar("ParteA")

    def producir_parte_b(self):
        self._producto.agregar("ParteB")

    def producir_parte_c(self):
        self._producto.agregar("ParteC")


class Producto():
    """
    Tiene sentido usar el patrón Constructor solo cuando los productos son bastante complejos
    y requieren una extensa configuración.

    A diferencia de otros patrones creacionales, diferentes constructores concretos pueden producir
    productos no relacionados. En otras palabras, los resultados de distintos constructores pueden
    no siempre seguir la misma interfaz.
    """

    def __init__(self):
        self.piezas = []

    def agregar(self, parte: Any):
        self.piezas.append(parte)

    def listar_partes(self):
        print(f"Partes del producto: {', '.join(self.piezas)}", end="")


class Director:
    """
    El Director solo es responsable de ejecutar los pasos de construcción en un
    orden particular. Es útil cuando se producen productos según un orden o
    configuración específicos. Estrictamente hablando, la clase Director es opcional,
    ya que el código cliente puede controlar los constructores directamente.
    """

    def __init__(self):
        self._constructor = None

    @property
    def constructor(self) -> Constructor:
        return self._constructor

    @constructor.setter
    def constructor(self, constructor: Constructor):
        """
        El Director trabaja con cualquier instancia de constructor que el código cliente le pase.
        De esta manera, el código cliente puede alterar el tipo final del producto recién ensamblado.
        """
        self._constructor = constructor

    """
    El Director puede construir varias variaciones del producto utilizando los mismos
    pasos de construcción.
    """

    def construir_producto_minimo_viable(self):
        self.constructor.producir_parte_a()

    def construir_producto_completo(self):
        self.constructor.producir_parte_a()
        self.constructor.producir_parte_b()
        self.constructor.producir_parte_c()


if __name__ == "__main__":
    """
    El código cliente crea un objeto constructor, lo pasa al director e inicia el proceso de construcción.
    El resultado final se obtiene del objeto constructor.
    """

    director = Director()
    constructor = ProductoConstructor()
    director.constructor = constructor

    print("\nProducto básico estándar: ")
    director.construir_producto_minimo_viable()
    constructor.producto.listar_partes()

    print("\nProducto completo estándar: ")
    director.construir_producto_completo()
    constructor.producto.listar_partes()

    # Recuerda, el patrón Constructor puede usarse sin una clase Director.
    print("\nProducto personalizado: ")
    constructor.producir_parte_a()
    constructor.producir_parte_b()
    constructor.producto.listar_partes()

    print("\n")
