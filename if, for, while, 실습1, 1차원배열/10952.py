zzin = []
while True:
    A, B = map(int, input().split())
    if A==0 and B==0:
        break
    else:
        zzin.append(A+B)
for i in range (len(zzin)):
    print(zzin[i])