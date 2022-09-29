# Singleton en Python


![whoisam](../img/only_instance.png)

## *¿Qué es?*
	
Es un patron de diseño creacional que garantiza que exista un solo objeto de su tipo 
y proporciona un único punto de acceso para cualquier otro código.


```{admonition} Patron de diseño creacional
Definen como puede crearse un objeto. Lo que incluye ailsar los detalles
de la creación del objeto, de forma que su código no dependa de otros y, por lo tanto, no deba
ser modificado al añadir información.
```


![comic-singleton](../img/singleton-comic-es.png)

## *¿Qué resuelve?*

El motivo más habitual es control el acceso a algún recurso compartido, por ejemplo,
una Base de Datos o un archivo.

## *¿Cómo funciona?*

Has creado un objeto y al cabo de un rato decides crear otro nuevo. En lugar de recibir
un objeto nuevo, obtendrás el que ya habias creado el cual fue gardado en caché.

<img src="_images/moe_and_barney.jpg"  width="30%"/>

## *Pros VS Contra*

| Pros | Contras |
| --- | --- |
| Puedes tener la certeza de que una clase tiene una única instancia. | Vulnera el Principio de responsabilidad única. El patrón resuelve dos problemas al mismo tiempo. |
|El objeto Singleton solo se inicializa cuando se requiere por primera vez. | El patrón requiere de un tratamiento especial en un entorno con múltiples hilos de ejecución, para que varios hilos no creen un objeto Singleton varias veces.|


## *Ejemplo:*

```python
class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """

        # ...


if __name__ == "__main__":
    # The client code.

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
```


## *Links de referencia*

[Creando un Singleton](https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python)

[¿Qué son las metaclasses en Python?](https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python)


