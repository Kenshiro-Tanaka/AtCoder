N = int(input())

i, tmp = 0, 0
while tmp < N: # N円以上で終了するからN円未満でループ
    i += 1
    tmp += i

print(i)
