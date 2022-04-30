# https://atcoder.jp/contests/abc244/tasks/abc244_c
# easy
N = int(input())
num_array = [i for i in range(1, 2*N+1+1)]

a_ans = 1
while not(a_ans == 0):
  t_ans = num_array[0]
  num_array.remove(t_ans)
  print(t_ans, flush=True)
  a_ans = int(input())
  num_array.remove(a_ans)