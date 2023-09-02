X = int(input())

tmp = 100
cnt = 0
while tmp < X:
    cnt += 1
    tmp = tmp * 101 // 100 # 1.01にして切り捨てすると大きい数で誤差が生じる

print(cnt)
