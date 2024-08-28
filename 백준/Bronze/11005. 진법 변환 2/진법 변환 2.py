N,B = map(int, input().split())
change=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
result=''
while True:
    if N!=0:
        N,C = divmod(N,B)
        if B>=10 and C>=10:
            result+=change[C-10]
        else:
            result+=str(C)
    elif N==0:
        break
print(result[::-1])