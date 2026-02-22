N = int(input())
A = list(map(int, input().split()))

A = [a - 1 for a in A]
answer=[0]*N

for i in range(N):
 
    path = []
    cur = i

    path_set = set()
    while cur not in path_set:
        path.append(cur)
        path_set.add(cur)
        cur = A[cur]
    
    loop_start=path.index(cur)
    before=len(path)
    loop=path[loop_start:]
    after=len(loop)
    
    K=10**100
    math=(K-before)%after
    
    answer[i]=loop[math-1]
    
print(*[x + 1 for x in answer])
