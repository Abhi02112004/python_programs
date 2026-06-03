list=[1,"Abhinav",14.95,12500,"BCA","icfai university",14900]
sum=0
for x in list :
    if type(x)==str:
        continue
    else:
        sum+=x
print(f"The sum of list is {sum}")