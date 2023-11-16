# numbers = [1, 5, 8, 12, 36, 50, 60, 81, 88, 10]
# new_list = []

# for number in numbers:
#     if number % 4 == 0 or number % 6 == 0:
#         new_list.append(number)

# print(new_list)


import random

numbers = []

for i in range(10):
    numbers.append(random.randint(1,10000))

new_list = []

for number in numbers:
    if (number % 4 == 0) or (number % 6 == 0):
        new_list.append(number)

print(numbers)
print(new_list)

    