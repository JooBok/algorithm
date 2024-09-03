N = int(input())
result_list=[]
for n in range(2,N+1):
    while True:
        if N%n==0:
            result_list.append(n)
            N=N//n
        else:
            break
for p in result_list:
    print(p)