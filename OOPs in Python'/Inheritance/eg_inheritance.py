class Samsung:
    def __init__(self):
        self.camera=48
        self.battery=5000
        self.processor="Exynos"
        self.display="AMOLED"

    def call_someone(self, x):
        print("Calling",x)

class S25(Samsung):
    def _init_(self):
        self.processor="SNAPDRAGON"
        self.display="sAMOLED"

    def bixby_routines(self,routine):
        print("Routine for",routine,"is set")

aniket_phone=S25()
'''despite .camera is not a method of s25 but it can access it through its parent 
class i.e. samsung'''
print("Phone camera megapixel is",aniket_phone.camera) 

'''display is an attribute of both s25 and samsung but while using display method 
s25 display was called. This is known as method overriding'''
print("Display of phone is",aniket_phone.display)

aniket_phone.bixby_routines("Sleep")