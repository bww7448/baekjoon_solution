H, M = map(int, input().split())
if 45 <= M:
    M = M-45
else :
    H = H-1
    M = M+15
    if H < 0:
        H = H+24
print (H, M)