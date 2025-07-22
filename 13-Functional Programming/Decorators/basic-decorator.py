def my_decorator(func): #this is a user defigned decorator
    def wrapper():
        print("****************")
        func()
        print("****************")
    return wrapper

def hello():
    print("Hello World")

a=my_decorator(hello)
a()

