n = int(input())
orders = list(map(int,input().split()))
seat = [[0 for _ in range(5)] for __ in range(20)]

buy = []
for order in orders:
    flag = 0
    for j in range(20):
        if 5 - sum(seat[j]) >= order:
            idx = seat[j].index(0)
            buy.append([ str(j*5+i+1) for i in range(idx,order+idx)])
            seat[j][idx:idx+order] = [1 for __ in range(order)]
            flag = 1
            break
    if flag == 0:
        bb = []
        for j in range(20):
            if sum(seat[j]) != 5 and order != 0:
                empty = 5 - sum(seat[j])
                idx = seat[j].index(0)
                bb += [ str(j*5+i+1) for i in range(idx,order+idx) ]
                seat[j][idx:idx+order] = [1 for __ in range(order)]
                order -= empty
            if order == 0:
                break
        buy.append(bb)
for _ in buy:
    print(" ".join(_))