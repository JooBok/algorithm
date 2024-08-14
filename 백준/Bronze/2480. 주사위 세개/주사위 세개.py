num1, num2, num3 = map(int, input().split(' '))

if num1 == num2 == num3:
    won = 10000 + (num1 * 1000)
elif num1 == num2 != num3 or num1 == num3 != num2:
    won = 1000 + (num1 * 100)
elif num2 == num3 != num1:
    won = 1000 + (num2 * 100)
elif num1 != num2 != num3:
    won = max(num1, num2, num3) * 100

print(won)