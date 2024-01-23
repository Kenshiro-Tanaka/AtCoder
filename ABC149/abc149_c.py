X = int(input())

for i in range(X, 10**9+1, 1): # いつ終わるか分からないから10**9+1にしたけど，普通はwhileにして判定関数を呼び出す．
    cnt = 0
    for j in range(2, i, 1): # 2からその数まで割っても割り切れないなら素数
        if i%j != 0:
            cnt += 1
    if cnt == i-2:
        print(i)
        exit()


# 判定関数
# def is_prime(x):
#     if x <= 1:
#         return False
#     for i in range(2, int(x**0.5)+1, 1): #sqrt(x)まで調べればいい
#         if x%i == 0:
#             return False
#     return True

# Nを2数の積で表す時，片方は1からsqrt(N)でもう片方はsqrt(N)からNにある．
