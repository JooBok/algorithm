import sys

input = sys.stdin.readline

N = int(input())
tmp=[]

for n in range(N):
    tmp.append(int(input()))
    
for t in sorted(tmp):
    print(t)