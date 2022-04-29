# https://atcoder.jp/contests/abc245/tasks/abc245_c
# 解説: https://blog.hamayanhamayan.com/entry/2022/03/26/230115
# review is reqiured
import copy

N, K  = map(int, input().split())
A_B = [list(map(int, input().split())) for l in range(2)]
current=[A_B[0][0],A_B[1][0]]
for i in range(1,N):
  next=[]
  if abs(current[0] - A_B[0][i])<=K:
    next.append(A_B[0][i])
  if abs(current[0] - A_B[1][i])<=K:
    next.append(A_B[1][i])
  if len(current)==2 and abs(current[1] - A_B[0][i])<=K:
    next.append(A_B[0][i])
  if len(current)==2 and abs(current[1] - A_B[1][i])<=K:
    next.append(A_B[1][i])
  next = list(set(next))
  if len(next)==0:
    print('No')
    break
  current = copy.deepcopy(next)
else: 
  print('Yes')