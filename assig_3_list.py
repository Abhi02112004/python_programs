employee=[
    [101, 'John', 'IT', 60000],
    [102, 'Alice', 'HR', 50000],
    [103, 'Bob', 'Finance', 70000],
    [104, 'Emma', 'IT', 55000],
    [105, 'David', 'Finance', 75000],
    [106, 'Sophia', 'HR', 48000]
]

it=0
it_count=0
hr=0
hr_count=0
finance=0
finance_count=0
for x in employee:
    if x[2]=='IT':
        it+=x[3]
        it_count+=1
        avg_it_sal=it/it_count
    elif x[2]=='HR':
        hr+=x[3]
        hr_count+=1
        avg_hr_sal=hr/hr_count
    elif x[2]=='Finance':
        finance+=x[3]
        finance_count+=1
        avg_finance_sal=finance/finance_count
print(f'The Salary of IT Department is {avg_it_sal}')
print(f'The Salary of HR Department is {avg_hr_sal}')
print(f'The Salary of Finance Department is {avg_finance_sal}')
