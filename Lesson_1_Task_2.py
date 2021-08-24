number_list = []
number_sum = 0
for i in range(1, 1001, 2):
    number_list.append(i ** 3)
    cube = i ** 3
    digit_sum = 0
    while cube > 0:
        digit = cube % 10
        digit_sum += digit
        cube = cube // 10
    if digit_sum % 7 == 0: number_sum += i ** 3
print(number_list)
print(number_sum)
number_sum = 0
for i in range(1, 1001, 2):
    number_list.append(i ** 3 + 17)
    number_list.remove(i ** 3)
    digit_sum = 0
    cube = i ** 3 + 17
    while cube > 0:
        digit = cube % 10
        digit_sum += digit
        cube = cube // 10
    if digit_sum % 7 == 0: number_sum += i ** 3 + 17
print(number_list)
print(number_sum)
