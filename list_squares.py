for i in range(1,4):
        list2=[[i,i**2,i**3] for i in range(1,4)]

flattened_list=[]
for sublist in list2:
        for item in sublist:
                flattened_list.append(item)
print(flattened_list)