N = int(input())
d = list(map(int, input().split()))

ans = 0
for i in range(N):
    ans += d[i]*(sum(d)-d[i])

print(ans//2) # 2回同じペアを計算しているので

# 2回ループ回してもいいけど
# for i in range(N):
#     for j in range(N):
#         if i != j:
#             ans += d[i]*d[j]
