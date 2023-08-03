n = int(input())

# 2^nは1のnビット左シフトと同じ，powを使うより実行時間が1/20に
print("Yes" if pow(n, 2) < 1<<n else "No")
