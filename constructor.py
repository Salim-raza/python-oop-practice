class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        print("constructor called")
        print(f"hello my name is {name} i am {age} year old")
        

obj1 = Person("salim", 20)