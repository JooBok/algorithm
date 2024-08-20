chess = list(map(int, input().split()))
needs = []
ori_chess = [1,1,2,2,2,8]
for o in range(len(ori_chess)):
    tmp = ori_chess[o] - chess[o]
    needs.append(tmp)
for i in needs:
    print(i, end=' ')