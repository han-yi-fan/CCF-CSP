paper = [[0 for _ in range(100)] for __ in range(100)]
n = int(input())
for  i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    for y in range(y1,y2):
        paper[y][x1:x2] = [1 for ___ in range(x2-x1)]
s = 0
for i in paper:
    s += sum(i)
print(s)