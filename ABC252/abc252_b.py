N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(K):
    if A[B[i]-1] == max(A): # indexに注意
        ans = "Yes"
        break
    else:
        ans = "No"

print(ans)
