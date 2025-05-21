import sys

input = sys.stdin.readline

N = input()
N_list = sorted(N, reverse=True)

num = ''
for n in N_list:
    num+=n

print(int(num))