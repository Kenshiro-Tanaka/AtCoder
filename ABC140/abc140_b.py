N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = 0
for i in range(N): # N-1ではダメなので
    ans += B[A[i]-1]
    if i >= 1 and A[i] - A[i-1] == 1: # i-1にする必要があり，i >= 1も必要に
        ans += C[A[i]-2] # Bとindexが1つずれている
    
print(ans)
