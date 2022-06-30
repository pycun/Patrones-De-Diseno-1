"""
Con el patrón Command podemos realizar operaciones reversibles.


El historial de comando es una pila que contiene todos los objetos de comando
ejecutados junto a copias de seguridad relacionadas del estado de la aplicación.

Existen dos desventajas:
    - No es tan fácil guardar el estado de una aplicación, porque parte de ella
        puede ser privada.
        Este problema puede mitigarse con el patrón Memento.

    - Las copias de seguridad de estado pueden consumir mucha memoria RAM. Por
        lo tanto, en ocasiones puedes recurrir a una implementación alternativa: 
        en lugar de restaurar el estado pasado, el comando realiza la operación
        inversa, aunque ésta también tiene un precio, ya que puede resultar
        difícil o incluso imposible de implementar.


"""


class CommandHistory:
    def __init__(self):
        self.__history = []

    def push(self, command):
        self.__history.append(command)

    def pop(self):
        if not self.__history:
            return
        return self.__history.pop()

