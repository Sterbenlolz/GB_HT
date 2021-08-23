price_list = [58, 49.53, 37.06, 157.80, 75.99, 38.60, 47, 322, 13.37, 42, 6.90, 73]


def price_stringing(prices):
    fullprice_list = []
    for price in prices:
        if type(price) == int:
            r = str(price)
            kk = '00'
            price_str = r + ' руб ' + kk + ' коп'
            fullprice_list.append(price_str)
        elif type(price) == float:
            r = str(price // 1).replace('.0', '')
            kk = str(price - price // 1).replace('0.', '')[0:2]
            price_str = r + ' руб ' + kk + ' коп'
            fullprice_list.append(price_str)
    print(', '.join(fullprice_list))


price_stringing(price_list)
print(id(price_list))
price_list.sort()
price_stringing(price_list)
print(id(price_list))
price_stringing(price_list[-6:-1])
