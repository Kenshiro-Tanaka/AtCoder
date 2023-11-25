O = input()
E = input()

E += " " # Eの文字列長の方が短い場合に備えて
ans = ""
for i in range(len(O)):
    ans += O[i] + E[i]

print(ans)
