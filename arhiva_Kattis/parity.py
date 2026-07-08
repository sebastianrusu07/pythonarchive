number = input()

while number != '#':
    ones = number.count('1')
    parity = number[-1]

    if parity == 'e':
        if ones % 2 == 0:
            print(number[:-1], '0', sep='')
        else:
            print(number[:-1], '1', sep='')
    else:
        if ones % 2 != 0:
            print(number[:-1], '0', sep='')
        else:
            print(number[:-1], '1', sep='')


    number = input()

