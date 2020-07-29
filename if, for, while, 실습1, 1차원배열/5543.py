a = 0
b = 2000
c = 0
d = 2000
for i in range(3):
    a = int(input())
    if a < b:
        b = a
for j in range(2):
    c = int(input())
    if c < d:
        d = c
print(b+d-50)