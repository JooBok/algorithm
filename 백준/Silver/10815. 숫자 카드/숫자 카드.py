import sys

input = sys.stdin.readline

N = int(input())
N_nums = set(map(int, input().split()))
M = int(input())
M_nums = input().split()

print(' '.join(['1' if int(m) in N_nums else '0' for m in M_nums]))