class Bank:
    def __init__(self,balance=0):
        self.__checkBalance(balance)
        self.__balance = balance

    def getBalance(self):
        return self.__balance
    
    def setBalance(self,balance):           # HW1:                     
        self.__checkBalance(balance)        #   use the same protection mechanism as in __init__()
        self.__balance = balance            #   but trying not to duplication the code
    
    def __checkBalance(self,balance):
        if type(balance) != int:
            raise TypeError("Only integer accepted as balance")



    def __str__(self):
        return f"BANK: {self.__balance}"
        
class LocalBank(Bank):
    def __init__(self, locality, balance=0):
        super().__init__(balance) # delegation
        self.locality = locality

    def __str__(self):
        return f"LOCAL BANK({self.locality}): {self.getBalance()}"

class CreditBank(Bank):
    def __init__(self, balance=0):                                                          
        super().__init__(balance)
                                                                    # HW2:
    def max_credit_amount(self):                                    #   CreditBank < Bank
        if self.getBalance() > 1_000:                               #   + max_credit_amount                           
            raise TypeError ("the credit line is exceeded")         #   + credit_percentage 5%
        
    def credit_percentage(self,rate=5):
        balance = self.getBalance()
        if rate <= 10:
            interest = balance * rate / 100
            print(interest + balance)
        else: 
            print("the percentage cannot be greater than 10")


world_bank = Bank(1_000_000_000_000)
agro       = LocalBank("Chisianau",1_000_000)
credit     = CreditBank(500)
credit.max_credit_amount()
agro.setBalance(100)
 
print(world_bank)
print(agro)
print(credit)
credit.credit_percentage(11)
