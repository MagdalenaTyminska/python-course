first_name = input('Jak masz na imię? ')
age = int(input('Ile masz lat? '))

print('Hello ' + first_name + '!')
print('Mam ' + str(age) + ' lat')

print(f'Mam {age} lat')

if first_name == 'Magda':
    print('Cześć Magda')
else:
    print('Miło Cię poznać')

if age >= 18:
    print('Jesteś pełnoletni/a')
else:
    print('Jeszcze musisz poczekać')
    print(f'{18 - age} lat')

def print_hi(name):
    print(f'Hello, {name}')

if __name__ == '__main__':
    print_hi('world!')