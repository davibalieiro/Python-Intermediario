class Car:
    def __init__(self, name):
        self.name = name
        self._engine = None
        self._manufacturer = None

    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, value):
        self._engine = value

    @property
    def manufacturer(self):
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self, value):
        self._manufacturer = value

class Engine:
    def __init__(self, name):
        self.name = name


class Manufacturer:
    def __init__(self, name):
        self.name = name

uno = Car("Uno")
engine_uno = Engine("2.0")
fiat = Manufacturer("Fiat")
uno.manufacturer = fiat
uno.engine = engine_uno
print(f"{uno.name} - {uno.engine.name} - {uno.manufacturer.name}")

