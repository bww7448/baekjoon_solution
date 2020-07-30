T = int(input())
A = []
for i in range(T):
    txt = ""
    H, W, N = map(int, input().split())
    if N%H == 0:
        fr = str(H)
        bk = N // H
    else:
        fr = str(N % H)
        bk = N // H + 1
    if bk > 9:
        bk = str(bk)
    else:
        bk = "0" + str(bk)
    txt += (fr+bk)
    A.append(txt)
for i in range(T):
    print(A[i])    