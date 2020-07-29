import sys
T = int(input())
N = []
n1 = []
n2 = []
for i in range (T):
    A, B = map(int, sys.stdin.readline().strip().split())
    n1.append(A)
    n2.append(B)
    N.append(A+B)
for i in range (T):
    print ("Case #{}:".format(i+1),"{} + {} =".format(n1[i], n2[i]), N[i])