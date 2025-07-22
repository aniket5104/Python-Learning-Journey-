def facto(n):
    if n==1 or n==0:
        return 1
    else:
        return n*facto(n-1)
    
n=int(input("Enter a no.: "))
fact=facto(n)
print("The factorial of",n,"is",fact)