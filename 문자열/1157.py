C = [-1]*26
S = input()
for i in S:
    if ord(i) > 91 :
        t = chr(ord(i)-32)
    else : 
        t = i
    C[ord(t)-65] += 1
Y = sorted(C)
if Y[24] == Y[25]:
    print("?")
else : 
    idx = C.index(max(C))
    print(chr(idx+65))
