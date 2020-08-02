A = []
while True:
    x, y, z = map(int, input().split())
    if x==0 :
        for i in A:
            print(i)
        break
    else:
        if 2*(max(x, y, z)**2) == x**2 + y**2 + z**2:
            A.append("right")
        else:
            A.append("wrong")