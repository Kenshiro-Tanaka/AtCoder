N, K = map(int, input().split())
l = list(map(int, input().split()))

sl = sorted(l, reverse=True)
print(sum(sl[:K]))
