N = int(input())
A = []
for i in range (N):
    a = input()
    a = a.split("X")
    A.append(a)
for i in range (N):
    r=0
    for j in range (len(A[i])):
        b = len(A[i][j])
        for k in range (b):
            b = b+k
        r=r+b
    print(r)        
        
