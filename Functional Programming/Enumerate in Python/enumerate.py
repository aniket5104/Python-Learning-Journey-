fruits= ["Apple", "Orange", "Banana"]
for index, fruit in enumerate(fruits,start = 1):
    print(fruit,index)

print(list(enumerate(fruits,start=0))) #converting to list