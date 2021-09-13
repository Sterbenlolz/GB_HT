import re

def email_parse(email_address):
    if re.compile(r'^(\w+\@)(\w+\.\w{2,3})').match(email_address):
        return {'username': re.compile(r'^(\w+)').search(email_address)[0], 'domain': re.compile(r'@\w+\.\w{2,3}').search(email_address)[0].strip('@')}
    else: return 'ValueError: wrong email: {}'.format(email_address)

print(email_parse('some_email@mail.ru'))
print(email_parse('someemail@mailru'))
print(re.compile(r'@\w+\.\w{2,3}').search('someemail@some.ru')[0])