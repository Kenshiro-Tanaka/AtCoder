N = int(input())
S = list(map(int, input().split()))

minus = 0
for i in range(N):
    print(S[i] - minus, end=" ")
    minus = S[i] # i番目で使ったやつをi+1番目で引きたいからprintした後に代入
