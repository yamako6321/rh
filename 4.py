m = 0
n = list(map(int, input().split()))
print(n)
for i in n:
    if i >= 100 and i <=999:
        m += 1
print(m)

