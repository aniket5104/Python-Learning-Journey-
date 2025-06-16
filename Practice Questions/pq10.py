def fact(n):
    facto=1
    for i in range(1,n+1):
        facto*=i
    print(facto)
n=int(input("Enter a no.: "))
fact(n)