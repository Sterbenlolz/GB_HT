import requests
from decimal import Decimal

def currency_rates(currency_code):
    currency_list = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text.split('<CharCode>')[1:]
    currency_rate = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text.split('<Value>')[1:]
    for currency in currency_list[:]:
        currency_list.append(currency[0:3])
        currency_list.remove(currency)
    for currency in currency_rate[:]:
        currency_rate.append(Decimal(currency[0:currency.index(',') + 5].replace(',', '.')))
        currency_rate.remove(currency)
    if currency_code in currency_list:
        return currency_rate[currency_list.index(currency_code)]
    else:
        return None

print(currency_rates('EUR'))
print(currency_rates('USD'))
