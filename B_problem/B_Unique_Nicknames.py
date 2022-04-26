# https://atcoder.jp/contests/abc247/tasks/abc247_b
n = int(input())
st = [map(str, input().split()) for _ in range(n)]
s, t = [list(i) for i in zip(*st)]
for i in range(n):
  s_duplication_flag = False
  t_duplication_flag = False
  for j in range(n):
    if i == j:
      continue
    if s[i] == s[j] or s[i] == t[j]:
      s_duplication_flag = True
    if t[i] == t[j] or t[i] == s[j]:
      t_duplication_flag = True
  if s_duplication_flag and t_duplication_flag:
    print('No')
    break
else:
  print('Yes')
