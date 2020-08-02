import sys

T = int(sys.stdin.readline())
A = [0]*10001
for i in range(T):
    j = int(sys.stdin.readline())
    A[j] += 1
for i in range(len(A)):
    if A[i] != 0:
        for j in range(A[i]):
            print(i)