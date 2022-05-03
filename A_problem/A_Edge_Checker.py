# https://atcoder.jp/contests/abc240/tasks/abc240_a
# easy: 12分

a, b = map(int, input().split())
if a == 1 and (b == 2 or b == 10):
  print('Yes')
elif b == 10 and (a == 1 or b == 9):
  print('Yes')
elif 2 <= a <= 9 and (b == (a-1) or b == (a+1)):
  print('Yes')
else:
  print('No')  