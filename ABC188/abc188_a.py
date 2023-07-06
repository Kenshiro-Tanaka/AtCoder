X, Y = map(int, input().split())

flag = False
if X > Y:
    if X < Y+3:
        flag = True
elif X < Y:
    if X + 3 > Y:
        flag = True
    
print("NYoe s"[flag::2])

# セクシーな別解 絶対値が3未満なら逆転できる どっちが勝っているか関係ない
# print("NYoe s"[abs(X - Y) < 3::2])
