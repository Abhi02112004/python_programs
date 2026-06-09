employees = [
    {"id": 101, "name": "Abhinav", "age": 21, "department": "Data", "salary": 35000},
    {"id": 102, "name": "Rahul", "age": 24, "department": "HR", "salary": 28000},
    {"id": 103, "name": "Amit", "age": 22, "department": "Data", "salary": 42000},
    {"id": 104, "name": "Neha", "age": 25, "department": "Finance", "salary": 50000},
    {"id": 105, "name": "Priya", "age": 23, "department": "Data", "salary": 38000},
    {"id": 106, "name": "Rohan", "age": 26, "department": "IT", "salary": 55000},
    {"id": 107, "name": "Karan", "age": 22, "department": "HR", "salary": 30000},
    {"id": 108, "name": "Sneha", "age": 24, "department": "Finance", "salary": 48000},
    {"id": 109, "name": "Vikas", "age": 27, "department": "IT", "salary": 60000},
    {"id": 110, "name": "Anjali", "age": 21, "department": "Data", "salary": 36000}
]
# total employees count
count=0
for x in employees:
    count+=1
#print("The total no. of employees are :",count)

# print all names
for x in employees:
    print(x["name"])

# print all salaries
for x in employees:
    print(x["salary"])

# highest_salary_of employee
max=0
for x in employees:
    if x["salary"]>max:
        max=x["salary"]
print("The highest_salary is :",max)

# lowest salary of employee
min=employees[0]["salary"]
for x in employees:
    if x["salary"]<min:
        min=x["salary"]
print("The lowest_salary is :",min)

# total salary payout
total=0
for x in employees:
    total+=x["salary"]
print("Total payout :",total)

# average salary of employees
sum=0
for x in employees:
    sum+=x["salary"]
    avg=sum/len(employees)
print("The sum of total salaries are :",sum)
print("The average of total salaries are :",avg)
        