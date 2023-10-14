N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N-1):
    if A[i] > A[i+1]: # 前の人の方が高かったら
        ans += A[i] - A[i+1] # 差分を答えに足しておいて
        A[i+1] = A[i] # 元の列は高い方に合わせていく

print(ans)
