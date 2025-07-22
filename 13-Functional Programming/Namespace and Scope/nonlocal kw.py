def outer():
    x=3
    def inner():
        nonlocal x #used to modify a variable in enclosing scope
        x+=2
        print(x)
    inner()

outer()
    