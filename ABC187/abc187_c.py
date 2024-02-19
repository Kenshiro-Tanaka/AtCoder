N = int(input())
S, l = [], []
for i in range(N):
    s = input()
    S.append(s)
    if s[0] != "!":
        l.append(s)

S = set(S) # set()にしたらTLEしなくなった
l = set(l) # lを用意した効果はなかった

for i in l: # in Sでいい
    if "!"+i in S:
        print(i)
        exit()

print("satisfiable ")


# set()で受け取れば短く書ける
# S = set(input() for i in range(N))
