list=[14,74,65,54,74,"abhi",74688,"hffdfv",74.11]
sum=0
for x in list:
    if type(x)==int or type(x)==float:
        sum+=x
print(sum)