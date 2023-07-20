N = int(input())

# 16進数にしてプレフィックスを除く
a = hex(N)[2:].upper() # upperで大文字に
print("0" + a if len(a) == 1 else a) # 1桁なら先頭に0を付ける
