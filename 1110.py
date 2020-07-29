N = int(input())
R = N
i = 1
while (True):
    b = R % 10
    a = (R-b) / 10
    R = 10*b + ((a+b) % 10)
    if R == N:
        break
    else : 
        i = i + 1
print(i)