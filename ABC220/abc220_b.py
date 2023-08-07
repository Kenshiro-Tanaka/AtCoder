def f(K,x): # K進法から10進法に直す関数
    ans = 0
    for i in range(len(str(x))):
        ans += x % 10 * pow(K, i) # 1の位を取り出してK^iをかける
        x //= 10 # 1の位を消してずらす
    return ans

K = int(input())
A, B = map(int, input().split())

print(f(K, A) * f(K, B))
