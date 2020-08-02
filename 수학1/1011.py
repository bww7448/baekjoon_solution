def move(i):
    r[1] = r[i]
    r[0] = r[1]-1
    r[2] = r[1]+1
    k = k+1
    return r, k
T = int(input())
A = []
for l in range (T):
    n = 1
    k = 1
    x, y = map(int, input().split()) 
    if x == y-1:
        pass
    elif x == y-2:
        k=k+1
    else:
        while True:
            n = n + 1
            if (y-x) > n*(n+1):
                pass
            else :
                break
        if (y-x) > n**2:
            k = 2*n
        else:
            k = 2*n-1
    A.append(k)

for i in A:
    print(i)
