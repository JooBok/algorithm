N, M = map(int, input().split(' '))
num_list = []
for n in range(N):
    num_list.append(n+1)
for _ in range(M):
    i, j = map(int, input().split(' '))
    num_list[i-1], num_list[j-1] = num_list[j-1], num_list[i-1]

for num in num_list:
    print(num, end=' ')