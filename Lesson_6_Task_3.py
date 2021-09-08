import sys
import json

result_dict = dict()
with open('names.csv', 'r', encoding = 'utf-8') as names, \
    open('hobbies.csv', 'r', encoding = 'utf-8') as hobbies:
    for name_line in names:
        hobby_line = hobbies.readline().strip()
        if not hobby_line:
            hobby_line = None
        if name_line not in result_dict:
            result_dict[name_line.strip()] = hobby_line
    hobby = hobbies.read()
    if hobby:
        sys.exit(1)

with open('result.json', 'w', encoding = 'utf-8') as result_file:
    dict_as_str = json.dumps(result_dict, ensure_ascii=False)
    result_file.write(dict_as_str)
with open('result.json', 'r', encoding = 'utf-8') as file:
    content = file.read()
    result = json.loads(content)
print(result)
