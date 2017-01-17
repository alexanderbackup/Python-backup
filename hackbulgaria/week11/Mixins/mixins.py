from utils.serializers import *


class Panda(JsonableMixin, Xmlable):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

class Person(JsonableMixin, Xmlable):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

        
p = Panda(name='Ivo', age=50)
p1 = p.to_json()
print(dir(p.from_json(p1)))
