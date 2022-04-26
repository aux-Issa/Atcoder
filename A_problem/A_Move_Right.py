# https://atcoder.jp/contests/abc247/tasks/abc247_a
s = [int(a) for a in str(input())]
s.pop()
s.insert(0,0)
res = ''
for i in s:
    res += str(i)

print(res)
