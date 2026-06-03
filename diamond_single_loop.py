<<<<<<< HEAD
num=int(input("Enter a number :"))
for i in range (1,2*num):
    if i<=num:
        spaces=num-i
        stars=2*i-1
    else:
        spaces=i-num
        stars=2*(2*num-i)-1
=======
num=int(input("Enter a number :"))
for i in range (1,2*num):
    if i<=num:
        spaces=num-i
        stars=2*i-1
    else:
        spaces=i-num
        stars=2*(2*num-i)-1
>>>>>>> d263f15ff0233c9aac765a72ba3a28d76fcf4771
    print(" "* spaces + "*" * stars)