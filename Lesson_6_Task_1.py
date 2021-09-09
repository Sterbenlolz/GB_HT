def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
result = []
spammer = dict()
with open('nginx_logs.txt', 'r', encoding='UTF-8') as first_list:
    for line in first_list:
        ln = line.split()
        ip = ln[0]
        result.append((ip, ln[5].strip('"'), ln[6]))
        if ip not in spammer:
            spammer[ip] = 1
        else: spammer[ip] += 1
for i in range(0, len(result)):
    print(result[i])
print('Больше всего запросов от: {}'.format(get_key(spammer, max(spammer.values()))))
print('Всего запросов: {}'.format(max(spammer.values())))