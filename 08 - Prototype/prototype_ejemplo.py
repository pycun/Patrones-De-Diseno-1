from abc import ABCMeta, abstractmethod
import copy


class IProtoType(metaclass=ABCMeta):
    """Interfaz con método de clonación"""
    @staticmethod
    @abstractmethod
    def clone():
        """El clon, va a depender de cómo tú
         quieras implementar los detalles en su clase concreta"""


class ConcreteClass1(IProtoType):
    """concrete class 1"""

    def __init__(self, i=0, s="", l=[], d={}):
        self.i = i
        self.s = s
        self.l = l
        self.d = d

    def clone(self):
        return type(self)(
            self.i,
            self.s,
            copy.deepcopy(self.l),
            copy.deepcopy(self.d))

    def __str__(self):
        return f"{id(self)}\ti={self.i}\ti={self.s}\tl{self.l}\t{self.d}"


class ConcreteClass2(IProtoType):
    """concrete class 2"""

    def __init__(self, i=0, s="", l=[], d={}):
        self.i = i
        self.s = s
        self.l = l
        self.d = d

    def clone(self):
        return type(self)(
            self.i,
            self.s,
            copy.deepcopy(self.l),
            copy.deepcopy(self.d))

    def __str__(self):
        return f"{id(self)}\ti={self.i}\ti={self.s}\tl{self.l}\t{self.d}"


if __name__ == "__main__":
    OBJECT1 = ConcreteClass1(1, "OBJECT1", [[1,2,3], 2, 3], {"a": 1, "b": 2, "c": 3})
    print(OBJECT1)
    OBJECT2 = OBJECT1.clone()
    OBJECT2.s = "OBJEC2"
    OBJECT2.l[0][0] = 10
    print(OBJECT2)
    print(OBJECT1)




