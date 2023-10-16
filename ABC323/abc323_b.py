N = int(input())

win = [0]*N
for i in range(N):
    S = input()
    win[i] = S.count("o")

ans = [0]*N # プレイヤー番号を入れる
for i in range(N):
    m = max(win) # 最大勝利数を見つけて
    ans[i] += win.index(m)+1 # その最大値をとるindex+1(プレイヤー番号が1始まり)がプレイヤー番号
    win[win.index(m)] = -1 # 一度選んだ人を選ばないように

print(*ans)
