
def MagicSquare(N):

    a=[[0]*N for _ in range(N)]
    r=0
    c=int((N-1)/2)
    k=1
    a[r][c]=k

    for j in range(N**2-1):
       k+=1
       if a[(r-1)%N][(c+1)%N]==0:
        a[(r-1)%N][(c+1)%N]=k
        r=(r-1)%N
        c=(c+1)%N

       else:
        a[(r+1)%N][c]=k
        r=(r+1)%N
       
       

    return a
   

n=int(input())
result=MagicSquare(n)

for row in result:
    print(*(row))
