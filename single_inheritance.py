# class FactoryDhaka: #parent class / superclass
#     a = "I am an attribute mentioned inside Factory"
    
#     def hello(self):
#         print("I am an method mentioned inside Factory")
        
        
# class FactoryDinajpur(FactoryDhaka): #child class /subclass
#     pass


# object1 = FactoryDhaka()

# object2 = FactoryDinajpur()

# object2.hello()

# print(object2.a)


class Animal:
    
    def __init__(self, name):
        self.name = name
        
    def show(self):
        print(f"hello your name is {self.name}")
        

class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        
    def show(self):
        print(f"hello your name is {self.name} you {self.age} year old")
        
        
obj1 = Animal("lion")

obj2 = Human("salim", 20)

obj1.show()
obj2.show()