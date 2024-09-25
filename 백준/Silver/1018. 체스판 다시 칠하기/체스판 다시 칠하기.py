N, M=map(int, input().split())
boards=[]
for _ in range(N):
    board = input()
    boards.append(board)
result_list=[]
# 8*8 배열 개수 찾기
for m in range(0, M-8+1):
    for n in range(0, N-8+1):
        count=0
        # 잘못된 색 찾기
        for i in range(n, n+8):
            for j in range(m, m+8):
                if i%2 == 0 and j%2 == 0:
                    if boards[i][j] != 'W':
                        count+=1
                if i%2 == 0 and j%2 != 0:
                    if boards[i][j] != 'B':
                        count+=1
                if i%2 != 0 and j%2 == 0:
                    if boards[i][j] != 'B':
                        count+=1
                if i%2 != 0 and j%2 != 0:
                    if boards[i][j] != 'W':
                        count+=1
        if count >= 32:
            count=64-count
        result_list.append(count)
print(min(result_list))