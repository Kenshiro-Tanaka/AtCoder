N = int(input())
S = input()

s = ""
for c in S:
    s += c # 調べる対象となる文字列，1文字ずつ増やす
    if s.count("A") >= 1 and s.count("B") >= 1 and s.count("C") >= 1:
        print(len(s))
        break
