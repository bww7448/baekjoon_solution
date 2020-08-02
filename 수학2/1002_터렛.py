import sys
import math
T = int(sys.stdin.readline())
for i in range(T):
    x1, x2, r1, y1, y2, r2 = map(int, sys.stdin.readline().split())

    d = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if x1 == x2 and y1 == y2 and r1 == r2:
        print (-1)
    elif x1 == x2 and y1 == y2 and r1 != r2:
        print(0)
    else:
        if r1+r2 == d or r1 - r2 == d or r2 - r1 ==d:
            print(1)
        elif r1 + r2 < d or d+ r1 < r2 or d+r2 < r1:
            print(0)
        elif r1+r2 > d:
            print(2)