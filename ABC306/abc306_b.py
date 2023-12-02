A = list(map(int, input().split()))

l2 = [2**x for x in range(64)]
ans = 0
for i in range(64):
    ans += A[i]*l2[i]

print(ans)

# 2乗のリストを用意しなくても
# ans += A[i]*2**iで良かったし
# シフト演算子を使えるとなお良い
# ans += A[i] << i
