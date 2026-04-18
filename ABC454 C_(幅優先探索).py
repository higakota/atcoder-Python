import sys
from collections import deque
input = sys.stdin.readline


N,M=map(int,input().split())

AB={}

for _ in range(M):
    a,b=map(int,input().split())
    
    if a not in AB:
        AB[a]=[]

    AB[a].append(b)


queue=deque([1])
count={1}

while queue:
    node=queue.popleft()


    if node in AB:
        for next_node in AB[node]:
            if next_node not in count:
                count.add(next_node)
                queue.append(next_node)



print(len(count))
