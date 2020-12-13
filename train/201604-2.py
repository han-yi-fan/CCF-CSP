# def lstadd(lst1,lst2):
#     result = []
#     for i in range(len(lst1)):
#         result.append(lst1[i]+lst2[i])
#     return result

# init=[]
# for _ in range(15):
#     line = list(map(int,input().split()))
#     init.append(line)
# init.reverse()

# new_block = []
# for __ in range(4):
#     line = list(map(int,input().split()))
#     new_block.append(line)
# new_block.reverse()

# loc = int(input())-1

# i = 0    # init
# j = 0    # new_block
# while i != 11 and j != 4:
#     if lstadd(init[i][loc:loc+4],new_block[j]) == init[i][loc:loc+4]:
#         j += 1
#         continue
#     elif 2 in lstadd(init[i][loc:loc+4],new_block[j]):
#         i += 1
#         continue
#     else:
#         init[i][loc:loc+4] = lstadd(init[i][loc:loc+4],new_block[j])
#         i += 1
#         j += 1
#         continue

# init.reverse()
# for line in init:
#     print(str(line)[1:-1].replace(",",""))

tmap = []
 
for i in range(15):
	tmap.append(list(map(int,input().split())))
for i in range(3):
	tmap.append([1]*10)
 
shape = []
for i in range(4):
	shape.append(list(map(int,input().split())))

x = int(input())
 

for i in range(4): 
	shape[i] = [0]*(x-1) + shape[i] + [0]*(10-4-(x-1))

right = 0
find = False
 
for i in range(15):
	for j in range(4):
		newline = [a+b for a,b in zip(tmap[i+j],shape[j])]
		if(2 in newline):
			right = i-1
			find = True
			break
	if(find):
		break
	if(i == 14):
		right=14
 
for j in range(4):
	tmap[right+j]= [a+b for a,b in zip(tmap[right+j],shape[j])]

for i in range(15):
	print(" ".join(map(str,tmap[i])))