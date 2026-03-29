def maxcount(a,b):
    max=0
    for i in range(H):
        count=0
        for j in range(W):
            if a[i][j] in b:
                count+=1
        if count>max:
            max=count

    return max
    
       


H,W,N=map(int,input().split())
A=[list(map(int,input().split()))for _ in range(H)]
B=[int(input()) for _ in range(N)]

result=maxcount(A,B)
print(result)
