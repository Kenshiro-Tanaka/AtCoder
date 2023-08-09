N = int(input())
S = [input() for _ in range(N)]

flag = True # 「全てに対して」->最初はTrueにして1つでも満たしていないならFalseにする
l1 = ["H", "D", "C", "S"] # 1文字目判定用
l2 = ["A", "T", "J", "Q", "K"] # 2文字目判定用
if len(S) != len(set(S)):
    flag = False
else:
    for c in S:
        if not c[0] in l1:
            flag = False
            break
        elif not (c[1] in l2 or "2" <= c[1] <= "9"):
            flag = False
            break

print("NYoe s" [flag::2])
