# import sys
# import math
# M, N = map(int, sys.stdin.readline().split())
# for i in range(M, N+1):
#     k = 0
#     r = 0
#     if i == 1 or i==4:
#         pass
#     elif i ==2 or i == 3:
#         r = r+1
#     else:
#         for j in range(2, math.ceil(i/2)):
#             if i%j ==0:
#                 k = k+1
#                 break
#         if k == 0:
#             r = r+1
#     if r!=0:
#         print(i)

import math 
def isPrime(num): 
    if num == 1: return False 
    n = int(math.sqrt(num)) 
    for k in range(2, n+1): 
        if num % k == 0: return False 
    return True 
    
# main 
m, n = map(int, input().split()) 
for k in range(m, n+1): 
    if isPrime(k) : print(k)

