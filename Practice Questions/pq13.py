def cal_sum(n):
    if n==1:
        return 1
    else:
        return cal_sum(n-1)+n
n=int(input("Enter n: "))
print("The sum of first",n,"natural no.s is",cal_sum(n))