S = list(input())
if S[0]==S[1]==S[2]: # 3文字一致，最初に厳しい条件を
    print('-1')
elif S[0] == S[1]: # 2文字一致
    print(S[2])
elif S[0] == S[2]: # 2文字一致
    print(S[1])
elif S[1]==S[2]: # 2文字一致
    print(S[0])
else: # 文字一致なし
    print(S[0]) 
