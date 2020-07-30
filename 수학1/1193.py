X = int(input())
d = 2
times = 2
summ = 1
while True :
    if X <= summ:
        break
    else:
        summ = summ + d
        d = d+1
        times = times + 1
if times % 2 == 0:
    a = summ-X+1
    b = times - a
else :
    b = summ-X + 1
    a = times - b
print("{}/{}".format(a,b))
