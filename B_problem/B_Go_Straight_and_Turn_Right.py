# https://atcoder.jp/contests/abc244/tasks/abc244_b
# easy
import numpy as np
N = int(input())
P = [char for char in input()]

vec_dic = {1:[1,0], 2:[0, -1], 3:[-1,0], 4:[0,1]}
co = [0,0]
vec = vec_dic[1]
counter_R = 1
for p in P:
  if p == 'R':
    counter_R += 1
    if counter_R == 5:
      counter_R = 1
    vec = vec_dic[counter_R]
  if p == 'S':
    co = np.array(co) + np.array(vec)
else:
  print(str(co[0])+' '+str(co[1]))    