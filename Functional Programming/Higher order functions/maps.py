num=[1,2,3,4,5]
sqr= lambda x: x**2 
square_lst=map(sqr,num)# i.e. apply sqr function to all elements of num.
print(list(square_lst))