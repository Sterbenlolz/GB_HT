def odd_to_n(n):
    for i in range(1, n + 1, 2):
            yield i


odd_to_15 = odd_to_n(15)
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))
print(next(odd_to_15))


