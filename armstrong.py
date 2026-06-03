num=int(input("Enter a number :"))
temp=num
sum=0
no_of_digits=len(str(num))
res=int(no_of_digits)
while(temp>0):
    digit=temp%10
    sum+=digit**res
    temp = temp//10

if sum==num :
    print("Armstrong Number .")
else :
    print("Not a Armstrong Number ")