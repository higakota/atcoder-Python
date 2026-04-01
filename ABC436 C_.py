import sys
input = sys.stdin.readline

N, M = map(int, input().split())

used_cells = set()

count = 0

for _ in range(M):
    r, c = map(int, input().split())
    
    
    yoncells = [
        (r, c), (r + 1, c),
        (r, c + 1), (r + 1, c + 1)
    ]
    
    
    can_place = True
    for cell in yoncells:
        if cell in used_cells:
            can_place = False
            break
            
    if can_place:
        
        for cell in yoncells:
            used_cells.add(cell)
        count += 1

print(count)
