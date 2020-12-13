class ball:
    def __init__(self,ori,posi):
        self.ori=ori
        self.posi=posi

n,L,t = map(int,input().split())
balls = []
posis = list(map(int,input().split()))
for i in posis:
    balls.append(ball(1,i))
for i in range(t):
    for bal in balls:
        if (bal.posi==L and bal.ori==1) or (bal.posi==0 and bal.ori==-1):
            bal.ori *= -1
        bal.posi += bal.ori
    for lidx in range(len(balls)-1):
        for ridx in range(lidx+1,len(balls)):
            if balls[lidx].posi == balls[ridx].posi:
                balls[lidx].ori *= -1
                balls[ridx].ori *= -1
                break
for ball in balls:
    print(str(ball.posi),end=' ')