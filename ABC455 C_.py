import collections

N, K = map(int, input().split())
A = list(map(int, input().split()))

counts = collections.Counter(A)

group_sums = []
for val, count in counts.items():
    group_sums.append(val * count)

group_sums.sort(reverse=True)


total = sum(group_sums)

remove = group_sums[:K] 
result = total - sum(remove)

print(result)
