# N = int(input())
# num = input().split()
# print(num)
# for i in range (N):
#     num[i] = int(num[i])
# print(min(num), max(num))

N = int(input())
num = list(map(int, input().split()))
max_num = num[0]
min_num = num[0]
for ber in num:
    if max_num < ber:
        max_num = ber
    if min_num > ber:
        min_num = ber
print(min_num, max_num)