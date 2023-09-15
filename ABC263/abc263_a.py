l = list(map(int, input().split()))

ans = "No"
if len(set(l)) == 2: # 数字の種類は必ず2種類
    if l.count(l[0]) == 2 or l.count(l[0]) == 3: # 1枚目の数字が2枚か3枚なら
        ans = "Yes"

print(ans)
