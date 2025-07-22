class ATM:
    def __init__(self):
        self.__pin="0000"
    
    @property #decorator for getter 
    def pin(self): #only self passes in decorator 
        return self.__pin
    
    @pin.setter
    def pin(self, new_pin):
        if len(new_pin)==4 and new_pin.isdigit():
            self.__pin = new_pin
        else:
            print("Invalid PIN Formaat")

atm=ATM()
atm.pin="1234"
print(atm.pin)
       