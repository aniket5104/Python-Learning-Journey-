import sys

lst = [x for x in range(1,10000)]
# for x in lst:
#     print(x)
print(sys.getsizeof(lst)) #85176 bytes

lst1= range(1,100000000000000000000000000)
print(sys.getsizeof(lst1)) #only 48 bytes!
