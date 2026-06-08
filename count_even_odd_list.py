list=[124,254,671,745,965,324,415,654,854,652]
even_count=0
odd_count=0
for x in list:
    if x%2==0:
        even_count+=1
    else:
        odd_count+=1
print("Even counts are :",even_count)
print("Odd Counts are :",odd_count)