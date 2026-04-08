
N=int(input())
A=list(map(int,input().split()))

limit=1+A[0]
count=1

for i in range(2,N+1):
    
    if i<limit:
        count+=1

        if i+A[i-1]>limit:
            limit=i+A[i-1]

    else:
        break

print(count)
