N, M, T = map(int, input().split())

tmp = 0
max_battery = N
for i in range(M):
    a, b = map(int, input().split())
    if N > a - tmp: # a - tmp はカフェ間の移動で減る分
        N -= a - tmp
    else: # このブロックに入るということは必ず途中で0になる
        print("No")
        exit()
    N = min(max_battery, N+b-a) # バッテリーは最大でもmax_batteryになってほしい
    tmp = b

# exit()せずに来たということは最後の充電までいけたということ
print("Yes" if N-T+b > 0 else "No") # (T-b)は最後の充電から帰宅までに減る分
