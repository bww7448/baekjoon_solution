N = int(input())
r = 0
for i in range (N):
    k = 0
    A = input()
    T = list(A)
    for j in range(len(T)-1):
        if T[j] == T[j+1]:
            T[j] = str(j)
    T.sort()
    for j in range(len(T)-1):
        if T[j] == T[j+1]:
            k = k+1
    if k == 0:
        r = r+1
print(r)
    



