N, X = map(int, input().split(' '))
for i in list(filter(lambda x: x < X, list(map(int, input().split(' '))))):
    print(i, end=' ')