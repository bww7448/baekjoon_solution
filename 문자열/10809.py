alpha = input()
L = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
beta = "abcdefghijklmnopqrstuvwxyz"
for i in beta:
    r = -1
    for j in alpha :
        r = r+1
        if i == j:
            L[ord(j)-97] = r
            break
for i in L:
    print(i, end = ' ')
