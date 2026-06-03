list=[(100,5),(200,18),(50,12),(500,18)]
list2=[(x[0],x[1],x[0]+x[0]*x[1]/100)for x in list]
print(list2)