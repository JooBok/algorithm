a = input()
tmp=[]
for i in range(1,9*len(a)):
    if int(a) > i:
        b = int(a)-i
        count=0
        for c in str(b):
            count+=int(c)
        if count==i:
            tmp.append(b)
if tmp == []:
    print(0)
else:
    print(tmp[-1])