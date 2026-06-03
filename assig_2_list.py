trans=[[1, 100, 'success'],
    [2, 200, 'pending'],
    [3, 150, 'success'],
    [4, 300, 'failed'],
    [5, 400, 'success'],
    [6, 250, 'pending'],
    [7, 350, 'failed'],
    [8, 450, 'success'],
    [9, 500, 'pending'],
    [10, 600, 'failed']
]

success=0
pending=0
failed=0
for x in trans:
    for items in x:
      if items=='success':
        success+=1
      elif items=='pending':
         pending+=1
      elif items=='failed':
         failed+=1
print("Output:")
print(f'Success :{success}')
print(f'pending :{pending}')
print(f'failed  :{failed}')