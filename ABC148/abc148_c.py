A, B = map(int, input().split())

# 最小公倍数を求めれば良い
def f(X, Y): # X < Y 想定
    for i in range(X, X*Y+1, X): # 増分を小さい方にしてXYまでのループでも全探索よりは効率よく
        if i%Y == 0: # Yでも割り切れるときが答え
            print(i)
            break

if A < B:
    f(A, B)
else:
    f(B, A)


# 最小公倍数(LCM)は最大公約数(GCD)を使って求められる
# import math
# def lcm(x,y):
#     return (x*y)//math.gcd(x,y)

# A,B=map(int, input().split())
# print(lcm(A,B))
    
