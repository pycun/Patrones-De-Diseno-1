"""
La interfaz Comando normalmente declara un único método para ejecutar el comando.

Step #1
Declara la interfaz de comando con un único método de ejecución.


"""
from abc import ABC, abstractmethod


class ICommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass