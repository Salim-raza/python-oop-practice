class Salim:
    def salim_self(self):
        print("I'm salim raza")
        
    def power(self):
        print("I've a lot of power.")
        
        
class Rakib(Salim):
    def rakib_self(self):
        print("I'm rakib hasan")
        

class Rohan(Salim):
    def rohan_self(self):
        print("I'm rohan")
        

obj1 = Salim()
obj1.salim_self()
obj1.power()


obj2 = Rakib()
obj2.rakib_self()
obj2.power()


obj3 = Rohan()
obj3.rohan_self()
obj3.power()