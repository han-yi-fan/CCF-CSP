n,k = map(int,input().split())
cake = list(map(int,input().split()))
s = 0
x = 0
for _ in range(n):
    x += cake[_]
    if x < k and _ == n-1:
        s += 1
    if x >= k:
        s += 1
        x = 0
    else:
        continue

print(s)
