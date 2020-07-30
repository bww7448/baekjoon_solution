
A, B, V = map(int, input().split())
T = (V-B) % (A-B)
C = (V-B) // (A-B)
if T == 0:
    print(C)
else :
    print(C+1)