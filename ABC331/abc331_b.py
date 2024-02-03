N, S, M, L = map(int, input().split())

v, ans = 0, 1000000
for i in range(-(-100//6)+1):
    for j in range(-(-100//8)+1):
        for k in range(-(-100//12)+1):
            egg = 6*i + 8*j + 12*k
            v = S*i + M*j + L*k
            if egg >= N: # 個数がN個以上なら
                ans = min(ans, v) # 最小金額を求める

print(ans)

# 切り上げ法 -(-10//3)=-4
