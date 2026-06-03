num=int(input("Enter a number :"))
for i in range (num):
    for j in range (i+1):
        if i==num-1 or j==0 or j==i: 
         print("*",end=" ")
        else:
           print(" ",end=" ")
    print()