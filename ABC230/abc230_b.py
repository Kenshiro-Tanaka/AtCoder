S = input()
# Sは最大10文字， Tはoxxの繰り返しなので12文字で十分
T = 'oxxoxxoxxoxxoxx'
flag = False
if S in T:
    flag = True

print("NYoe s"[flag::2])
