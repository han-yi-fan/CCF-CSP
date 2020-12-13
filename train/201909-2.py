n = int(input())
trees = []
drop = [0 for i in range(n)]

for i in range(n):
    x = list(map(int,input().split()))
    trees.append(x[1])
    for _ in x[2:]:
        if _ <= 0:
            trees[i] += _
        else:
            if _ > 0 and trees[i] != _:
                drop[i] = 1
                trees[i] = _
T = sum(trees)
D = sum(drop)
E = 0
for i in range(len(drop)-2):
    if drop[i] == drop[i+1] == drop[i+2] == 1:
        E += 1
if drop[0] == drop[-2] == drop[-1] == 1:
    E += 1
if drop[0] == drop[1] == drop[-1] == 1:
    E += 1
print(T,D,E)
