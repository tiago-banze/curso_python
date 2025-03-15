# python calculator

operator = input('Enter an operator (+ - */): ')
num1 =float(input('enter the 1st number: '))
num2 =float(input('enter the 2nd number: '))
result = 0

if operator == '+':
    result = num1 + num2
    print (f'{num1} + {num2} = {round(result,2)}')
elif operator == '-':
    result = num1 - num2
    print (f'{num1} - {num2} = {round(result,2)}')
elif operator == '*':
    result = num1 * num2
    print (f'{num1} * {num2} = {round(result,2)}')
elif operator == '/':
    if num2 ==0:
        result = 0
        print (f'Cannot divide {num1} by {num2}:')
    else:
        print (f'{num1} / {num2} = {round(result,2)}')
else: 
    print(f'{operator} is not valid oparator!')

# print(num1 + num2)