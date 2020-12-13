n,m = map(int,input().split())
s = ""
for i in range(n):
    s += input()
dic = eval(s)

re = []
for i in range(m):
    se = input().split(".")
    if se[0] not in dic:
        re.append("NOTEXIST")
    else:
        if len(se) == 1:
            re.append(dic[se[0]])
        else:
            for j in range(len(se)):
                if se[j] in dic:
                    dic
