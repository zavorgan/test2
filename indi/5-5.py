# n = int(input())
# for i in range(n+1):
#     for j in range(i):
#         print(j+1, end=' ')
#     print()

# def is_plain_number(p):
#     if p % 2 == 0 and p != 2 or p == 1:
#         return False
#     d = 3
#     while d*d <= p:
#         if p % d == 0:
#             return False
#         d +=2
#     return True
#
# n = int(input())
# count=0
#
# for p in range(n+1, n*2):
#     if is_plain_number(p):
#         count += 1
# print(count)

n = int(input())
mas = list(map(int, input().split()))
count=0
for run in range(n-1):
    for i in range(n-1-run):
        if mas[i] > mas[i+1]:
            count +=1
            mas[i], mas[i+1] = mas[i+1], mas[i]
print(*mas)
print(count)