N = int(input())
W, X = [], []
for i in range(N):
    w, x = map(int, input().split())
    W.append(w)
    X.append(x)

Time_list = [0]*24 # その開始時刻(GMT)で参加できる人数を入れるリスト
for i in range(24):
    for j in range(N):
        if 9 <= (i+X[j])%24 < 18: # 18時開始ではいけない
            Time_list[i] += W[j]

print(max(Time_list))
