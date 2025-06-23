class Car:
    wheels=4

    def __init__(self, name):
        self.name=name
    def show_details(self):
        print("Name:",self.name)

car1=Car("Fortuner")
car1.show_details()
        