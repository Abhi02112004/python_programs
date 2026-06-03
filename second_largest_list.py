list=[5,1,7,8,9,6,2,3,8]
largest=0
second_largest=0
for x in list:
    if x >largest:
        largest=x
    if second_largest<x & x!=largest:
        second_largest=x
print(largest)
print(second_largest)
