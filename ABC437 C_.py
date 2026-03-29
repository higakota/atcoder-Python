T=int(input())

for _ in range(T):
    price=[]
    totalpower=0
    M=0
    count=0
    N=int(input())
    for i in range(N):
        W,P=map(int,input().split())
        price.append(W+P)
        totalpower+=P
    
    price.sort()
        
    for i in range(len(price)):
        M+=price[i]
            
        if totalpower>=M:
            count+=1
        else:
            break

    print(count)
