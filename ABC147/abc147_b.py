S = list(input())

rS = list(reversed(S))
cnt = 0
for i in range(len(S)):
    if S[i] != rS[i]:
        cnt += 1

print(cnt//2) # 逆順にしたものと比べているので同じペアに対して2回カウントしてしまう
