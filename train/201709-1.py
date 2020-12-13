N = int(input())
s = 0
while N >= 50:
    s +=7
    N -= 50
while N >= 30:
    s +=4
    N -= 30
s += N//10
print(s)


