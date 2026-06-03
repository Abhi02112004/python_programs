num=int(input("Enter a number :"))
for i in range (num):
    print(" "*(num-i),end=" ")
    print("*"*(2*i-1))
for i in range (num,0,-1):
    print(" "*(num-i),end=" ")
    print("*"*(2*i-1))