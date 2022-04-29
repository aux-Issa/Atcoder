# https://atcoder.jp/contests/abc245/tasks/abc245_a
# 6分くらい, easy
l = list(map(int, input().split()))
t = [l[0],l[1]]
a = [l[2],l[3]]
if t[0]*60 + t[1] < a[0]*60 + a[1] + 1:
  print('Takahashi')
else:
  print('Aoki')
