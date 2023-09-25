
class Animal:
    """ Base class for Animals which describes behaviour interface """
    def __init__(self, name="Animal's Name", age=0):
        self.name = name
        self.age = age
        self.behaviour = "moving"
        self.voice = "Here must be the sound of animal"

    def say(self):
        """Animal can make a sound"""
        print(self.voice)

    def move(self):
        """Animal can move around"""
        print(f"I'm {self.name} and I'm {self.behaviour}")

    def eat(self):
        """Strange sounds"""
        print("Nam-Nam")

    def __str__(self):
        string_description = f"""This is an animal with name: {self.name}
         Its age: {self.age}
         it can say: {self.voice}"""
        return string_description


class Cat(Animal):
    def __init__(self, name="Cat's name", age=0):
        super().__init__(name, age)
        self.behaviour = "jamping arround"


class Dog(Animal):
  def __init__(self, name="Dog's name", age=0):
    super().__init__(name, age)
    self.behaviour = "walking"
    self.voice = "Gav-Gav"

class DogTerier(Dog):
  def __init__(self, name="Fox terier's name", age=2):
    super().__init__(name, age)
    self.behaviour = "running"
    self.voice = "Where is a foxy?"

  def eat(self):
      """Sounds which makes animal when it is eating"""
      print("I like to eat a meat and sugar")



if __name__ == "__main__":

    tom = Cat(name="Thomas", age=4)
    # tom.move()
    jack = Dog(name="Jack", age=12)
    # jack.say()
    # jack.eat()
    larry = DogTerier(name="Lariontiy III")
    # larry.say()
    # larry.eat()
    for animal in tom, jack, larry:
        animal.move()
        animal.say()
        animal.eat()
