S = input()
MOD = 998244353


dp = [0] * len(S)
dp[0] = 1 

for i in range(1, len(S)):
    if S[i] != S[i-1]:
        
        dp[i] = (1 + dp[i-1]) % MOD
    else:
        
        dp[i] = 1


print(sum(dp) % MOD)
