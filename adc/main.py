import modules1
import modules2

print('1. factorial')
print('2. table')

choice = input('choice a number: ')
if choice == '1':
    num = int(input('choice a number: '))
    print('factorial =', modules1.factorial(num))
elif choice == '2':
    num = int(input('enter a number: '))
    modules2.print_table(num)
else:
    print('choice is error number')

