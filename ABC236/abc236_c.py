N, M = map(int, input().split())
S = input().split() # この書き方ってlist()使わなくてもlistになるんだ
T = set(input().split())

for i in S:
    print("Yes" if i in T else "No") # こっちにset(T)してもダメ


# inをlistで使うと全探索するのでO(n)
# setで使うとハッシュテーブルで実装されているのでO(1)
