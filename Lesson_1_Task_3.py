for n in range(1, 150):
    if n % 10 == 1 and n % 100 != 11:
        print('{} процент'.format(n))
    elif n % 10 == 2 and n % 100 != 12:
        print('{} процента'.format(n))
    elif n % 10 == 3 and n % 100 != 13:
        print('{} процента'.format(n))
    elif n % 10 == 4 and n % 100 != 14:
        print('{} процента'.format(n))
    else:
        print('{} процентов'.format(n))
