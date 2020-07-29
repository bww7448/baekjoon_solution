import math
A = int(input())
B = int(input())
C = int(input())
T = A * B * C
U = [0,0,0,0,0,0,0,0,0,0]
if T < 10**7 :
    U[0] = -2
elif T < 10**8:
    U[0] = -1
for i in range (9):
    k = 10**(8-i)
    r = math.floor(T/k)
    U[r] = U[r]+1
    T = T-r*k
for i in range (10):
    print(U[i])