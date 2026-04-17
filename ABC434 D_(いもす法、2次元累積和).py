import sys

input = sys.stdin.readline

def solve():
    sky=[[0]*2005 for _ in range(2005)]
    memory=[]
    count=0
    N=int(input())

    for _ in range(N):
        U,D,L,R=map(int,input().split())
        memory.append((U,D,L,R))

        sky[U][L] += 1
        sky[U][R+1] -= 1
        sky[D+1][L] -= 1
        sky[D+1][R+1] += 1

    
    
    for i in range(1, 2001):
        for j in range(1, 2001):
            sky[i][j] += sky[i][j-1]
    
    
    only_one_sum = [[0]*2002 for _ in range(2002)]
    for i in range(1, 2001):
        for j in range(1, 2001):
            sky[i][j] += sky[i-1][j]
            if sky[i][j] >= 1:
                count += 1
            
            
            val = 1 if sky[i][j] == 1 else 0
            
            only_one_sum[i][j] = val + only_one_sum[i-1][j] + only_one_sum[i][j-1] - only_one_sum[i-1][j-1]

    result = []
    for U,D,L,R in memory:
        
        minus = only_one_sum[D][R] - only_one_sum[U-1][R] - only_one_sum[D][L-1] + only_one_sum[U-1][L-1]
        
        current_count = count - minus
        number = 4000000 - current_count
        result.append(number)

    for res in result:
        print(res)

solve()
