from collections import defaultdict

N, K, M = map(int, input().split())

gems = defaultdict(list)

for _ in range(N):
    c, v = map(int, input().split())
    gems[c].append(v)

main = []
rest = []

for c in gems:
    gems[c].sort(reverse=True)
    main.append(gems[c][0])
    rest.extend(gems[c][1:])

main.sort(reverse=True)

ans = sum(main[:M])

candidates = main[M:] + rest
candidates.sort(reverse=True)

ans += sum(candidates[:K - M])

print(ans)
