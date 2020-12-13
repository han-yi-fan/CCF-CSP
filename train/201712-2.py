n,k = map(int,input().split())
cur_num = 1
people = [i for i in range(1,n+1)]

idx = 0

while len(people) != 1:
    
    if idx == len(people)-1 and ( cur_num%k ==0 or str(cur_num).endswith(str(k)) ):
        people.remove(people[idx])
        idx = 0
        cur_num+=1
    elif cur_num%k ==0 or str(cur_num).endswith(str(k)):
        people.remove(people[idx])
        cur_num+=1
    elif idx == len(people)-1:
        idx = 0
        cur_num += 1
    else:
        idx += 1
        cur_num += 1       

print(people[0])