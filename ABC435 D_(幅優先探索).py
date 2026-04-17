import sys
from collections import deque


input = sys.stdin.readline

def solve():
    
    N, M = map(int, input().split())
    
    
    rev_adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        X, Y = map(int, input().split())
        rev_adj[Y].append(X)
    
    
    can_reach_black = [False] * (N + 1)
    
    
    todo = deque()
    
    Q = int(input())
    ans = []
    
    for _ in range(Q):
        query = list(map(int, input().split()))
        
        if query[0] == 1:
            v = query[1]
            
            if not can_reach_black[v]:
                can_reach_black[v] = True
                todo.append(v)
                
                
                while todo:
                    now = todo.popleft()
                    for next_node in rev_adj[now]:
                        if not can_reach_black[next_node]:
                            can_reach_black[next_node] = True
                            todo.append(next_node)
                            
        else:
            v = query[1]
            
            if can_reach_black[v]:
                ans.append("Yes")
            else:
                ans.append("No")
    
    
    print('\n'.join(ans))

solve()
