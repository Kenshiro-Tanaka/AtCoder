N = int(input())

print(N//2/N if N%2 == 0 else 1-(N-1)//2/N)


# 別解：素直にカウント
# cnt = 0
# for i in range(1, N+1, 1):
#     if i%2 != 0:
#         cnt += 1

# print(cnt/N)
