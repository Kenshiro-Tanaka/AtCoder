N = int(input())

cnt = 0
for i in range(1, N + 1): # あるiに対してどちらの場合でも7を含まないように
    if not ("7" in list(str(i))):
        if not ("7" in list(oct(i)[2:])): # octを使って8進数に直すとstrになる
            cnt += 1

print(cnt)
