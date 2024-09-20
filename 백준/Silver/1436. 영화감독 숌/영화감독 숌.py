N = int(input())
n = 0
number = 0
while True:
    n += 1
    if '666' in str(n):
        number += 1
        if number == N:
            break
print(n)