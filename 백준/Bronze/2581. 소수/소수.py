M = int(input())
N = int(input())
result_list=[]  # 소수 저장용도
for num in range(M,N+1):
    count=0  # 소수인지 아닌지 확인하는 용도
    for n in range(1,num+1):
        if num%n==0:
            count+=1
    if count==2:
        result_list.append(num)
if result_list==[]:
    print(-1)
else:
    print(sum(result_list))
    print(min(result_list))