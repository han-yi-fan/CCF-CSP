n,m = map(int,input().split())
trees = []
cut = []
for _ in range(n):
    x = list(map(int,input().split()))
    trees.append(x[0])
    cut.append(sum(x[1:]))
T = sum(trees) + sum(cut)
k = cut.index(min(cut))
P = cut[k]
print(T,k+1,-P)