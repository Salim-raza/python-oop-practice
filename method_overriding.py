class Animal:
    def Sound(self):
        print("animal sound")


class Dog(Animal):
    def Sound(self):
        print("dog says: Ghew Ghew")
        
        
obj = Dog()
obj.Sound()