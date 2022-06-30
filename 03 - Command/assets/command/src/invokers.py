"""
La clase Emisora (o invocadora) es responsable de inicializar las solicitudes.

Esta clase debe tener un campo para almacenar una referencia a un objeto de comando.

El emisor activa este comando en lugar de enviar la solicitud directamente al receptor.

Ten en cuenta que el emisor no es responsable de crear el objeto de comando.
Normalmente, obtiene un comando precreado de parte del cliente a través del constructor.

"""


class Button:
    def __init__(self):
        self.__callback = None

    def render():
        # do stuff
        pass

    def handle_event():
        # do stuff
        pass

    def on_click(self, callback):
        """ Define el evento on_click

        :param callback: Función a ejecutar cuando se detecte un click en el btn

        """
        self.__callback = callback

    def click(self, *args, **kwargs):
        """ Método lanzado por presionar el botón

        """
        return self.__callback(*args, **kwargs)


class Shortcut:
    def __init__(self):
        self.__callback = None
        self.__keys = None

    def handle_event():
        # do stuff
        pass

    def on_key_press(self, keys, callback):
        """ Define el evento on_key_press

        :param keys: Tecla o combinación de teclas para aplicar la acción.

        :param callback: Función a ejecutar cuando se detecte la convinación de teclas
        """
        self.__callback = callback
        self.__keys = keys

    def key_press(self, *args, **kwargs):
        """ Método lanzado por realizar la combinación de teclas correctas
        """
        return self.__callback(*args, **kwargs)
