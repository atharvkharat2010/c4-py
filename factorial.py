def recur_factorial(n):
    if n==1:
        return n
    else:
        return n * recur_factorial(n-1)
num=int(input("enter a number "))
if num<0:
    print("negative numbers are not allowed")
elif num==0:
    print("the factorial of 0 is 1")
else:
    print("the factorial is",recur_factorial(num))