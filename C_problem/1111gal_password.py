# https://atcoder.jp/contests/abc242/tasks/abc242_c
# review is reqiured
# 動的計画法
# pypy
n = int(input())
dp = [[0]*10 for _ in range(n+1)]
for i in range(1,10):
  dp[1][i] = 1
for d in range(2, n+1):
  for i in range(1, 10):
    if i==0:
      dp[d][i] = dp[d-1][i] + dp[d-1][i+1] 
    elif i==9:
      dp[d][i] = dp[d-1][i-1] + dp[d-1][i] 
    else:
      dp[d][i] = dp[d-1][i-1] + dp[d-1][i] + dp[d-1][i+1]
    
    dp[d][i]%=998244353

ans = sum(dp[n])%998244353
print(ans)
