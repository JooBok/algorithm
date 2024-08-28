N = int(input())
default=2
for i in range(N):
    default=default+default-1
    result=default**2
print(result)