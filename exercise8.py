class Animall:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name


class Cat(Animall):

    def speak(self):
        return self.name + ' meows.'


dog = Animall("Fibi")
print(dog.speak())

mial = Cat("Puma")
print(mial.speak())




