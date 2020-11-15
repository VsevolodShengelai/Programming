import json

# открытие файла на чтение
with open('in.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

outData = []

for block in data:
    flag = False
    for i in range(len(outData)):
        if outData[i]['userId'] == (block['userId']):
            flag = True
            # print('Yes')
            if block['completed'] == True:
                outData[i]['task_completed'] = outData[i]['task_completed'] + 1
    if flag == False:
        dict_ = {'userId': block['userId'], 'task_completed': 0}
        if block['completed'] == True:
            dict_['task_completed'] = dict_['task_completed']+1

        outData.append(dict_)

# открытие файла на запись
with open('out.json', 'w') as f:
    json.dump(outData, f, indent= 4) # отступ в 4 пробела

print(outData) #для отладки

