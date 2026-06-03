# [[1,1,1],[2,4,8],[3,9,27]]
list=[(x,x**2,x**3) for x in range (1,4)]
#print(list)

format_list=[]
for subitems in list:
    for items in subitems:
        format_list.append(items)
print(format_list)
