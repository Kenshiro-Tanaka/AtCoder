input()
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 左端と右端を近づけていくことを考えた
print(max(min(B)-max(A)+1, 0)) # 負になったら0にすることをmax(, 0)で簡単に
