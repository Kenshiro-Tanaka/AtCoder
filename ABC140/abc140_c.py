N = int(input())
B = list(map(int, input().split()))

ans, tmp = 0, 10**5+1
for i in range(N-1):
    ans += min(tmp, B[i])
    tmp = B[i]

print(ans+B[-1])


# # 図を書いてリストAを作って考えたものをそのままコードに落としたら
# A = [0]*N
# tmp = 10**5+1
# for i in range(N-1):
#     A[i] = min(tmp, B[i])
#     tmp = B[i]
# A[N-1] = B[N-2]
# print(sum(A))
