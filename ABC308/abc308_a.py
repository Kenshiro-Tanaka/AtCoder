S = list(map(int, input().split()))

flag = False
T = S[:] # 深いコピーにしないと元のリストも変更される
T.sort() # ソートしても同じなら単調増加
if T == S:
    if S[0] >= 100 and S[7] <= 675:
        for i in range(8):
            if S[i] % 25 == 0:
                flag = True

print("NYoe s"[flag::2])
