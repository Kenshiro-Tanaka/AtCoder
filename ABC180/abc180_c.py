N = int(input())

# 出力例から約数列挙だということは分かるが普通にやると間に合わなさそう
# sqrt(N)までにしてペアを同時に記録することで
# 計算量半分にしたかったけどforだと入力例1から詰んだからwhile
l = []
i = 1
while i ** 2 <= N: 
    if N % i == 0: # 割り切れるなら，iは約数
        l.append(i) # 約数を記録
        l.append(N // i) # ペアも記録
    i += 1

l.sort()
# 9 = 3 * 3だから[1, 3, 3, 9]で被る
l = list(set(l)) # setで重複消してからlistに戻す
for i in range(len(l)):
    print(l[i])
