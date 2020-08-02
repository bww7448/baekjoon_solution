import sys
import math
def Prime(num): 
    if num == 1: return False 
    n = int(math.sqrt(num)) 
    for k in range(2, n+1): 
        if num % k == 0: return False 
    return True 
A = []
T = int(sys.stdin.readline())
for i in range (T):
    N = int(sys.stdin.readline())
    a = int(N/2)
    b = int(N/2)
    while True:
        if Prime(a) and Prime(b) :
            A.append(a)
            A.append(b)
            break
        else :
            a = a-1
            b = b+1
for i in range(0, len(A), 2):
    print(A[i], A[i+1])