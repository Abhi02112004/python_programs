num=int(input("Enter a number :"))
fact=1
temp=num
while temp>0:
    fact=fact*temp
    temp-=1

print(f"The factorial of {num} is ",fact)