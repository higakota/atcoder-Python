S=input()
N=[int(x) for x in S]

cur=N
answer=0

for i in range(100):
    answer=0
    
    for k in cur:
      answer+=k**2
        
    if answer==1:
     print('Yes')
     exit()
     
    cur=[int(x) for x in str(answer)]
       
print('No')


