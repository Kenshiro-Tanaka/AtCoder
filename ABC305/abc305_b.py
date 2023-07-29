p, q = map(str, input().split())

ans = 0
l = [3, 1, 4, 1, 5, 9]
start_pos = min(ord(p)-ord('A'), ord(q)-ord('A'))  # リストのindexに合わせるためにord('A')を引く
for i in range(abs(ord(p)-ord(q))):
    ans += l[start_pos+i] # 開始位置を与えてからのループ

print(ans)
