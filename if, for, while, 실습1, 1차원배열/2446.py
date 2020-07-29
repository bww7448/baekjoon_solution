# N = int(input())
# for i in range (1, N):
#     s = "*"*(2*N-2*i+1)
#     print(s.center(2*N-1))
# for j in range(1, N+1):
#     s="*"*(2*j-1)
#     print(s.center(2*N-1))

N = int(input())
for i in range (1, N):
    print(" " * (i), "*" * (2*(N-i)-1))
for i in range (1, N-1):
    print(" "*(N-1-i), "*"*(2*i+1))