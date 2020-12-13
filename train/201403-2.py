N , M = map(int,input().split())
win = []
idx = []
for i in range(N):
    x1 , y1 , x2 , y2 = map(int,input().split())
    win.append([x1,x2,y1,y2])
    idx.append([x1,x2,y1,y2])
win.reverse()
p = []
for i in range(M):
    x , y = map(int,input().split())
    pp = None
    for w in range(len(win)):
        window = win[w]
        if x in range(window[0],window[1]+1) and y in range(window[2],window[3]+1):
            pp = idx.index(window)+1
            del win[w]
            win = [window] + win
            break
        else:
            continue
    if pp == None: p.append("IGNORED")
    else: p.append(pp)

for i in p:
    print(i)

