import sys
ax, ay = map(int, sys.stdin.readline().split())
bx, by = map(int, sys.stdin.readline().split())
cx, cy = map(int, sys.stdin.readline().split())

if ax == bx: 
    dx = cx 
elif ax == cx:
    dx = bx
else :
    dx = ax
if ay == by: 
    dy = cy 
elif ay == cy:
    dy = by
else :
    dy = ay

print (dx, dy)