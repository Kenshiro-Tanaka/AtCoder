S = input()
T = input()

# len(T)分の文字列をスライドしながらSから切り取る
l = []
for i in range(len(S)-len(T)+1):
    l.append(S[i:i+len(T)])

# それらのうち一番マッチしている文字数を保持
ans = 0
for i in l:
    cnt = 0
    for j in range(len(i)):
        if i[j] == T[j]:
            cnt += 1
    ans = max(ans, cnt)   

print(len(T)-ans) # 最大値を引けば最小値
