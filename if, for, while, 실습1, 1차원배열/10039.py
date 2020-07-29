avg = 0
for i in range(5):
    s = int(input())
    if s <40:
        s = 40
    avg = avg + s
print(int(avg/5))