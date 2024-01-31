s = list(input())

# 左からA，右からZを見つけるだけ
l = s.index("A")
rs = list(reversed(s))
r = rs.index("Z")

r = len(s)-r # sの右から何番目か
print(r-l)
