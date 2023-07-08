X, Y, N = map(int, input().split())

# X <= Y より N * X <= N * Y
print(min((N // 3) * Y + (N % 3) * X, N * X))
