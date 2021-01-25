import re
import json
from datetime import datetime
dic = {}
with open("datafile.py", "r") as data:
    for line in data.readlines():
        line = re.split(' = |,', line)
        dic [line[0]] = line[1].replace('"', '').replace('\n', '')
ordered_data = sorted(dic.items(), key = lambda x:datetime.strptime(x[1], '%Y-%m-%d'), reverse=True)
print('Список сотрудников отсортированный по уменьшению возраста:')
dic1 = {}
for i in ordered_data:
    print(i[1], '-', i[0])
    dic1 [i[0]] = i[1]

DOB_of_the_youngest = datetime.strptime(list(dic1.values())[0], '%Y-%m-%d')


for i in ordered_data:
    DOB = datetime.strptime(i[1], '%Y-%m-%d')
    now = datetime.now()
    days_to_current_date = now - DOB
    age_in_1998 = (DOB_of_the_youngest - DOB).days // 365
    list_json = {
    "Name": i[0],
    "tags": [
        {"Days to current date": days_to_current_date.days},
        {"Age in 1998": age_in_1998}  
        ]
    }
    with open('result.json', 'a') as write_file:
        json.dump(list_json, write_file, ensure_ascii=False)
        write_file.write('\n')
