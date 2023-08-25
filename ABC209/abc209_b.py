N, X = map(int, input().split())
A = list(map(int, input().split()))

# セール時のAを作って和がXより小さければよい
for i in range(N):
    if i % 2 != 0: # 1 <= i <= Nであるため偶奇が逆転
        A[i] -= 1

print("Yes" if sum(A) <= X else "No")
