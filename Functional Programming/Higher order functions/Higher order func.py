#higher order fuction are thee one which: 
#1.---> takes another functon as agrs.
#2.---> returns another function as a result, or both.
def apply_and_return(func, value): #function as input
    def inner():
        return func(value) 
    return inner #returning a function

def square(x):
    return x * x

f = apply_and_return(square, 5)
print(f())  # Output: 25

#Built-in Higher Order Functions in Python:
#1. map(func, iterable)
#2. filter(func, iterable)
#3. reduce(func, iterable) # import from functools