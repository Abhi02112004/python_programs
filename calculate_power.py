arr=list(map(int,input("Enter elements : ").split()))

smallest=arr[0]
largest =arr[0]

for i in arr:
    if i>largest :
        largest=i
    if i<smallest:
        smallest =i

print("largest element is ",largest)
print("smallest element is ",smallest)

