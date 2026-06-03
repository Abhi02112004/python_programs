n=int(input("Enter the number :"))
num=1
for i in range(n):
    for j in range(i):
        print(num,end =" ")
        num=num+1
    print()