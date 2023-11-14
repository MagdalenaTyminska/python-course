# lists
fruits = ['peach', 'banana', 'mango', 'lemon', 'apple', 'kiwi']
fruits.sort()

for fruit in fruits:
    print(fruit)


fruits2 = []

for i in range(5):
    # fruits2.append(input('Enter a fruit: '))
    # lub
    fruits2.append(input(f'Enter your {i+1} favourite fruit: '))
    fruits2.sort()

for fruit in fruits2:
    print(fruit)



