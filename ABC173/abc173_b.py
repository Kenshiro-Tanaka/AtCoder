N = int(input())

cnt_AC = 0
cnt_WA = 0
cnt_TLE = 0
cnt_RE = 0
for _ in range(N):
    s = input()
    if s == "AC":
        cnt_AC += 1
    elif s == "WA":
        cnt_WA += 1
    elif s == "TLE":
        cnt_TLE += 1
    elif s == "RE":
        cnt_RE += 1

print("AC x", cnt_AC)
print("WA x", cnt_WA)
print("TLE x", cnt_TLE)
print("RE x", cnt_RE)
