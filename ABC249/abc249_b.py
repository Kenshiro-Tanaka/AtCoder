import re # 正規表現モジュール
S = input()

s = set(S) # 全ての文字が相異なるなら長さが変わらないはず
flag = False
if re.search("[A-Z]", S) and re.search("[a-z]", S):
    if len(S) == len(s):
        flag = True

print("NYoe s"[flag::2])
