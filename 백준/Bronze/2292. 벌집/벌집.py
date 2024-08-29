N=int(input())
n=0
default=1
while True:
    default+=6*n
    n+=1
    if N<=default:
        print(n)
        break