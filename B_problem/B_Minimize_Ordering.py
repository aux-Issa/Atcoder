# https://atcoder.jp/contests/abc242/tasks/abc242_b
# easy: 3分

S = input()
arr = []
for s in S:
  arr.append(s)
arr.sort()

print(''.join(arr))