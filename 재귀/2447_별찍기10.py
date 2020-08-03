import sys
def star(x):
    if x == 1: 
        k = "*"
        return k
    else:
        star(x/3) * x 
        return k







x = int(sys.stdin.readline())
print(star(x))

