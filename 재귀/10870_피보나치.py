import sys

def pivo(N):
    if N == 0 : 
        return 0
    elif N == 1:
        return 1
    else :
        X = pivo(N-1) + pivo(N-2)
        return(X)

N = int(sys.stdin.readline())
print(pivo(N))