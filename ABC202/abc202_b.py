def f(num):
    return 9 if num == 6 else 6 if num == 9 else num

S = list(input())

# 文字列を180度回転 -> 後ろから1文字ずつ取り出してconvert
ans = []
for i in reversed(S):
    ans.append(f(int(i)))

print("".join(map(str, ans)))
