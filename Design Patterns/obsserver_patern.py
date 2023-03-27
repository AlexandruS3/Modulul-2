from time import sleep
class CentralBankPublisher:

    def __init__(self):
        # Bank role
        self.__rates = {
            "EUR_USD": None,
            "USD_EUR": None,
        }
        # OBSERVER ROLE
        self.__subscribers = []

    def subscribe (self, subscriber):
        self.__subscribers.append(subscriber)

    def unsubscribe (self, subscriber):                                        # HW2: add the unsubscribe(subscriber) method
        self.__subscribers.remove(subscriber)

    def notifySubcribers(self):
        for subscriber in self.__subscribers:
            subscriber.update()


    def setRate(self, from_currency, to_currency, rate):

        if from_currency == "EUR" and to_currency == "USD":
            self.__rates["EUR_USD"] = rate                                     # HW1: from_currency, to currency -> to set the current value
        elif from_currency == "USD" and to_currency == "EUR":               
            self.__rates["USD_EUR"] = rate
        self.__rates ["EUR_USD"] = rate # functioneaza si fara !!

        self.notifySubcribers()

    def __str__(self):
        return f'BANK RATES : \n {self.__rates}\n {self.__subscribers}'
    


class Subscriber:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"COMPANY: {self.name}"
    
    def __repr__(self):
        return self.__str__()
    
    def update(self):
        print (f'{self.name} GOT THE NOTIFICATION !')

##########################################################

cb = CentralBankPublisher()
cb.subscribe(Subscriber("Construction Materials Store"))
cb.subscribe(Subscriber("AUTO SERVICE \"Victory\""))

cb.setRate("USD", "EUR", 1.2)
sleep(2)
cb.setRate("EUR", "USD", 1.1)
#cb.unsubscribe(Subscriber("COMPANY: Construction Materials Store"))
print(cb)

