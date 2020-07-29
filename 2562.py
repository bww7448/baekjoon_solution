# A = []
# for i in range(9):
#     a = int(input())
#     A.append(a)
# max_num = A[0]
# for i in range(9) :
#     if max_num < A[i]:
#         max_num = A[i]
#         r = i
# print(max_num)
# print(r+1)

a = []
for i in range(9):
    a.append(int(input()))
print(max(a))
print(a.index(max(a))+1)

