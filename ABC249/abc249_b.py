import re
S = input()

s = set(S) # 全ての文字が相異なるなら長さが変わらないはず
if re.search("[A-Z]", S) and re.search("[a-z]", S):
    if len(S) == len(s):
        print("Yes")
    else:
        print("No")
else:
    print("No")
