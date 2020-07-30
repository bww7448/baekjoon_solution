import math
A, B, C = map(int, input().split())
if C > B :
    N = math.trunc(A/(C-B)) + 1
    print(N)
else : 
    print("-1")