while True:
    conversion_choice = input('Enter 1 to convert from Celsius to Fahrenheit, 2 to convert from Fahrenheit to Celsius: ')
    

    if conversion_choice == '1':
        degrees = float(input('Provide temperature to convert: '))
        print((degrees * 9/5) + 32)
        break
    elif conversion_choice == '2':
        degrees = float(input('Provide temperature to convert: '))
        print((degrees - 32) * 5/9)
        break
    else:
        print('Incorrect choice. Enter 1 or 2.')

