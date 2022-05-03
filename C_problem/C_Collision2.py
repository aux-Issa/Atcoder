# https://atcoder.jp/contests/abc243/tasks/abc243_c
# review is required

N = int(input())
X, Y = [], []
for _ in range(N):
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)
S = input()

right_min, left_max = dict(),dict()
for i in range(N):
  if S[i] == "R":
    if not Y[i] in right_min:
      right_min[Y[i]] = X[i]
    else:
      right_min[Y[i]] = min(X[i], right_min[Y[i]])
  else:
    if not Y[i] in left_max:
      left_max[Y[i]] = X[i]
    else:
      left_max[Y[i]] = max(X[i], left_max[Y[i]])

  if S[i] == 'R':
    if Y[i] in left_max and X[i] < left_max[Y[i]]:
      print('Yes')
      exit(0)
  else:
    if Y[i] in right_min and right_min[Y[i]] < X[i]:
      print('Yes')
      exit(0)

print('No')
