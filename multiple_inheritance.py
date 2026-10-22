class Father:
    def skill(self):
        print("coding")
        
class Mother:
    def skill(self):
        print("coking")
        
class Son(Father, Mother):
    def show(self):
        print("I Have Multiple Skill")
        
        
obj1 = Son()
obj1.show()
obj1.skill()
