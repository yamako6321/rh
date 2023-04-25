m = 0
n = int(input())
for i in range(n):
    a = int(input())
    if abs(a) % 100 == 12:
        m += 1
print(m)