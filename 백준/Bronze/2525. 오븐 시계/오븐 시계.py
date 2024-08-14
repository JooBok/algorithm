hour, min = map(int, input().split(' '))
time = int(input())

min = min + time
if min >= 60:
    hour = hour + (min // 60)
    min = min % 60

if hour >= 24:
    hour = hour % 24

print(f'{hour} {min}')