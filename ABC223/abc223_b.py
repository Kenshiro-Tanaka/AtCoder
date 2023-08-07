S = input()

SS = S + S # 文字列を2つ繋げれば左シフト，右シフトに関わらず全パターンのベースになる
l = [] # シフトしたものを全部入れる
for i in range(0, len(S), 1): # len(S)+iからはi番目と同じなのでlen(S)まで
    l.append(SS[i:i+len(S)])

L = sorted(l) # 辞書順で最小と最大が欲しいので一旦ソート
print(L[0])
print(L[len(S)-1])
