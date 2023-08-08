S = input()

flag = False
if len(S) == 8:
    if 'A' <= S[0] <= 'Z' and 'A' <= S[7] <= 'Z': # 先頭と末尾の条件
        if '1' <= S[1] <= '9' and S[1:7].isdecimal(): # 間の条件
            flag = True
    
print("NYoe s" [flag::2])

# 正規表現を使った別解
# import re
# pattern = r'[A-Z][1-9][0-9]{5}[A-Z]'
# ans = re.match(pattern, s)
