N = int(input())
tmp = N # Nがこの後消えるので他の変数に入れる

# 各桁の和は10で割った余りを繰り返すと出る
tmp1 = 0
while N != 0:
    tmp1 += N%10
    N = N//10

print("Yes" if tmp%tmp1 == 0 else "No")


# 各桁の和は sum(list(map(int, str(N)))) でいい
