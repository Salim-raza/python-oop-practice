class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        print("constructor called")
        print(f"hello my name is {name} i am {age} year old")
        
        
    def show(self): #instant method
        print("instant method called")
        
    @classmethod
    def greet(self): #class method
        print("class method called")
        
    @staticmethod
    def static():
        print("static method called")
        

obj1 = Person("salim", 20)
obj1.show()
obj1.greet()
obj1.static()