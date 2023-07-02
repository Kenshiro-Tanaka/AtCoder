H, W, X, Y = map(int, input().split())
# この問題は文字列なので以下の書き方でも二次元配列っぽく扱えるが汎用性に乏しい
# grid = [input() for i in range(H)]
# 二次元配列はリストのリストで扱う
grid = []
for i in range(H):
    S = input()
    S = list(S) # 1文字ずつになる
    grid.append(S)

count = 1 # grid[X][Y]自身として1
X -= 1 # indexに揃えるため
Y -= 1 # indexに揃えるため

# grid[X][Y]から障害物に当たるまで数えるだけ
# 遡れるrangeが便利すぎる
# 上
for i in range(X-1, -1, -1): # stopは含まれないから0まで行くなら-1
    if grid[i][Y]==".":
        count += 1
    else:
        break
# 下
for i in range(X+1, H): # index的にはH-1までなのでこれでいい
    if grid[i][Y]==".":
        count += 1
    else:
        break
# 左
for j in range(Y-1, -1, -1):
    if grid[X][j]==".":
        count += 1
    else:
        break
# 右   
for j in range(Y+1, W): # index的にはW-1までなのでこれでいい
    if grid[X][j]==".":
        count += 1
    else:
        break
print(count)
