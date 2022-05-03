# https://atcoder.jp/contests/abc247/tasks/abc247_c
# 15分
# easy
import copy
n = int(input())
S = []
S_before = []
for i in range(1,n+1):
  if i ==1:
    S = [1]
    S_before = [1]
    continue
  S.append(i)
  S += S_before
  S_before = copy.deepcopy(S)
else:
  map = map(str, S)
  print(' '.join(map))

