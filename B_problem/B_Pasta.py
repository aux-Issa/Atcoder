# https://atcoder.jp/contests/abc241/tasks/abc241_b
# easy: 8分

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(M):
  if B[i] in A:
    A.remove(B[i])
  else:
    print('No')
    break
else:
  print('Yes')  