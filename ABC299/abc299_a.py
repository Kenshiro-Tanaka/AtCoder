N = int(input())
S = input()

# ピリオドを取り除いて|*|の形で残ればいい
print("in" if S.replace('.','') == '|*|' else "out")
