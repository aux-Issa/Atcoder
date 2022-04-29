# https://atcoder.jp/contests/abc245/tasks/abc245_b
# easy
N = int(input())
A = list(map(int, input().split()))
dic = {n:0 for n in range(N)}

for a in A:
  dic[a] = 1

for key, val in dic.items():
  if val == 0:
    print(key)
    break
else: 
  print(N)