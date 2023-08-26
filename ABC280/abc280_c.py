S = input()
T = input()

for i in range(len(S)): # Tの最後だけ比較できない
    if S[i] != T[i]:
        print(i+1)
        exit()

print(len(T)) # 挿入が最後の文字の場合exitしないでここに来る
