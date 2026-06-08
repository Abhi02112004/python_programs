list=[124,254,415,745,965,324,415,652,854,652]
unique_list=[]
for x in list:
    if x not in unique_list:
        unique_list.append(x)
print(unique_list)