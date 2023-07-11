# 地道に確かめて合わせた
S = input()
a, b = map(int, input().split())

print(S[:a-1]+S[b-1]+S[a:b-1]+S[a-1]+S[b:])

# 最初に考えた素直な解法
# S = input()
# a, b = map(int, input().split())
# s = list(S)

# for i in range(1, len(S)+1):
#     if i == a:
#         tmp = s[i-1]
#         s[i-1] = s[b-1]
#     if i == b:
#         s[i-1] = tmp

# print(''.join(s))
