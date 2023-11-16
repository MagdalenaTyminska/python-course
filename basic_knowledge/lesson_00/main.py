first_name = input('What\'s your name? ')
age = int(input('How old are you? '))

print('Hello ' + first_name + '!')
print('I\'m' + str(age))

print(f'I am {age}')

if first_name == 'Magda':
    print('Hello Magda')
else:
    print('Nice to meet you')

if age >= 18:
    print('You are adult')
else:
    print('You still have to wait')
    print(f'{18 - age} years')

# def print_hi(name):
#     print(f'Hello, {name}')

# if __name__ == '__main__':
#     print_hi('world!')