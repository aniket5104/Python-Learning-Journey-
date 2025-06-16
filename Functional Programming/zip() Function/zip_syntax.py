names=["Aniket","Ravi","Pooja"]
marks=[90,85,78]
zipped= zip(names,marks)
#print(list(zipped))

#Unzipping a zip
names,marks=zip(*zipped) #names and marks are assgined the unzipped values
# *<zip_name> is used to unzip a zip
print(names)
print(marks)