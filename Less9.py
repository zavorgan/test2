list = ['a', 'b', 'c', 'd', 'e']
# print(list)
# print(len(list))

i = 0
while i < len(list):
    print(i, '-', list[i])
    i+=1

idnex_list = input('Введите индкс списка:')
index = int(idnex_list)

if index <= len(list):
    print('Значение индекса: ', index, ' = ', list[index])
else:
    print('Элемент не существует')