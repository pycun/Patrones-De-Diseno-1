"""
El Cliente crea y configura los objetos de comando concretos.

El cliente debe pasar todos los parámetros de la solicitud, incluyendo una instancia del receptor, dentro del
constructor del comando. Después de eso, el comando resultante puede asociarse con uno o varios emisores.

"""
from src.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from src.invokers import Button, Shortcut
from src.utils import CommandHistory


class Calculator:
    def __init__(self, verbose=False):
        self.__verbose = verbose
        self.total = 0.0
        self.__history = CommandHistory()

        # NOTE: Aqui se podria ser el receptor donde los comandos delegan
        #  las acciones a los metodos del receptor
        self.__receiver = None

        # region Elementos UI
        self.add_btn = None
        self.add_shortcut = None
        self.subtract_btn = None
        self.subtract_shortcut = None
        self.multiply_btn = None
        self.multiply_shortcut = None
        self.divide_btn = None
        self.divide_shortcut = None
        self.undo_btn = None
        self.undo_shortcut = None
        # endregion

    def __execute_command(self, command):
        command.execute()
        # Si el comando fue ejecutado se guarda en el historial
        if command.is_executed:
            self.__history.push(command)

            # Se imprime la operación en pantalla
            if self.__verbose:
                print(command)

    def __add_callback(self, num):
        command = AddCommand(self.__receiver, self, num)
        self.__execute_command(command)

    def __subtract_callback(self, num):
        command = SubtractCommand(self.__receiver, self, num)
        self.__execute_command(command)

    def __multiply_callback(self, num):
        command = MultiplyCommand(self.__receiver, self, num)
        self.__execute_command(command)

    def __divide_callback(self, num):
        command = DivideCommand(self.__receiver, self, num)
        self.__execute_command(command)

    def __undo_callback(self):
        command = self.__history.pop()
        if command:
            command.undo()

        # Se imprime la operación en pantalla
        if self.__verbose:
            print(F'[UNDO] = {self.total}')

    def create_user_interface(self):
        """
        Código para asignar comandos a objetos UI
        """
        # region inicialización de elementos de la interfaz de usuario
        self.add_btn = Button()
        self.add_shortcut = Shortcut()

        self.subtract_btn = Button()
        self.subtract_shortcut = Shortcut()

        self.multiply_btn = Button()
        self.multiply_shortcut = Shortcut()

        self.divide_btn = Button()
        self.divide_shortcut = Shortcut()

        self.undo_btn = Button()
        self.undo_shortcut = Shortcut()
        # endregion

        # ...

        # region Eventos
        # Eventos de botones
        self.add_btn.on_click(self.__add_callback)
        self.subtract_btn.on_click(self.__subtract_callback)
        self.multiply_btn.on_click(self.__multiply_callback)
        self.divide_btn.on_click(self.__divide_callback)
        self.undo_btn.on_click(self.__undo_callback)
        # Eventos de los atajos
        self.add_shortcut.on_key_press('+', self.__add_callback)
        self.subtract_shortcut.on_key_press('-', self.__subtract_callback)
        self.multiply_shortcut.on_key_press('*', self.__multiply_callback)
        self.divide_shortcut.on_key_press('/', self.__divide_callback)
        self.undo_shortcut.on_key_press('ctrl + z', self.__undo_callback)
        # endregion

