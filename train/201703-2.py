n = int(input())
line = [i for i in range(1,n+1)]
m = int(input())
for _ in range(m):
    name,change = map(int,input().split())
    idx = line.index(name)
    line.remove(name)
    line = line[:idx+change] + [name] + line[idx+change:]
print(" ".join(map(str,line)))
