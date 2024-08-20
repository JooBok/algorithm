N = int(input())
stars = []
for i in range(0,N*2,2):
    stars.append(i+1)
for j in range((N-1)*2,0,-2):
    stars.append(j-1)
for k in range(2*N-1):
    space = abs(N-k-1)
    print(' '*space + '*'*stars[k])