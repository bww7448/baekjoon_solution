# def d(n):
#     dn = n
#     for i in str(n):
#         dn = dn + int(i)
#     return dn
# SN = []
# for k in range(1, 10001):
#     r = 0
#     for j in range(1, k+1):
#         a = d(j)
#         if a == k:
#             r = r+1
#             break
#     if r == 0:
#         SN.append(k)
# for k in range (len(SN)):
#     print(SN[k])

natural_number_set = set(range(1, 10001))
generated_number_set= set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_number_set.add(i)

self_number_set = natural_number_set - generated_number_set

for i in sorted(self_number_set):
    print(i)