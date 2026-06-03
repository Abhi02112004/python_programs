list=[[1,1,1],[2,4,8],[3,9,27]]
list2=[[x[0],x[0]**2,x[0]**3] for x in list]
#print(list2)
list3=[items for sublist in list for items in sublist]
print(list3)