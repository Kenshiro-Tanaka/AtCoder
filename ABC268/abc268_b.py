S = input()
T = input()

ans = "No"
if len(S) <= len(T): # これを満たさないと接頭辞じゃない
    if S[0] == T[0] and S in T: # 条件は含まれることに加えて1文字目から合っていること
        ans = "Yes"

print(ans)

# 実はT.startswith(S)でいい
