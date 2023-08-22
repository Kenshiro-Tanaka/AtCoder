H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

tmp1 = [] # 1つ目の"o"の座標
tmp2 = [] # 2つ目の"o"の座標
cnt = 1 # 何個目の"o"かを区別するため
for i in range(H):
    for j in range(W):
        if S[i][j] == "o" and cnt == 1:
            cnt = 2
            tmp1 = [i, j]
        if S[i][j] == "o" and cnt == 2:
            tmp2 = [i, j]

print(abs(tmp1[0]-tmp2[0]) + abs(tmp1[1]-tmp2[1]))
