import re

def nginx_logs_parser(file):
    RE_IP = re.compile(r'(\d{1,3}\.){3}(\d{1,3})')
    RE_MAC = re.compile(r'(.*\:){7}.*')
    RE_DATETIME = re.compile(r'\[.+ \+\d{4}\]')
    RE_REQUESTTYPE = re.compile(r'([A-Z]{3,4})')
    RE_REQUESTRESOURCE = re.compile(r'(/downloads/\w+\ )')
    RE_RESPONSECODENSIZE = re.compile(r'\ \d{1,3}\ \d+\ ')
    result = []
    errors = []
    for line in list(file):
        date = RE_DATETIME.search(line)[0][1:-1]
        type = RE_REQUESTTYPE.search(line)[0]
        resource = RE_REQUESTRESOURCE.search(line)[0][:-1]
        code = RE_RESPONSECODENSIZE.search(line)[0].strip(' ')[:RE_RESPONSECODENSIZE.search(line)[0].strip(' ').index(' ')]
        size = RE_RESPONSECODENSIZE.search(line)[0].strip(' ')[RE_RESPONSECODENSIZE.search(line)[0].strip(' ').index(' ') + 1:]
        if RE_IP.search(line):
            ip = RE_IP.match(line)[0]
            result.append((ip, date, type, resource, code, size))
        elif RE_MAC.search(line):
            mac = RE_MAC.search(line)[0]
            result.append(((mac, date, type, resource, code, size)))
        else:
            errors.append('ValueError: wrong address: {}'.format(line))
    for i in range(0, len(result)):
        print(result[i])
    for i in range(0, len(errors)):
        print(errors[i])\

nginx_logs_parser(open('nginx_logs.txt', 'r', encoding='UTF-8'))