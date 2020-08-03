import sys

def factorial(N):
    X = 1
    if N == 0 : 
        return 1
    if N == 1 : 
        return 1
    else :
        X = N*factorial(N-1)
        return X
N= int(sys.stdin.readline())
print(factorial(N))