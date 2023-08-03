S = []
for _ in range(10):
    s = input()
    S.append(s)

SS = [0]*10 # 行を数えるための配列
for i in range(10):
    if (S[i].find("#") != -1): # findは存在しない場合-1を返す，0ではない
        ans1 = S[i].find("#")
        ans2 = S[i].rfind("#")
        SS[i] = 1 # "#"があるなら配列SSで1が立つ

print(SS.index(1)+1, 10-SS[::-1].index(1)) # indexメソッドに後ろから数える方法がなく，反転して長さから引いた
print(ans1+1, ans2+1) # index揃えるため+1
