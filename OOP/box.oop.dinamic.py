# dynamic
from os import system
system("Cls")

class Box:

    def __init__(self,value=None):
        self.value = value
              
    def isEmpty(self):
         if self.value == None :
            return True
         
    def __lt__(self,other):
        if isinstance(other, Box):
            return self.value < other.value
        else:
            return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Box):
            return self.value > other.value
        else:
            return NotImplemented
    def __eq__(self, other):
         if isinstance(other, Box):
            return self.value == other.value
         else:
            return NotImplemented
        

    
        
         
    

b1 = Box(1150)
b2 = Box(25055)



if b1 < b2:
    print(f"{b2.value} este mai mare deccit {b1.value}")


elif b1 > b2:
    print(f"{b1.value} este mai MARE decit {b2.value}")


elif b1 == b2:
    print("boxele sunt egale")
