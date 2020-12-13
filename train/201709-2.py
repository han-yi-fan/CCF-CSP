N,K = map(int,input().split())
keys = [i for i in range(1,N+1)]

datas = []
for i in range(K):
    temp = list(map(int,input().split()))  
    # 拆分操作为借还操作
    datas.append([temp[0],temp[1],1])
    datas.append([temp[0],temp[1]+temp[2],2])

# 按借或还的操作时间、先还后借、操作钥匙的顺序进行排序
datas.sort(key=lambda temp: (temp[1],-temp[2],temp[0]))

for data in datas:
    if data[2] == 1:
        keys[keys.index(data[0])] = 0
    else:
        keys[keys.index(0)] = data[0]

for key in keys:
    print(key,end=" ")