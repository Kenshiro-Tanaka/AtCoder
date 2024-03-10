S = input()

l = [i for i, x in enumerate(S) if x == "|"]

print(S[:l[0]]+S[l[1]+1:])


# 解説にあった短いやつ
# S = input()
# a, b, c = S.split('|')
# print(a+c)
