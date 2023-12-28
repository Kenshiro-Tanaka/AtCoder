a, b, c, d = map(int, input().split())

flag = False
if abs(a-b) <= d and abs(b-c) <= d: # 間接的
    flag = True
if abs(c-a) <= d: # 直接的
    flag = True

print("Yes" if flag else "No")
