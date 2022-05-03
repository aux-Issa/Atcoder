N, X = map(int, input().split())
ab = [map(int, input().split()) for _ in range(N)]
a, b = [list(i) for i in zip(*ab)]
dp = [[False]*(X+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(N):
  for j in range(X+1):
    if dp[i][j]:
      if j + a[i] <= X:
        dp[i+1][j+a[i]] = True  
      if j + b[i] <= X:
        dp[i+1][j+b[i]] = True  

print('Yes' if dp[N][X] == True else 'No')
