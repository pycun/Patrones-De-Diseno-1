class Subject:
    def __init__(self):
        # Inicializa la lista de observadores como vacía y el estado como nulo
        self.__observers = []
        self.__state = None
    
    def attach(self, observer):
        # Agrega un nuevo observador a la lista de observadores
        self.__observers.append(observer)
    
    def detach(self, observer):
        # Elimina un observador de la lista de observadores
        self.__observers.remove(observer)
    
    def notify(self):
        # Recorre la lista de observadores y llama al método update() de cada uno
        for observer in self.__observers:
            observer.update(self.__state)
    
    def updateState(self, state):
        # Actualiza el estado del objeto sujeto y notifica a los observadores registrados
        self.__state = state
        self.notify()


class Observer:
    def update(self, state):
        # Define la interfaz de actualización del observador
        pass


class ConcreteObserver(Observer):
    def update(self, state):
        # Implementa la actualización del observador
        print(f"Received state: {state}")


# Crea un objeto sujeto y un objeto observador
subject = Subject()
observer = ConcreteObserver()
subject.attach(observer)
subject.updateState("New state")



