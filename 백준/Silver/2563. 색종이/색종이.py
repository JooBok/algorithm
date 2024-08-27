N = int(input())  # 색종이 개수
array = [list(map(int, input().split())) for _ in range(N)]
grid = [[0] * 100 for _ in range(100)]  # 임시 100*100
total_area = 0
for x, y in array:
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            if grid[i][j] == 0:
                total_area += 1
            grid[i][j] += 1
print(total_area)