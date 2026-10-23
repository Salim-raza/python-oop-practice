class Dog:
    def sound(self):
        print("Ghew Ghew")

class Cat:
    def sound(self):
        print("Meow Meow")

def make_sound(animal):
    animal.sound()

dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)
