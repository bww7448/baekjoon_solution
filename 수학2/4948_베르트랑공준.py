import sys
import math
def Prime(num): 
    if num == 1: return False 
    n = int(math.sqrt(num)) 
    for k in range(2, n+1): 
        if num % k == 0: return False 
    return True 
A = []
while True:
    N = int(sys.stdin.readline())
    r = 0
    if N== 0:
        break
    else :
        for i in range(N+1, 2*N+1):
            if Prime(i) :
                r = r+1
        A.append(r)

for i in A:
    print(i)
