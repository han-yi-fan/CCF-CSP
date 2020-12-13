n,a,b = map(int,input().split())
u = {}
v = {}
for i in range(a):
    index, value = map(int,input().split())
    u[index] = value
for i in range(b):
    index, value = map(int,input().split())
    v[index] = value
s = 0
for index,value in u.items():
    if index in v:
        s += value*v[index]
print(s)