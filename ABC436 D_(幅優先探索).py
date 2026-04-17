import sys
from collections import deque

def solve():
    
    input = sys.stdin.readline
    H,W = map(int, input().split())
    
    grid = [input().strip() for _ in range(H)]
    

    warp_portals = {}
    for r in range(H):
        for c in range(W):
            char = grid[r][c]
            if 'a' <= char <= 'z':
                if char not in warp_portals:
                    warp_portals[char] = []
                warp_portals[char].append((r, c))
    
   
    dist = [[-1] * W for _ in range(H)]
    queue = deque([(0, 0)]) 
    dist[0][0] = 0
    
    
    used_warp_chars = set()
    
    while queue:
        r, c = queue.popleft() 
        
        
        if r == H - 1 and c == W - 1:
            print(dist[r][c])
            return

        
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            
            
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != '#' and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                queue.append((nr, nc))
        
        char = grid[r][c]
        if 'a' <= char <= 'z' and char not in used_warp_chars:
            
            for wr, wc in warp_portals[char]:
                if dist[wr][wc] == -1:
                    dist[wr][wc] = dist[r][c] + 1
                    queue.append((wr, wc))
            
    
            used_warp_chars.add(char)

    
    print(-1)

solve()
