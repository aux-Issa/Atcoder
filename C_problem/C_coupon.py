# https://atcoder.jp/contests/abc246/tasks/abc246_c
# review is reqiured
N, K, X = map(int, input().split())
A = list(map(int, input().split()))

ans = sum(A)
remain_k = K
comsumption_one_cool = sum(x //X for x in A)
remain_price = sorted([x % X for x in A], reverse=True)

ans -= X*min(comsumption_one_cool, remain_k)
remain_k -= min(comsumption_one_cool, remain_k)
ans -= sum(remain_price[:remain_k])
print(ans)

