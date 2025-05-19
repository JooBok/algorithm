import sys

input = sys.stdin.readline

N, M = map(int, input().split())
N_set = {input().strip() for _ in range(N)}

count = 0
for _ in range(M):
    if input().strip() in N_set:
        count += 1

print(count)