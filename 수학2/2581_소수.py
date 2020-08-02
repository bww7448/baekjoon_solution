import sys
import math
M = int(sys.stdin.readline())
N = int(sys.stdin.readline())
T = 0
k = 0
h = -1
for i in range(N, M-1, -1):
    if i == 1 or i ==4:
        pass
    else:
        r = 0
        for j in range(2, math.ceil(i/2)):
            if i % j == 0:
                r = r+1
                break
        if r == 0:
            T += i
            k = i
            h = h+1
if h == -1:
    print(h)
else:      
    print(T)
    print(k)