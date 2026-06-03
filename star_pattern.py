num=int(input("Enter the number of rows"))
for i in range(1,num+1):
   print(" "*(num-i) + "* "*i)
for i in range(num,0,-1):
   print(" "*(num-i) + "* "*i)