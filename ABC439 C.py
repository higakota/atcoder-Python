from collections import Counter

N=int(input())
sum=[]
B=[]
count=0
limit = int(N**0.5) + 1

for i in range(1,limit):
  for j in range(i+1,limit):
    val=i**2+j**2
    if val<=N:
      sum.append(val)
      
counts = Counter(sum)

for i in range(len(sum)):
  if counts[sum[i]]==1:
       count+=1
       B.append(sum[i])
       
B.sort()   
print(count)
print(*B)
