input_list=["hello","hello","I","AM","abhinav","abhinav"]
new_set=set(input_list)
#print(new_set)

count_list=[]
for word in new_set:
    count_list.append((word,input_list.count(word)))
print(count_list)
