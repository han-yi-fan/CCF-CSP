
n,m=map(int,input().split())
rules={}
var={}
for i in range(n):
    key,value=input().split()
    rules[key]=key.split('/')
    var[key]=value
for i in range(m):
    s=input().split('/')
    find=1
    for k in rules:
        rule=rules[k]
        path=0
        out=[]
        match=0
        if len(s)>=len(rule):
            for j in range(len(rule)):
                if s[j]==rule[j]:
                    match+=1
                elif s[j].isdigit() and rule[j]=='<int>':
                    out.append(str(int(s[j])))
                    match+=1
                elif rule[j]=='<str>':
                    if s[j]=='':
                        break
                    out.append(s[j])
                    match+=1
                elif rule[j]=='<path>':
                    out.append('/'.join(s[j:]))
                    path=1
                    match+=1
            if match==len(rule) and (len(s)==len(rule) or path):
                print(var[k],' '.join(out))
                find=0
                break
    if find:
        print('404')