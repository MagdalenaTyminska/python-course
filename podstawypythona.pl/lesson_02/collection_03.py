#set - nie sortują się i nie przyjmują duplikatów
first_names = set()

first_names.add('Michał')
first_names.add('Ania')


team_a = {'Wojtek', 'Ania', 'Rafał'}
team_b = {'Paweł', 'Ola', 'Tosia'}

print('Sum', team_a | team_b),
print('Intersection', team_a & team_b)
print('Symmetric difference', team_a ^ team_b)
print('A - B', team_a - team_b)
print('B - A', team_b - team_a)