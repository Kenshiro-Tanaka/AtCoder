X, K, D = map(int, input().split())
    
X = abs(X) # 思いつかなかった
# 0にできるだけ近づいてから振動すればいい
if X-K*D > 0:
    print(X-K*D)
else:
    # X//D 回 Dだけ0に近づく
    cnt = X//D
    pos = X - cnt*D # 0を超える前の座標
    # 残りの X-cnt 回振動した時にどっちにいるか
    print(pos if (K-cnt)%2 == 0 else abs(pos - D))
