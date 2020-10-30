def analysis(my_list, my_dict):
    for i in my_list:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

lst = "hallo, klempner, das, ist, fantastisch, fluggegecheimen"
lst = [i for i in lst if i.isalpha()]

dct = {}

analysis(lst, dct)

#for item in sorted(dct):
    #print("'%s':%s" % (item, dct[item]))

for i in dct:
    dct[i] /= len(lst)

#for item in sorted(dct):
    #print("'%s':%s" % (item, dct[item]))

p = 1

print('Введите Стоп - слово.')
slovo = input()
slovo = [i for i in slovo]
#print(slovo)
for i in dct:
    for k in range(len(slovo)):
        if i == slovo[k]:
            p *= dct[i]
print(p)
            




