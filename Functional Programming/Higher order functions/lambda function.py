#general examples:---
sqr= lambda x : x**2 # lambda arg : expression
print(sqr(4)) #always written in one line
even_odd= lambda x: "Even" if x%2==0 else "Odd"
print(even_odd(45))

# return type of lambda:---
print(type(sqr),type(even_odd)) # returns a function type

