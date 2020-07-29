import sys
T = int(input())
N = []
for i in range (T):
    A, B = map(int, sys.stdin.readline().strip().split())
    N.append(A+B)
for i in range (T): 
    print(N[i])