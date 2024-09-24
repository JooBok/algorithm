import sys
N=int(sys.stdin.readline())
cnt_list=[0]*10001
for _ in range(N):
    n=int(sys.stdin.readline())
    cnt_list[n] += 1
for i in range(10001):
    if cnt_list != 0:
        for _ in range(cnt_list[i]):
            print(i)