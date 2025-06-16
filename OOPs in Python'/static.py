class ATM:
    __counter=1
    def __init__(self):
        self.__pin=""
        self.__balance= 0
        self.sno = ATM.__counter
        ATM.__counter=ATM.__counter+1

    @staticmethod
    def get_counter():  # NO self is required in static method
        return ATM.__counter
    
    @staticmethod
    def set_counter(new):
        if isinstance(new, int):
            ATM.__counter = new
        else:
            print("Not Allowed")
    
sbi= ATM()
sbi.set_counter(4)
print(sbi.get_counter())