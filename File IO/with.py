# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

# an equivalent of this using with statement
with open("file.txt") as f:
    print(f.read())
#you dont have to eplicitly cliose the fie
