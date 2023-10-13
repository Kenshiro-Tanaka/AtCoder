N, K, M = map(int, input().split())
A = list(map(int, input().split()))

total = sum(A)
print(-1 if N*M > total + K else max(0, N*M - total))
