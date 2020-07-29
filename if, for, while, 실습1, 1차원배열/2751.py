num = []
far = int(input())
for i in range(far):
    num.append(int(input()))
num = sorted(num)
for i in range(far):
    print(num[i])
