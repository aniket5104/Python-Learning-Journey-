def sanity_check(data_type):
    def outer(func):
        def inner(*args):
            if type(args[0]) == data_type:
                func(*args)
            else:
                raise TypeError("Not a valid Data Type")
        return inner
    return outer

@sanity_check(int)
def square(n):
    print(n**2)

@sanity_check(str)
def say_hello(name):
    print("hello",name)

square(5)
say_hello("Aniket")


    