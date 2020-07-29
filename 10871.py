N, X = map(int, input().split())
A = []
zzin = []
A = input().split()
for i in range (N):
    if int(A[i]) < X:
        zzin.append(A[i])
print(' '.join(zzin))