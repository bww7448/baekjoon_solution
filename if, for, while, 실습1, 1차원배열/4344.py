C = int(input())
A = []
S = []
for i in range(C):
    B = list(map(int, input().split()))
    A.append(B)
for i in range(C):
    total = 0
    for j in range(1, A[i][0]+1):
        total = total + A[i][j]
    avg = total / A[i][0]
    r = 0
    for j in range(1, A[i][0]+1):
        if A[i][j] > avg:
            r = r + 1
        else :
            pass
    print("%.3f%%" % (r / A[i][0] *100))