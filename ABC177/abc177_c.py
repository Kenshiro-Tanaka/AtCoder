N = int(input())
A = list(map(int, input().split()))

total = sum(A[1:])
ans = 0
for i in range(N-1):
    ans += A[i]*total
    ans %= 10**9+7
    total -= A[i+1]

print(ans)

# 分解する 1*2+1*3+1*4+2*3+2*4+3*4 = 1*(2+3+4)+2*(3+4)+3*(4)
