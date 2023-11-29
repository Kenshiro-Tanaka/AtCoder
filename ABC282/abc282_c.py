N = int(input())
S = input()

ans = ''
flag = False
for i in range(N):
    if S[i] == '"' and flag == False: # Falseのとき1つ目の"がない
        flag = True
        ans += S[i]
    elif S[i] == ',' and flag == False: # flagがFalseなら括られた文字に入らない
        ans += '.'
    elif S[i] == '"' and flag: # 1つ目の"があるなら
        flag = False
        ans += S[i]
    else: # FlagがTrueのときの','はここに入れたい
        ans += S[i]

print(ans)
