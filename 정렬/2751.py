# T = int(input())
# A = []

# for i in range(T):
#     s = int(input())
#     if s > len(A):
#         for j in range(s-len(A)):
#             A.append(0)
#     A[s-1] += 1
# for i in range(len(A)):
#     if A[i] != 0:
#         for j in range(A[i]):
#             print(i+1)

import sys

ipt = sys.stdin.readline
arr = []

for i in range(int(ipt())):
    arr.append(int(ipt()))

arr = sorted(arr)

for i in arr:
    print(i)


        
