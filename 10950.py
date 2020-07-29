T = int(input())
N = []
for i in range(T):
    A, B = map(int, input().split())
    N.append(A+B)
for i in range(T):
    print(N[i])
