S = input()

# 文字列から隣接する重複文字を削除する
ans = ""
v = None
for c in S:
    if v != c:
        ans += c
        v = c

print("Yes" if ans in ["A", "B", "C", "AB", "AC", "BC", "ABC"] else "No") # リストに過不足があっても気付きにくいのでこの解法は危険


# 解法1:各アルファベットの個数を数えた後，連結してSに一致すれば良い
# 解法2:アルファベットもソートできる．"".join(sorted(S)) == S
# 解法3:正規表現使う
