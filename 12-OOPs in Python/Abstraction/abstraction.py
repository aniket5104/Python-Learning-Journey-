from abc import ABC, abstractmethod

class UPI(ABC):
    @abstractmethod
    def security_pin(self):
        pass
    @abstractmethod
    def pay(self):
        pass

class PayTM(UPI):
    def security_pin(self):
        print("Security IMPLEMENTED!")

    def pay(self,money):
        print(money,"sent to another bank accont")

aniket=PayTM()
aniket.security_pin()
aniket.pay(2000)

