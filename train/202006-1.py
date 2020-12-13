n,m = map(int,input().split())
A = []
B = []
for _ in range(n):
    x,y,type = input().split()
    if type == "A":
        A.append([int(x),int(y)])
    else:
        B.append([int(x),int(y)])
res = []
for __ in range(m):
    c1,c2,c3 = map(int,input().split())
    flag1 = []
    for point in A:
        if c1 + c2*point[0] + c3 * point[1] > 0:
            flag1.append(0)
        else:
            flag1.append(1)
    flag2 = []
    for point in B:
        if c1 + c2*point[0] + c3 * point[1] > 0:
            flag2.append(0)
        else:
            flag2.append(1)
    if ( sum(flag1) == 0 and sum(flag2) == len(flag2) ) or ( sum(flag2) == 0 and sum(flag1) == len(flag1) ):
        res.append("Yes")
    else:
        res.append("No")
for ___ in res:
    print(___) 