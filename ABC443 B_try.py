N,K=map(int,input().split())
sum=0
count=0
while sum<K:
  sum+=N
  N+=1
  count+=1
  
  
print(count-1)
