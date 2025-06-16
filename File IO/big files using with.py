# L=["Hello World." for x in range(1000)]
# f=open("Big_File.txt","w")
# f.writelines(L)
chunk=100
with open("Big_File.txt","r") as f:
    while len(f.read(chunk))>0:
        print(f.read(chunk),end='')
        f.read(chunk)

