while True:
    pesel = input('Enter your PESEL number: ')

    if pesel is not None and len(pesel) == 11:
        day = int(pesel[4:6])
        month = int(pesel[2:4])
        year = int(pesel[0:2])

        if month > 20 and month <= 32:
            year += 2000
            month -= 20

        elif month > 80 and month <= 92:
            year += 1800
            month -= 80

        else:
            year += 1900
        date_of_birth = f'{day}.{month}.{year}'
        print(f'Date of birth: {date_of_birth}')
        break

    else:
        print('Incorrect PESEL number. PESEL should have 11 characters. Try again.')
