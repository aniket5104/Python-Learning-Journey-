from functools import reduce
num= [1,2,3,4,5,6]
total= reduce(lambda x,y : x+y, num)
print(total)
