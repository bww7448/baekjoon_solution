R=[]
r = 0
for i in range(42):
    R.append(0)

for i in range(10):
    a = int(input())
    b = a % 42
    R[b] = R[b]+1

for i in range(42):
    if R[i]>0:
        r = r+1

print(r)