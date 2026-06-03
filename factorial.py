num=int(input("Enter a number :"))
temp=num
fact=1
while temp>0:
      fact=fact*temp
      temp=temp-1
print(f"The factorial of the {num} is ",fact)