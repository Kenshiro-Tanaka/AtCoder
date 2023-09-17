N = int(input())
S = input()

cnt = 0
for i in range(0, len(S)-2, 1):
    if S[i:i+3] == "ABC":
            cnt += 1

print(cnt)
