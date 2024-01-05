Sx, Sy, Gx, Gy = map(int, input().split())

print((Gx - Sx) * Sy / (Sy + Gy) + Sx)

# 出力例1の図から1:2であることを見つけ，y軸の値で内分されていることをなんとか見つけたが
# 本来は目標地点を折り返して，内分点としてx座標を求めれば良い
# 高校でやった内分公式 -> (Sx*Gy + Sy*Gx) / (Sy + Gy) 
