# dynamic
from os import system
system("Cls")

class Box:

    def __init__(self,value=None): #HW1:
        self.value = value         # modify init code so it puts None when no 
                                   # argument is passed
    def isEmpty(self):
         if self.value == None :
            return True
         
    def __lt__(self,other):
        if isinstance(other, Box):              #HW2: methods of comparation
            return self.value < other.value          # __lt__
        else:
            return NotImplemented
    def __gt__(self, other):                         # __gt__
        if isinstance(other, Box):
            return self.value > other.value
        else:
            return NotImplemented
    def __eq__(self, other):                         # __eq__
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
