# https://atcoder.jp/contests/abc246/tasks/abc246_c
# 答え: https://qiita.com/u2dayo/items/4896cea07b59c707df3a#c%E5%95%8F%E9%A1%8Ccoupon
# review is reqiured
N, K, X = map(int, input().split())
A = list(map(int, input().split()))

ans = sum(A)
# 以下の二つの大小
remained_k = K
consumption_one_cool = sum([a // X for a in A])

remained_price = sorted([ a % X for a in A], reverse=True)

ans -= X*min(remained_k, consumption_one_cool)
remained_k -= min(remained_k, consumption_one_cool)
ans -= sum(remained_price[:remained_k])
print(ans)