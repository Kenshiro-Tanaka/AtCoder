S = input()

ans = 999999999
for i in range(len(S)-2):
    m = int(S[i:i+3])
    ans = min(ans, abs(m-753))

print(ans)
