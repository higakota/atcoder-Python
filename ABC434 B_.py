N,M=map(int,input().split())
kind=[0]*M
plus=[0]*M

for i in range(N):
    A,B=map(int,input().split())
    count=0
    sum=0
    count=kind[A-1]
    sum=count+B
    kind[A-1]=sum
    plus[A-1]+=1

for i in range(M):
    print(kind[i]/plus[i])

