# -*- coding: utf-8 -*-

import time
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        """ 
            Instancias que se comportan como funciones y se pueden llamar como una función. Ejemplo: 
            class Product:
                def __init__(self): 
                    print("Instance Created") 
                
                def __call__(self, a, b): 
                    print(a * b) 
    
            operation_product = Product() 
            operation_product(10, 20) 
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]

    
class Singleton(metaclass=SingletonMeta):
    def __init__(self, server_ftp_name):
        """Inicializamos los atributos del objeto que creamos"""
        self.server_ftp_name = 'Bootcamp'
        self.port = '21'
        self.ip = '0.0.0.0'
        
    def open_connection_ftp(self):
        for state in ['LOADING...', 'SYNC...', 'SUCCESS!!!']:
            time.sleep(2)
            print(state)
        return F'Connection OPEN at {self.server_ftp_name}'
            


if __name__ == "__main__":
    s1 = Singleton("Test")

    print(s1.open_connection_ftp())
