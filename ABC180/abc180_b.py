N = int(input())
x = list(map(int, input().split()))

# マンハッタン距離
print(sum(map(lambda val: abs(val), x))) # mapで全体に絶対値かけてsumで合計
# ユークリッド距離
print(pow(sum(map(lambda val: abs(val)**2, x)), 1/2))
# チェビシェフ距離
print(max(map(lambda val: abs(val), x)))
