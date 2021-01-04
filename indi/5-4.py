# n = int(input())
# a = []
# # l = len(result)
# while n > 0:
#     a.append(n % 10)
#     n //= 10
# a.reverse()
# # print(a)
# # print(len(result))
# count = [0] * 10
# for i in a:
#     count[i] +=1
# # print(count)
# for i in range(10):
#     if count[i] > 0:
#         print(i, count[i])

n = int(input())
a = list(map(int, input().strip().split()))[:n] #Ввод списка n-чисел в одну строку
# print(a)
count = [0]*201
for i in a:
    count[i+100] += 1
# print(count)
for i in range(201):
     if count[i] > 0:
         x = str(i-100)+' '
         print(x * count[i], end='')