# https://atcoder.jp/contests/abc243/tasks/abc243_b
# easy
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_dic = {A.index(a):a for a in A }
b_dic = {B.index(b):b for b in B }
count_1 = 0
count_2 = 0
for key, val in a_dic.items():
  for k,v in b_dic.items():
    if key==k and val ==v:
      count_1 +=1
    elif key != k and val ==v:
      count_2+=1  
else:
    print(count_1)
    print(count_2)