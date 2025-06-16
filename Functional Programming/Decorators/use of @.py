def my_decorator(func):
    def wrapper():
        print("****************")
        func()
        print("****************")
    return wrapper

@my_decorator
def hello():
    print("Hello World")

hello()






