N = int(input())

ans = 0
for i in range(1, N+1, 1):
    if len(list(str(i)))%2 != 0:
        ans += 1

print(ans)


# 解説見たら文字列に直して桁長を見るまでもなかった
# for i in range(1, N+1, 1):
#     if 1 <= i <= 9:
#         ans += 1
#     elif 100 <= i <= 999:
#         ans += 1
#     elif 10000 <= i <= 99999:
#         ans += 1
