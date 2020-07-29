import math
N = int(input())
for i in range (1, N+1):
    print("* " * math.ceil(N/2))
    print(" *" * math.floor(N/2))