L1, R1, L2, R2 = map(int, input().split())

# 塗られていたら+1，被っていたら2になるリスト
ans = [0]*400 # リストを0で初期化するための書き方
for i in range(L1, R1+1):
    ans[i] += 1
for i in range(L2, R2+1):
    ans[i] += 1

# 2の個数が0なら-1したくない
print(ans.count(2)-1 if ans.count(2)>0 else ans.count(2))
