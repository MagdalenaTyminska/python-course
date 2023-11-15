import random

words = {
    'pies': 'dog',
    'kot': 'cat',
    'krowa': 'cow',
    'kura': 'hen',
    'kaczka': 'duck',
    'świnia': 'pig',
    'koń': 'horse',
    'owca': 'sheep',
    'mysz': 'mouse',
    'ryba': 'fish'
}

random_words = random.sample(list(words.items()), 5)

for i in range(5):
    key_or_value = random.choice(['key', 'value'])

    if key_or_value == 'key':
        question = f'Enter the Polish word for: '{random_words[i][1]}' '
        user_input = input(question)
        if user_input.lower() == random_words[i][0]:
            print('Correct answer!')
        else:
            print(f'Incorrect. Correct answer is: '{random_words[i][0]}'')
    else:
        question = f'Enter the English word for: '{random_words[i][0]}' '
        user_input = input(question)
        if user_input.lower() == random_words[i][1]:
            print('Correct answer!')
        else:
            print(f'Incorrect. Correct answer is: '{random_words[i][1]}'')