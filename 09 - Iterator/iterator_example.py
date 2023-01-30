class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.keys = list(self.collection.keys())
        self.index = 0

    def has_next(self):
        return self.index < len(self.keys)

    def next(self):
        if self.has_next():
            key = self.keys[self.index]
            self.index += 1
            return key, self.collection[key]
        else:
            raise StopIteration


class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, key, value):
        self.items[key] = value

    def remove_item(self, key):
        self.items.pop(key)

    def get_iterator(self):
        return Iterator(self.items)


# Crear una instancia del inventario
inventory = Inventory()

# Añadir algunos items al inventario
inventory.add_item("Espada", 100)
inventory.add_item("Arco", 50)
inventory.add_item("Flechas", 200)



# Obtener un iterador para el inventario
iterator = inventory.get_iterator()

# Imprimir cada item del inventario
while iterator.has_next():
    print(iterator.next())
