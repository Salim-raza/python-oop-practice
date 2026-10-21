class Student:
    Institute_name = "TPI" #class attribute 
    
    def __init__(self, name, id): #method
        department = "CST" #local variable
        self.name = name #instant variable/instant attribute 
        self.roll = id
        
        print(f"your name {name} and your id {id} also you department {department} and your college {self.Institute_name}")
        
Student("salim", 50)

#creating a object 
obj = Student("rakib", 40) #object
        