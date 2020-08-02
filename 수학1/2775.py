T = int(input())
A = []
for i in range (T):
    k = int(input())
    n = int(input())
    s = [j for j in range(1,n+1)]
    for j in range (k):
        for l in range(1, n):
            s[l] = s[l] + s[l-1]
    A.append(s[n-1])
for i in A:
    print(i)


