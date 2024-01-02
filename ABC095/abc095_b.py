N, X = map(int, input().split())
l = []
for i in range(N):
    m = int(input())
    l.append(m)

weight = X - sum(l) # 1つずつ作ったあとの残りの重さ
print(len(l)+weight//min(l)) # 少なくとも1つずつ作るのでlen(l)，それと一番使う量が少ないドーナツを作れば最大個数
