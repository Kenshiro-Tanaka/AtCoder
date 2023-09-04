# 当てはまったらTrueに変えるビンゴ判定用カード
card = [[False, False, False], [False, False, False], [False, False, False]]

A = [list(map(int, input().split())) for i in range(3)]
N = int(input())
for _ in range(N):
    b = int(input()) # 当てはまったらTrueに変える
    for i in range(3):
        for j in range(3):
            if A[i][j] == b: 
                card[i][j] = True

bingoflag = False# ビンゴ達成かを判定
for i in range(3): # 横一列でビンゴ
    if card[i][0] and card[i][1] and card[i][2]:
        bingoflag = True
        break

for i in range(3): # 縦一列でビンゴ
    if card[0][i] and card[1][i] and card[2][i]:
        bingoflag = True
        break

if card[0][0] and card[1][1] and card[2][2]: # 斜めでビンゴ
    bingoflag = True

if card[0][2] and card[1][1] and card[2][0]: # 斜めでビンゴ
    bingoflag = True

print("NYoe s"[bingoflag::2])
