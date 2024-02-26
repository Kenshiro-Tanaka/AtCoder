A, B = list(map(int, input().split()))

d = pow(A*A + B*B, 1/2) # 2点間の距離

print(A/d, B/d) # 大きさ1になる
