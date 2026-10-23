# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
        
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
    
#     def get_balance(self):
#         return self.__balance
    
# account = BankAccount(1000)

# account.deposit(500)
# print(account.get_balance())



class Demo:
    def __init__(self, name, age, salary):
        self.name = name            #Public
        self._age = age             #Protected
        self.__salary = salary      #privet
        
    def show(self):
        print(f"name: {self.name}")
        print(f"age: {self._age}")
        print(f"salary: {self.__salary}")
        
        
obj = Demo("Rohan", 21, 15000)

obj.show()


class Student:
    def __init__(self, marks):
        self.__marks = marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks

    def get_marks(self):
        return self.__marks


student = Student(80)
student.set_marks(90)

print(student.get_marks())