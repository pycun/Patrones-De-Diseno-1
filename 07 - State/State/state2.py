from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"La máquina cambio su estado a {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def moneda(self):
        self._state.handle1()

    def empujar(self):
        self._state.handle2()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""


class Bloqueado(State):
    def handle1(self) -> None:
        print("Se inserta moneda a máquina Bloqueada")
        print("Se activa mecanismo")
        self.context.transition_to(Desbloqueado())

    def handle2(self) -> None:
        print("Se empuja a máquina Bloqueada")


class Desbloqueado(State):
    def handle1(self) -> None:
        print("Se inserta moneda a máquina Desbloqueada")

    def handle2(self) -> None:
        print("Se empuja a máquina Desbloqueada")
        print("Se activa mecanismo")
        self.context.transition_to(Bloqueado())


if __name__ == "__main__":
    # The client code.

    maquina = Context(Bloqueado())
    maquina.moneda()
    maquina.moneda()