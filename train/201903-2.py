result = []
n = int(input())
for i in range(n):
    cal = input()
    call = ""
    for i in range(7):
        if cal[i] == "x":
            call += "*"
        elif cal[i] == "/":
            call += "//"
        else:
            call += cal[i]
    if eval(call) == 24:
        result.append("Yes")
    else:
        result.append("No")
for ___ in result:
    print(___)