class Factory:
    def __init__(self, material, zip):
        self.material = material
        self.zip = zip
        
class RajshahiFactory(Factory):
    def __init__(self, material, zip, color):
        super().__init__(material, zip)
        self.color = color
        
class RangpurFactory(RajshahiFactory):
    def __init__(self, material, zip, color, pockets):
        super().__init__(material, zip, color)
        self.pockets = pockets
        
        
    def display(self):
        print(f"material : {self.material}")
        print(f"zip : {self.zip}")
        print(f"color : {self.color}")
        print(f"pockets : {self.pockets}")
        

obj = RangpurFactory("Cotton", "Metal", "Black", 2)

obj.display()
