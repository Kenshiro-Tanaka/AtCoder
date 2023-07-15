A, B = map(int, input().split())

# 答えが整数になるかどうか
print((A * B / 100) if (B % 100 != 0) else (A * B // 100))
