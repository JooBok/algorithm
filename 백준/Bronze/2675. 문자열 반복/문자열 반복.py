T = int(input())
for i in range(T):
    R, S = map(str, input().split(' '))
    tmp = ''
    for j in S:
        tmp+=j*int(R)
    print(tmp)