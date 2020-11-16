list = []
print(list)

list = ['h', 'e', 'l', 'l', 'o']
print(list)

print(list[0])
print('Длинна массива: ', len(list))
print('Последний элемент: ', list[len(list) - 1])

print('=============================')


i = 0
while i < len(list):
    print(list[i])
    i += 1

print('=============================')
list = [[2, 3],  [4, 5, 6]]
i = 0
while i < len(list):
    j = 0
    while j < len(list[i]):
        print(list[i][j])
        j += 1
    i += 1

print('=============================')
prices = [20, 30, 40, 50, 15, 22]
min = prices[0]
max = prices[0]
i = 1
while i < len(prices):
    if prices[i] < min:
        min = prices[i]
    if prices[i] > max:
        max = prices[i]
    i += 1
print(prices)
print('Минимальное значение: ', min)
print('максимальное значение: ', max)

