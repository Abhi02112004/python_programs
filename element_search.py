list=[14,1,21,23,14,46,74,82,2,4]
min=list[0]
max=0
for x in list:
    if x>max:
        max=x
    if x<min:
        min=x

print(max)
print(min)