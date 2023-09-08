a, b, c, d = map(int, input().split())

print(max(a*d, a*c, b*c, b*d)) # 結局これでいい


# 全パターン考えるなら
# if a >= 0 and c >= 0: # 正正正正
#     print(b*d)
# elif b <= 0 and d <= 0: # 負負負負
#     print(a*c)
# elif (b <= 0 and c >= 0) or (a >= 0 and d <= 0): # 負負正正 正正負負
#     print(max(a*d, b*c))
# else: # 負正負正
#     print(max(a*c, b*d))
