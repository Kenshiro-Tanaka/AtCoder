# 入力された文字列をソートして連結すれば用意するリストは10通り
S = input()
T = input()
S = ''.join(sorted(S)) # S = S[0]+S[1]でも
T = ''.join(sorted(T))

d = {"AB":1, "AC":2, "AD":2, "AE":1, "BC":1, "BD":2, "BE":2, "CD":1, "CE":2, "DE":1}
print("Yes" if d[S] == d[T] else "No")
