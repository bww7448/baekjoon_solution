N = int(input())
A = []
T = 0
A = list(map(int, input().split()))
max_score = max(A)
for i in range(N):
    A[i] = (A[i]*100)/max_score
    T = T + A[i]
print(T/N)
        