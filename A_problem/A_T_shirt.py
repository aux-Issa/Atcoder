# https://atcoder.jp/contests/abc242/tasks/abc242_a
# easy
A, B, C, X = map(int, input().split())
ans = 0
if B < X:
  ans = 0 
elif X<= A:
  ans = 1
else:
  ans = C/(B-A)

print(ans)