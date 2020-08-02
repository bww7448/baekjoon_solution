import math
N = int(input())
A = list(map(int, input().split()))
r = 0
for i in A:
    k = 0
    if i == 1 or i==4:
        pass
    elif i ==2 or i == 3:
        r = r+1
    else:
        for j in range(2, math.ceil(i/2)):
            if i%j ==0:
                k = k+1
                break
        if k == 0:
            r = r+1
print(r)