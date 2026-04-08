
N=int(input())

A=list(map(int,input().split()))

count=0
for l in range(N):
    
    for r in range(l,N):
        total=0
        total=sum(A[l:r+1])

        if all(total % x !=0 for x in A[l:r+1]):
            count+=1


print(count)
