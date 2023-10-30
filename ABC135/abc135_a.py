A, B = map(int, input().split())

K = (A+B)/2 # A - K = -(B - K)しかありえない
print(int(K) if int(K) == K else "IMPOSSIBLE") # 整数判定思いつかなかった
