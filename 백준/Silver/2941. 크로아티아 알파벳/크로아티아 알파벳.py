S = input()
S=S.replace('c=','c')
S=S.replace('c-','c')
S=S.replace('dz=','d')
S=S.replace('d-','d')
S=S.replace('lj','l')
S=S.replace('nj','n')
S=S.replace('s=','s')
S=S.replace('z=','z')
count=0
for s in S:
    count+=1
print(count)