# https://atcoder.jp/contests/abc246/tasks/abc246_b
# easy
import math
o = list(map(int, input().split()))
x = math.sqrt(1/((o[0])**2+(o[1])**2))
print(str(o[0]*x)+' '+ str(o[1]*x))