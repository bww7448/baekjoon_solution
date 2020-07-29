C = int(input())
A = []
for i in range(C):
    B = list(map(int, input().split()))
    A.append(B)
for i in range(C):
    total = 0
    for j in range(1, A[i][0]):
        total = A[i][j]