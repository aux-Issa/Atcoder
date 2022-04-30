# https://atcoder.jp/contests/abc243/tasks/abc243_a
# easy

V, A, B, C = map(int, input().split())

while True:
  V -= A
  if V < 0:
    print('F')
    break
  V -= B
  if V < 0:
    print('M')
    break
  V -= C
  if V < 0:
    print('T')
    break