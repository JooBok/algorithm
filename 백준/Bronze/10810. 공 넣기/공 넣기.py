N, M = map(int, input().split(' '))
num_list = []
for _ in range(N):
    num_list.append(0)
for _ in range(M):
    i, j, k = map(int, input().split(' '))
    for l in range(i,j+1):
        num_list[l-1] = k
for num in num_list:
    print(num, end=' ')