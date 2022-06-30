"""
Los Comandos Concretos implementan varios tipos de solicitudes.

Un comando concreto no se supone que tenga que realizar el trabajo por su cuenta,
sino pasar la llamada a uno de los objetos de la lógica de negocio.

Sin embargo, para lograr simplificar el código, estas clases se pueden fusionar.

Casi cualquier objeto puede actuar como receptor. La mayoría de los comandos solo
gestiona los detalles sobre cómo se pasa una solicitud al receptor, mientras que
el propio receptor hace el trabajo real.
"""
from abc import abstractmethod

from src.interfaces import ICommand


class BasicOperatorCommand(ICommand):
    def __init__(self, receiver, app, num: float):
        # receiver
        self._receiver = receiver

        # params
        self._num = num
        self._app = app
        # ...

        # local variables
        self.input = self._app.total
        self.result = None

    @property
    @abstractmethod
    def operator(self):
        pass

    @property
    def is_executed(self) -> bool:
        return self.result is not None

    def _can_be_executed(self):
        return True

    def __str__(self):
        return F"{self.input} {self.operator} {self._num} = {self.result}"


class AddCommand(BasicOperatorCommand):
    operator = '+'

    def execute(self) -> None:
        self.result = self._app.total + self._num  # o self._receiver.action()
        self._app.total = self.result

    def undo(self) -> None:
        self.result = self._app.total - self._num  # o self._receiver.action()
        self._app.total = self.result


class SubtractCommand(BasicOperatorCommand):
    operator = '-'

    def execute(self) -> None:
        self.result = self._app.total - self._num  # o self._receiver.action()
        self._app.total = self.result

    def undo(self) -> None:
        self.result = self._app.total + self._num  # o self._receiver.action()
        self._app.total = self.result


class MultiplyCommand(BasicOperatorCommand):
    operator = '*'

    def execute(self) -> None:
        self.result = self._app.total * self._num  # o self._receiver.action()
        self._app.total = self.result

    def undo(self) -> None:
        self.result = self._app.total / self._num  # o self._receiver.action()
        self._app.total = self.result


class DivideCommand(BasicOperatorCommand):
    operator = '/'

    def execute(self) -> None:
        # NOTE: Se puede aplicar condicionales si se puede ejecutar el comando
        #  asi como si se puede des hacer. Tota esa lógica deberia ir en el receptor
        # self._can_be_executed()

        self.result = self._app.total / self._num  # o self._receiver.action()
        self._app.total = self.result

    def undo(self) -> None:
        self.result = self._app.total * self._num  # o self._receiver.action()
        self._app.total = self.result

