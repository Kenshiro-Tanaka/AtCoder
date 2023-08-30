N = int(input())

flag = True
# 実際に移動する必要はなく，実行可能か判定するだけ
# i -> i+1で考えるのがポイント
t_old, x_old, y_old = 0, 0, 0
for _ in range(N):
    t, x, y = map(int, input().split())
    dt = t-t_old
    dist = abs(x-x_old) + abs(y-y_old)

    t_old = t
    x_old = x
    y_old = y

    # この問題で使う条件は実は次の2つだけ
    if dt < dist: # 増えた時刻分より多く離れることはできない
        flag = False
    elif dt % 2 != dist % 2: # dtとdistの偶奇は一致するはず（パリティ)，行き来は考えなくて済む
        flag = False

print("NYoe s"[flag::2])
