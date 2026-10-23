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