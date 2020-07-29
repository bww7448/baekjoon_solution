# import sys
# N = int(input())
# A = []
# for i in range(N):
#     r, S = map(str, sys.stdin.readline().strip().split())
#     R = int(r)
#     A.append(R)
#     A.append(S)
# for j in range(int(len(A)/2)):
#     print()
#     for i in A[2*j+1]:
#         print(i*A[2*j], end = '')

t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)