# https://atcoder.jp/contests/abc246/tasks/abc246_a

c1 = list(map(int, input().split()))
c2 = list(map(int, input().split()))
c3 = list(map(int, input().split()))
x = [c1[0],c2[0],c3[0]]
y = [c1[1],c2[1],c3[1]]
ans = [i for i in set(x) if x.count(i)==1]
ans = ans + [i for i in set(y) if y.count(i)==1]
print(str(ans[0])+' '+str(ans[1]))