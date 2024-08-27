array=[]
for _ in range(9):
    array.append(list(map(int, input().split())))
    tmp = 0  # 최대값 비교용
    roc=[]
    for i in array:
        if tmp<max(i):
            tmp=max(i)
        tmp=tmp
print(tmp)
for i in range(9):
    try:
        print((i+1), (array[i].index(tmp)+1))
    except:
        pass