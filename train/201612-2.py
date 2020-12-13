
mon=[3500,3500+1500,3500+4500,3500+9000,3500+35000,3500+55000,3500+80000]
tax=[0.03,0.1,0.2,0.25,0.3,0.35,0.45]
tax_range=[3500]
for i in range(1,len(tax)):
    tax_range+=[int(tax_range[i-1]+(mon[i]-mon[i-1])*(1-tax[i-1]))]

t=int(input())
for i in range(len(tax_range)+1):
    if i == len(tax_range):
        break
    elif t<tax_range[i]:
        break
if i==0:
    print(t)
else:
    print(int(mon[i-1]+(t-tax_range[i-1])/(1-tax[i-1])))