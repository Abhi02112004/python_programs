orders_amount=[100,200,50,500,400,900,1200,70]
orders_exclusive_amount=[]
for x in orders_amount:
  orders_exclusive_amount.append(x+x*.18)
print(orders_exclusive_amount)