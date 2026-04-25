H,W=map(int,input().split())

S=[list(input()) for i in range(H)]
ans=0


for h1 in range(H):
    for h2 in range(h1, H):
        for w1 in range(W):
            for w2 in range(w1, W):
                
                symmetric = True
                for i in range(h1, h2 + 1):
                    for j in range(w1, w2 + 1):
                        
                        ni = h1 + h2 - i
                        nj = w1 + w2 - j
                        
                        
                        if S[i][j] != S[ni][nj]:
                            symmetric = False
                            break
                    if not symmetric:
                        break
                
                
                if symmetric:
                    ans += 1

print(ans)
