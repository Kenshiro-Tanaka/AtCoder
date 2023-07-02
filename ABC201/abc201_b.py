N = int(input())

# ソートの練習 ソートを使いたいから辞書ではなくリスト
# ソートの計算量はO(NlogN)
mount = []
for i in range(N):
    # strで同時に受け取ってintにする
    S, T = map(str, input().split())
    T = int(T)
    # 二次元配列は先頭の要素に沿って並び替えるのでintにして入れ替え
    # l.append(list)で二次元配列に
    mount.append([T,S])

mount.sort()
print(mount[-2][1])
