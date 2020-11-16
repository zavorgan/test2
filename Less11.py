import random

num1 = input('Введите количество значений в списке: ')
num2 = int(num1)
# print(type(num2))
list1 = [(int(random.random() * 100)) for i in range(0, num2)]
print(list1)

n = 0
while n < len(list1):
    print(list1[n])
    n +=1

myset = set(list1)
print(myset)
list2 = list(myset)
print(list2)

for k in list2:
    print(k)