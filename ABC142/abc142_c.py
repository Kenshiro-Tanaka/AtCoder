N = int(input())
A = list(map(int, input().split()))

idx = [*range(N)]
sidx = sorted(idx, key = lambda i: A[i]) # idxをソートする（A[i]の大小で）
sidx = list(map(lambda x: x+1, sidx))

print(*sidx)
