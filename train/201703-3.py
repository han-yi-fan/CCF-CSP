lines = []
line = input()
while line != None:
    lines.append(line)
    line = input()
result = []
for idx in len(lines):
    if lines[idx] == "\n":
        result.append("\n")
    elif "#" in lines[idx]:
        num = line.count("#")
        new_line = "<h"+str(num)+">"+line[2:]+"</h"+str(num)+">"
    elif "*" in lines[idx]:
        new_line = "<li>" + lines[idx][2:] + "/li"
        result.append(new_line)
        if lines[idx-1] == "\n":
            result[idx-1] = "<ul>"
        elif lines[idx+1] == "\n":
            result.append("ul")
    else:
        if lines[idx-1] == lines[idx+1] == "\n":
            new_line = "p"+lines[idx]+"/p"
            result.append(new_line)
        elif lines[idx-1] == "\n":
            new_line = "p"+lines[idx]
            result.append(new_line)
        elif lines[idx+1] == "\n":
            new_line = lines[idx] + "/p"
            result.append(new_line)
        else:
            result.append(lines[idx])
for _ in result:
    if "_" in _:
        loc = _.index("_")
        _[loc] = "<em>"
        loc = _.index("_")
        _[loc] = "</em>"
    if "[" in _:
        loc_0 = _.index("[")
        loc_1 = _.index("]")
        text = _[loc_0:loc_1]
        loc_2 = _.index("(")
        loc_3 = _.index(")")
        link = _[loc_2:loc_3]
        new_line = _[:loc_0] + "<a herf=\" "+link+">"+text+"/a"+_.[loc_3:]
        loc = result.index(_)
        result[_] = new_line
for line in result:
    if line == "\n":
        continue
    else:
        print(line)
        



