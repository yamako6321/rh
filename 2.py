n = int(input())
m = 0
for i in range(1, n+1):
    s = int(input())
    if s < 0:
        m += 1
print(m)