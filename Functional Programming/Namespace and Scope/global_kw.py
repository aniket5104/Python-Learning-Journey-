#Use of global keyword
a=4
print("Value of a=",a)

def change():
    global a
    a+=2
    print("Now a=",a)

change()



