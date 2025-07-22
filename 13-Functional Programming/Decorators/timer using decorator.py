import time

def timer(func):
    def wrapper(*args):
        start= time.time()
        func(*args)
        print("Time Taken by",func.__name__,"to execute is",time.time() - start)
    return wrapper

@timer
def square(n):
    print(n**2)
    time.sleep(2)

@timer
def sum(a,b):
    print(a+b)
    time.sleep(3)

square(2)
sum(2,3)