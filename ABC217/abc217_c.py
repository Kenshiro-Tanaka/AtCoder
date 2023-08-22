N = int(input())
P = [0] + list(map(int, input().split()))

Q = [0] * (N+1) # Q=[]とするとappendで前から入れなければならなくなって時間かかるから場所を作ってあげる
for i in range(1, N+1, 1):
    Q[P[i]] = i

print(*Q[1:])
