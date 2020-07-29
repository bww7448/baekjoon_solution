def AP(N):
    if N < 100:
        print(N)
    elif N == 1000:
        print("144")
    else:
        A = 99
        for i in range (100, N+1):
            R = []
            for j in str(i):
                R.append(int(j))
            if R[0] - R[1] == R[1] - R[2]:
                A = A+1
        print(A)
N = int(input())
AP(N)
            
