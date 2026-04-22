import sys
input=sys.stdin.readline

N=int(input())

A=list(map(int,input().split()))

for i in range(N):
    count=[]

    if i>0:

        for j in range(i):

            if A[i]<A[j]:
                count.append(j+1)

    if count:
        print(count[-1])

    else:
        print(-1)
