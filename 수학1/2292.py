N = int(input())
A = [1]
if N == 1:
    print(1)
else:
    for i in range(18500):
        k = A[i] + 6*(i+1)
        A.append(k)
    for i in range(len(A)):
        if N > A[i] and N <= A[i+1]:
            print(i+2)
            break
