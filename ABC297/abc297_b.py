S = list(input()) # 文字列を分けて1文字ずつリストに

# 全てのindexを取得するためにはenumerate()と組み合わせる
B = [i for i, c in enumerate(S) if c == "B"]
K = [i for i, c in enumerate(S) if c == "K"]
R = [i for i, c in enumerate(S) if c == "R"]

ans = "No"
if (B[0] + B[1]) % 2 != 0:
    if R[0] < K[0] < R[1]:
        ans = "Yes"

print(ans)
