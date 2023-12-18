# 各桁の和関数
def f(X):
    v = 0
    while X != 0:
        v += X%10
        X //= 10
    return v

N = int(input())

# ハージャッド数の判定
print("Yes" if N%f(N) == 0 else "No")
