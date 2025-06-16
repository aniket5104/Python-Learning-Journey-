with open("file.txt","r") as f:
    print(f.read(10))
    print(f.tell()) #tells the current cursor position
    f.seek(0) #changes the current position
    print(f.read(10))

with open("file.txt","w") as f:
    f.write("aniket")
    f.seek(0)
    f.write("e")