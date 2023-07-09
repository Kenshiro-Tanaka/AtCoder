N = int(input())
S = input()

if S.count('T') > S.count('A'):
    print('T')
elif S.count('T') < S.count('A'):
    print('A')
else: # 先に達した方の判定は最後の文字だけ見ればいい
    print('A' if S[-1] == 'T' else 'T')
