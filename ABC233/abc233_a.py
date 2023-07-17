X, Y = list(map(int,input().split()))

# すでに多めに払っている場合，0枚
# ちょうど払える場合
# 端数分1枚多く払う場合
print(0 if X >= Y else (Y - X) // 10 if (Y - X) % 10 == 0 else (Y - X) // 10 + 1)
