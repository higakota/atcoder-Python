
import sys

input = sys.stdin.readline

def solve():
    sky=[[0]*2001 for _ in range(2001)]
    memory=[]
    count=0
    N=int(input())

    for _ in range(N):
        U,D,L,R=map(int,input().split())
        memory.append((U,D,L,R))

        for i in range(U-1,D):
            for j in range(L-1,R):

                sky[i][j]+=1
                if sky[i][j]==1:
                    count+=1

    result=[]

    for U,D,L,R in memory:
        tmp=count
        for i in range(U-1,D):
            for j in range(L-1,R):
                
                if sky[i][j]==1:
                    count-=1
        

        number=2000*2000-count
        result.append(number)
        count=tmp
    

    for res in result:
        print(res)
solve()
