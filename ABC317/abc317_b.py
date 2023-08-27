N = int(input())
A = list(map(int, input().split()))

a = sorted(A)
for i in range(1, N, 1):
    if a[i]-a[i-1] == 2:
        print(a[i]-1)
        break
