N, D = map(int, input().split())
S = [list(input()) for _ in range(N)]

ans = 0 # 最長日数の記録
day = 0 # 連続日数（考えている部分）のカウント
for j in range(D): # 縦に見ていきたいのでiとjの順番を逆に
    flag = True
    for i in range(N):
        if S[i][j] == "x":
            ans = max(ans, day) # これまでの最長との比較
            day = 0 # 次に備えてリセット
            flag = False # 下のif文に入らないように
            break
    
    if flag: # その日がみんな遊べる日なら
        day += 1
    
print(max(ans, day)) # 全部がoのときansに代入されずdayのままなので
