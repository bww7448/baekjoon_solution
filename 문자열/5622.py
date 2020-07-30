import math
T = input()
r = 0
for i in T:
    if ord(i) < 80 :
        t = math.floor((ord(i)+1)/3)-19
    elif ord(i)>83 and ord(i) < 87:
        t = math.floor(ord(i)/3)-19
    elif ord(i) <= 83 and ord(i) >=80:
        t = math.floor(ord(i)/4) - 12
    elif ord(i) >= 87:
        t = math.floor((ord(i)+1)/4) - 12 
    r = r+t
print(int(r))