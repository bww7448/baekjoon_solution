import math
N = int(input())
a = int(math.floor(N/5))
b = N - 5*a
if b == 0:
    c = 0
elif b == 1:
    a = a-1
    c = 2
elif b == 2:
    a = a-2
    c = 4
elif b == 3:
    c = 1
elif b ==4:
    a = a-1
    c = 3
if a < 0:
    print(-1)
else:
    print(a+c)