# bit演算に気づければ | だけでいい

A, B = map(int, input().split())

def f(X):
    if X == 0:
        return [0, 0, 0]
    elif X == 1:
        return [1, 0, 0]
    elif X == 2:
        return [0, 2, 0]
    elif X == 3:
        return [1, 2, 0]
    elif X == 4:
        return [0, 0, 4]
    elif X == 5:
        return [1, 0, 4]
    elif X == 6:
        return [0, 2, 4]
    else:
        return [1, 2, 4]

la = f(A)
lb = f(B)

ans = 0
for i in range(3):
    if la[i] != 0 or lb[i] != 0: # どちらかが正解していれば
        ans += max(la[i], lb[i]) # 正解している方，つまり大きい方を足す

print(ans)
