a=2 #global variable
def dif_name():
    b=3 #local variable
    print("Inside the function",a,b)

def same_name():
    a=4 #local var
    print("Inside the  function", a) 
    #inside the function the value of a in local scope is assigned

#dif_name()
same_name()
print("Outside the function",a)