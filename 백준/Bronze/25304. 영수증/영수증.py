X = int(input())
won = 0
for _ in range(int(input())):
    price, num = map(int, input().split(' '))
    won += (price * num)
if X == won:
    print('Yes')
else:
    print('No')