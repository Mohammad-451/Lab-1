hours_worked = int(input('Enter hours worked: '))
pay_rate = float(input('Enter pay rate: '))
if hours_worked <= 40:
    salary = hours_worked * pay_rate
    print('Your Salary is:', salary)
else:
    salary = pay_rate * 40 + (pay_rate * 1.5 * (hours_worked - 40))
    print('Your Salary is:', salary)