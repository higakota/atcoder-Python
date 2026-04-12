from collections import defaultdict

N,M=map(int,input().split())
my_dict = defaultdict(list)
my_query =defaultdict(list)

for i in range(1,N+1):
    my_dict[i].append(i)

for _ in range(M):
    X, Y = map(int, input().split())
    my_dict[X].append(Y)
    
while True:
    changed = False 
    
    for key in range(1, N + 1):
        
        old_values = set(my_dict[key])
        
        
        new_values = set(old_values)
        for v in old_values:
            new_values.update(my_dict[v])
        
        
        if new_values != old_values:
            my_dict[key] = list(new_values)
            changed = True 
            
    
    if not changed:
        break


Q=int(input())
result=[]
for _ in range(Q):
    z, v = map(int, input().split())
    if z==1:
        my_query[z].append(v)

    if z==2:
        if any(d in my_dict[v] for d in my_query[1]):
            result.append("Yes")

        else:
            result.append("No")

for res in result:
    print(res)
